import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import Tracker

tracker = Tracker.Tracker()
tracker.window.show_all()

Gtk.main()
