from gi.repository import Gtk
import BuilderObject, PillData, PillEdit

class PillFrame(BuilderObject.BuilderObject):
    def __init__(self, pill, tracker):
        super().__init__("pill_template")
        self.frame = self.builder.get_object("pill_frame")
        self.name = self.builder.get_object("pill_name")
        self.time_tracker_container = self.builder.get_object("pill_time_track_container")
        self.tracker = tracker
        self.pill = pill
        self.name.set_text(self.pill.name)

    def on_pill_edit_clicked(self, widget):
        pill_edit = PillEdit.PillEdit(self.tracker, self.pill)
        pill_edit.window.show_all()

class TimeTracker(BuilderObject.BuilderObject):
    def __init__(self):
        super().__init__("time_track_template")
        self.checkbox = self.builder.get_object("time_track_checkbox")
        self.name = self.builder.get_object("time_track_name")
        self.alert = self.builder.get_object("time_track_alert")

    def on_time_track_checkbox(self, widget):
        NotImplemented

class TimeEditor(BuilderObject.BuilderObject):
    def __init__(self, pill_editor):
        super().__init__("time_edit_template")
        self.time_edit = self.builder.get_object("time_edit")
        self.select_hour = self.builder.get_object("time_select_hour")
        self.select_minute = self.builder.get_object("time_select_minute")
        self.select_ampm = self.builder.get_object("time_select_ampm")
        self.name_entry = self.builder.get_object("time_name_entry")
        self.notification_checkbox = self.builder.get_object("time_notification_checkbox")
        self.pill_editor = pill_editor
        self.prev_and_curr_minute_values = [0, 0] # previous, current

    @staticmethod
    def from_time(time, pill_editor):
        res = TimeEditor(pill_editor)
        hour = time.hour # Get local copy so we don't edit the time
        if hour >= PillData.Time.PMOffset:
            hour -= PillData.Time.PMOffset
            res.select_ampm.set_active_id("pm")
        res.select_hour.set_value(hour)
        res.select_minute.set_value(time.minute)
        res.name_entry.set_text(time.name)
        res.notification_checkbox.set_active(time.notifications)
        return res

    def on_time_select_hour_output(self, widget):
        hour = int(self.select_hour.get_value())
        self.select_hour.set_property("text", str(12 if hour == 0 else hour))
        return True

    def on_time_select_minute_output(self, widget):
        minute = int(self.select_minute.get_value())
        self.select_minute.set_property("text", "{:02d}".format(minute))
        return True

    def on_time_select_minute_value_changed(self, widget):
        minute = int(self.select_minute.get_value())
        self.prev_and_curr_minute_values.pop(0) # pop from top (old previous)
        self.prev_and_curr_minute_values.append(minute) # push to bottom (new current)

    def on_time_select_hour_wrapped(self, widget):
        # switch am and pm
        self.select_ampm.set_active_id(
            "am" if self.select_ampm.get_active_id() == "pm" else "pm"
        )

    def on_time_select_minute_wrapped(self, widget):
        # GTK doesn't let us see which way the spinner wrapped, so this must be worked around
        minute = int(self.select_minute.get_value())
        if self.prev_and_curr_minute_values[0] == 59:
            self.select_hour.spin(Gtk.SpinType.STEP_FORWARD, 1)
        elif self.prev_and_curr_minute_values[0] == 0:
            self.select_hour.spin(Gtk.SpinType.STEP_BACKWARD, 1)
        else:
            raise ValueError("time_select_minute wrapped at unusual value {}!".format(self.prev_and_curr_minute_values[0]))

    def on_time_remove_button_clicked(self, widget):
        self.pill_editor.time_edit_container.remove(self.time_edit)
        self.pill_editor.time_editors.remove(self)
