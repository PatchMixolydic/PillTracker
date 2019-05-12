from gi.repository import Gtk
import BuilderObject, DeleteWarning, TemplateObjects

class PillEdit(BuilderObject.BuilderObject):
    def __init__(self):
        super().__init__("pill_edit")
        self.window = self.builder.get_object("pill_edit_window")
        self.time_edit_container = self.builder.get_object("time_edit_container")

    def on_time_edit_add_clicked(self, widget):
        timeEditor = TemplateObjects.TimeEditor(self.time_edit_container)
        self.time_edit_container.add(timeEditor.time_edit)

    def on_pill_edit_ok_clicked(self, widget):
        NotImplemented

    def on_pill_edit_cancel_clicked(self, widget):
        self.window.close()

    def on_pill_edit_delete_clicked(self, widget):
        warning = DeleteWarning.DeleteWarning()
        warning.window.show_all()
