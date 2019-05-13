import datetime, sys
from gi.repository import Gtk
import BuilderObject, DatePicker, PillEdit, TemplateObjects

class Tracker(BuilderObject.BuilderObject):
    def __init__(self):
        super().__init__("tracker")
        self.window = self.builder.get_object("tracker_window")
        self.date_label = self.builder.get_object("date_label")
        self.pills_container = self.builder.get_object("pills_container")
        self.no_pills_label = self.builder.get_object("no_pills_label")
        self.date = None
        self.pills = []
        self.pill_to_widget = {}
        self.set_date(datetime.date.today())

    def on_tracker_window_destroy(self, widget):
        Gtk.main_quit()

    def on_add_pill_button_clicked(self, widget):
        pill_edit = PillEdit.PillEdit(self)
        pill_edit.new_mode()
        pill_edit.window.show_all()

    def on_date_menu_select_activate(self, widget):
        date_picker = DatePicker.DatePicker(self)
        date_picker.window.show_all()

    def on_date_menu_today_activate(self, widget):
        self.set_date(datetime.date.today())

    def set_date(self, date):
        self.date = date
        self.date_label.set_text(date.strftime("%A %x"))
        for pill in self.pills:
            widget = self.pill_to_widget.get(pill, None)
            if widget is None:
                continue
            for time_tracker in widget.time_trackers:
                dates_taken = pill.dates_taken[time_tracker.time]
                time_tracker.checkbox.set_active(self.date in dates_taken)


    def add_pill(self, pill):
        self.pills_container.remove(self.no_pills_label)
        self.pills.append(pill)
        widget = TemplateObjects.PillFrame(pill, self)
        self.pills_container.add(widget.frame)
        self.pill_to_widget.update({pill: widget})
        self.save_pills()

    def delete_pill(self, pill):
        try:
            self.pills.remove(pill)
        except ValueError:
            # It might have already been removed due to some race condition.
            print("Couldn't remove pill {} from tracker.pills!".format(pill.name), file = sys.stderr)
        pillWidget = self.pill_to_widget.pop(pill, None) # Get the pill's widget, if it exists
        if pillWidget is not None: # If there was a widget, remove it
            self.pills_container.remove(pillWidget.frame)
            pillWidget = None
        if len(self.pills) == 0:
            self.pills_container.pack_start(self.no_pills_label, True, True, 0)
        self.save_pills()

    def save_pills(self):
        print("TODO: save pills")
