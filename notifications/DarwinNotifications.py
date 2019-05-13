# These imports are part of pyobjc:
from Foundation import NSUserNotification
from Foundation import NSUserNotificationCenter
from Foundation import NSUserNotificationDefaultSoundName

def send_notification(title, text, wantSound=True):
    # Use NSUserNotification to construct our notification:
    notification = NSUserNotification.alloc().init()
    notification.setTitle_(title)
    notification.setInformativeText_(text)
    if wantSound:
        notification.setSoundName_(NSUserNotificationDefaultSoundName)

    # Now, deliver that notification to the default macOS notification center:
    center = NSUserNotificationCenter.defaultUserNotificationCenter()
    center.deliverNotification_(notification)
