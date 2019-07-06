import sys
from gi.repository import Gtk

ApplicationPathTemplate = "{}/res/{}.glade".format(sys.path[0], '{}')

class BuilderObject:
    def __init__(self, resourceName):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(ApplicationPathTemplate.format(resourceName))
        self.builder.connect_signals(self)
