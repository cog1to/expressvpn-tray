# ExpressVPN Tray Icon

Tray icon for displaying status of ExpressVPN client/daemon on Linux desktops.

Icons are copied from Mac version of ExpressVPN client.

## Requirements

Requires Gtk3 for building and running since it's using Gtk3's StatusIcon for controlling system tray.

## Building

It's just a python script, duh.

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
