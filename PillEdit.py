from gi.repository import Gtk
import BuilderObject, DeleteWarning, PillData, TemplateObjects

class PillEdit(BuilderObject.BuilderObject):
    def __init__(self, tracker, pill = None):
        super().__init__("pill_edit")
        self.window = self.builder.get_object("pill_edit_window")
        self.time_edit_container = self.builder.get_object("time_edit_container")
        self.name_entry = self.builder.get_object("pill_name_entry")
        self.delete_button = self.builder.get_object("pill_edit_delete")
        self.buttons_container = self.builder.get_object("pill_edit_buttons_container")
        self.tracker = tracker
        self.old_pill = pill
        self.time_editors = []
        if self.old_pill is not None:
            # Populate the fields with the old values
            self.name_entry.set_text(self.old_pill.name)
            for time in self.old_pill.times:
                time_editor = TemplateObjects.TimeEditor.from_time(time, self)
                self.add_time_editor(time_editor)

    def new_mode(self):
        # Changes this window into a new pill window rather than an edit pill window
        self.window.set_title("Create new pill")
        self.buttons_container.remove(self.delete_button)

    def delete_pill(self):
        self.tracker.delete_pill(self.old_pill)

    def on_time_edit_add_clicked(self, widget):
        time_editor = TemplateObjects.TimeEditor(self)
        self.add_time_editor(time_editor)

    def add_time_editor(self, time_editor):
        self.time_edit_container.add(time_editor.time_edit)
        self.time_editors.append(time_editor)

    def on_pill_edit_ok_clicked(self, widget):
        newPill = PillData.Pill.from_pill_editor(self)
        if self.old_pill is not None:
            # Remove the old pill
            self.tracker.delete_pill(self.old_pill)
        self.tracker.add_pill(newPill)
        self.window.close()

    def on_pill_edit_cancel_clicked(self, widget):
        self.window.close()

    def on_pill_edit_delete_clicked(self, widget):
        warning = DeleteWarning.DeleteWarning(self)
        warning.window.show_all()
