import datetime
from gi.repository import Gtk
import BuilderObject, DatePicker, PillEdit

class Tracker(BuilderObject.BuilderObject):
    def __init__(self):
        super().__init__("tracker")
        self.window = self.builder.get_object("tracker_window")
        self.date_label = self.builder.get_object("date_label")
        self.set_date(datetime.date.today())

    def on_tracker_window_destroy(self, widget):
        Gtk.main_quit()

    def on_add_pill_button_clicked(self, widget):
        pill_edit = PillEdit.PillEdit()
        pill_edit.window.show_all() # TODO: functionality...

    def on_date_menu_select_activate(self, widget):
        date_picker = DatePicker.DatePicker(self)
        date_picker.window.show_all()

    def on_date_menu_today_activate(self, widget):
        self.set_date(datetime.date.today())

    def set_date(self, date):
        self.date = date
        self.date_label.set_text(date.strftime("%A %x"))
