from win10toast import ToastNotifier

toaster = ToastNotifier()

def send_notification(title, text):
    toaster.show_toast(
        title,
        text
    )