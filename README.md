# Tray icon for displaying status of ExpressVPN client/daemon on Linux desktops.

## Requirements

Requires Gtk3 for building and running since it's using Gtk3's StatusIcon for controlling system tray.

## Building

Not required.

## Packaging

```
python3 setup.py sdist
```

## Installing

```
sudo pip3 install .
```

or

```
sudo python3 setup.py install
```
