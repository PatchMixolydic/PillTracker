import BuilderObject

class DeleteWarning(BuilderObject.BuilderObject):
    def __init__(self, pill_editor):
        super().__init__("delete_warning")
        self.window = self.builder.get_object("delete_warning_window")
        self.pill_editor = pill_editor

    def on_delete_pill_cancel_clicked(self, widget):
        self.window.close()

    def on_delete_pill_delete_clicked(self, widget):
        self.pill_editor.delete_pill()
        self.window.close()
        self.pill_editor.window.close()
