from gi.repository import Gtk
import BuilderObject, DeleteWarning, PillData, TemplateObjects

class PillEdit(BuilderObject.BuilderObject):
    def __init__(self, tracker):
        super().__init__("pill_edit")
        self.window = self.builder.get_object("pill_edit_window")
        self.time_edit_container = self.builder.get_object("time_edit_container")
        self.name_entry = self.builder.get_object("pill_name_entry")
        self.tracker = tracker
        self.time_editors = []

    def on_time_edit_add_clicked(self, widget):
        time_editor = TemplateObjects.TimeEditor(self)
        self.time_edit_container.add(time_editor.time_edit)
        self.time_editors.append(time_editor)

    def on_pill_edit_ok_clicked(self, widget):
        pill = PillData.Pill.from_pill_editor(self)
        self.tracker.add_pill(pill)
        self.window.close()

    def on_pill_edit_cancel_clicked(self, widget):
        self.window.close()

    def on_pill_edit_delete_clicked(self, widget):
        warning = DeleteWarning.DeleteWarning()
        warning.window.show_all()
