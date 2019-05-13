import collections

class Time:
    PMOffset = 12  # hours
    def __init__(self, name, hour, minute, notifications = True):
        # hour is 24 hour representation, 0-23
        self.name = name
        self.hour = hour
        self.minute = minute
        self.notifications = notifications

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

class Pill:
    def __init__(self, name, times):
        self.name = name
        self.times = times
        self.dates_taken = collections.defaultdict(list) # time: [date, date, date...]

    @staticmethod
    def from_pill_editor(pill_editor):
        name = pill_editor.name_entry.get_text()
        times = list(map(Time.from_time_editor, pill_editor.time_editors))
        res = Pill(name, times)
        if pill_editor.old_pill is not None:
            # copy data from old pill
            res.dates_taken = pill_editor.old_pill.dates_taken
        return res
