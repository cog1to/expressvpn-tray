# ExpressVPN Tray Icon

Tray icon for displaying status of ExpressVPN client/daemon on Linux desktops.

Icons are copied from Mac version of ExpressVPN client.

## Requirements

Requires Gtk3 for building and running since it's using Gtk3's StatusIcon for controlling system tray.

The logic relies on the `expressvpn` CLI utility output, so there's a chance it could break with the next released version of ExpressVPN. In that case, feel free to file an issue here, so I can update the code.

## Building

It's just a python script, duh.

## Installing

```
sudo pip3 install .
```

## Running

Can be as simple as
```
expressvpn-tray &
```

But given that StatusIcon is deprecated in Gtk3, it will produce deprecation warnings while it's running. So I recommend to do this instead:
```
expressvpn-tray 1>/dev/null 2>&1  &
```
