# PillTracker
A useful utility for tracking your medication. You can see if you've taken your
medicine today or on any given day and recieve friendly reminders!

I created this application for two reasons: first, I really needed some practice
with GUI programming. Because of that, I decided to learn GTK for this project.
Second off, I seriously needed a pill tracker so I could stop forgetting my
medicine! I found some for mobile, but none for my Linux desktop where I spend
most of my time.

I must emphasize that this is my first time using GTK. Please, don't take this
as the gold standard for UI programming!

## Dependencies
Dependencies include
[pycairo, PyGObject](https://pygobject.readthedocs.io/en/latest/getting_started.html),
and [pyyaml](https://pyyaml.org/wiki/PyYAMLDocumentation). Additionally, Linux
users will need [notify2](https://pypi.org/project/notify2/) and Windows users
will need [win10toast](https://github.com/jithurjacob/Windows-10-Toast-Notifications)
and its dependencies for notifications.

## Usage
To run the application, simply run main.py with Python 3. Save data is stored in
the savedData directory in YAML format.
