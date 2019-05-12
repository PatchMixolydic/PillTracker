from gi.repository import Gtk

class BuilderObject:
    def __init__(self, resourceName):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("res/{}.glade".format(resourceName))
        self.builder.connect_signals(self)
