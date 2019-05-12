import BuilderObject

class DeleteWarning(BuilderObject.BuilderObject):
    def __init__(self):
        super().__init__("delete_warning")
        self.window = self.builder.get_object("delete_warning_window")

    def on_delete_pill_cancel_clicked(self, widget):
        self.window.close()

    def on_delete_pill_delete_clicked(self, widget):
        NotImplemented
