PMOffset = 12  # hours

class Time:
    def __init__(self, hour, minute):
        # hour is 24 hour representation, 0-23
        self.hour = hour
        self.minute = minute

    @staticmethod
    def from_time_editor(self, time_editor):
        # Python doesn't have function overloading, so we can't use __init__(self, time_editor).
        # Well, we could use __init__(self, hour_or_time_editor, minute = 0), but the implementation would be awkward.
        hour = int(time_editor.select_hour.get_value())
        # convert from 12 hour to 24 hour
        if time_editor.select_ampm.get_active_id() == "pm":
            hour += PMOffset
        minute = int(time_editor.select_minute.get_value())
        return Time(hour, minute)

class Pill:
    def __init__(self, name, times):
        self.name = name
        self.times = times
