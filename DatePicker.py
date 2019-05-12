import datetime
import BuilderObject

class DatePicker(BuilderObject.BuilderObject):
    def __init__(self, tracker):
        super().__init__("date_picker")
        self.window = self.builder.get_object("date_picker_window")
        self.calendar = self.builder.get_object("date_picker_calendar")
        self.tracker = tracker

    def on_date_picker_ok_clicked(self, widget):
        year = self.calendar.get_property("year")
        month = self.calendar.get_property("month") + 1 # GtkCalendar returns month - 1. Day and year are already right.
        day = self.calendar.get_property("day")
        self.tracker.set_date(datetime.date(year, month, day))
        self.window.close()

    def on_date_picker_cancel_clicked(self, widget):
        self.window.close()
