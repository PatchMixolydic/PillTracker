import datetime, yaml

class YAMLSafeDefaultListDict(yaml.YAMLObject):
    yaml_tag = "!defaultdict"
    yaml_loader = yaml.SafeLoader
    def __init__(self):
        self._dict = {}

    def __getitem__(self, key):
        res = self._dict.get(key, None)
        if res is None:
            res = set()
            self._dict[key] = res
        return self._dict[key]

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __len__(self):
        return len(self._dict)

class Time(yaml.YAMLObject):
    yaml_tag = "!Time"
    yaml_loader = yaml.SafeLoader
    PMOffset = 12  # hours
    def __init__(self, name, hour, minute, notifications = True):
        # hour is 24 hour representation, 0-23
        self.name = name
        self.hour = hour
        self.minute = minute
        self.notifications = notifications

    def get_hour_minute(self):
        """
        :return: "hour:minute" representation
        """
        return "{}:{:02d}".format(self.hour, self.minute)

    def get_datetime_time(self):
        """
        :return: datetime.time representation of this Time
        """
        return datetime.time(hour = self.hour, minute = self.minute)

    @staticmethod
    def from_time_editor(time_editor):
        # Python doesn't have function overloading, so we can't use __init__(self, time_editor).
        # Well, we could use __init__(self, hour_or_time_editor, minute = 0), but the implementation would be awkward.
        name = time_editor.name_entry.get_text()
        hour = int(time_editor.select_hour.get_value())
        # convert from 12 hour to 24 hour
        if time_editor.select_ampm.get_active_id() == "pm":
            hour += Time.PMOffset
        minute = int(time_editor.select_minute.get_value())
        notifications = time_editor.notification_checkbox.get_active()
        return Time(name, hour, minute, notifications)

class Pill(yaml.YAMLObject):
    yaml_tag = "!Pill"
    yaml_loader = yaml.SafeLoader
    def __init__(self, name, times):
        self.name = name
        self.times = times
        self.dates_taken = YAMLSafeDefaultListDict() # (hour, minute): [date, date, date...]

    @staticmethod
    def from_pill_editor(pill_editor):
        name = pill_editor.name_entry.get_text()
        times = list(map(Time.from_time_editor, pill_editor.time_editors))
        res = Pill(name, times)
        return res
