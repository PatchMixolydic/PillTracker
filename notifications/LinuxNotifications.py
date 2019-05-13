import notify2

notify2.init('Pill Tracker', 'glib')

def send_notification(title, text):
    n = notify2.Notification(title, text, "face-cool")
    n.show()
