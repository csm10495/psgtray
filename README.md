
# Note this is a fork of psgtray that links to PySimpleGUI-4-foss
# Instead of the non-opensource PySimpleGUI 5+
# I'm not planning on updating this, just using it for my own cases.
# pip install psgtray-foss

<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Logo%20with%20text%20for%20GitHub%20Top.png" alt="Python GUIs for Humans">
  <h1 align="center">psgtray</h1>
</p>

Add a System Tray Icon to your tkinter port of PySimpleGUI.


## Installation

Installation is via pip:

`python -m pip install psgtray`

or if you need to upgrade later:

`python -m pip install --upgrade --no-cache-dir psgtray`


## Adding To Your PySimpleGUI Program

This is a copy of the demo program that can be found in the PySimpleGUI Project's Demo Program folder.

```python
import PySimpleGUI as sg
from psgtray import SystemTray

"""
    A System Tray Icon courtesy of pystray and your friends at PySimpleGUI

    Import the SystemTray object with this line of code:
    from psgtray import SystemTray

    Key for the system tray icon is:
        tray = SystemTray()
        tray.key

    values[key] contains the menu item chosen.

    One trick employed here is to change the window's event to be the event from the System Tray.


    Copyright PySimpleGUI 2021
"""

def main():

    menu = ['', ['Show Window', 'Hide Window', '---', '!Disabled Item', 'Change Icon', ['Happy', 'Sad', 'Plain'], 'Exit']]
    tooltip = 'Tooltip'

    layout = [[sg.Text('My PySimpleGUI Celebration Window - X will minimize to tray')],
              [sg.T('Double clip icon to restore or right click and choose Show Window')],
              [sg.T('Icon Tooltip:'), sg.Input(tooltip, key='-IN-', s=(20,1)), sg.B('Change Tooltip')],
              [sg.Multiline(size=(60,10), reroute_stdout=False, reroute_cprint=True, write_only=True, key='-OUT-')],
              [sg.Button('Go'), sg.B('Hide Icon'), sg.B('Show Icon'), sg.B('Hide Window'), sg.Button('Exit')]]

    window = sg.Window('Window Title', layout, finalize=True, enable_close_attempted_event=True)


    tray = SystemTray(menu, single_click_events=False, window=window, tooltip=tooltip, icon=sg.DEFAULT_BASE64_ICON)
    tray.show_message('System Tray', 'System Tray Icon Started!')
    sg.cprint(sg.get_versions())
    while True:
        event, values = window.read()

        # IMPORTANT step. It's not required, but convenient. Set event to value from tray
        # if it's a tray event, change the event variable to be whatever the tray sent
        if event == tray.key:
            sg.cprint(f'System Tray Event = ', values[event], c='white on red')
            event = values[event]       # use the System Tray's event as if was from the window

        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.cprint(event, values)
        tray.show_message(title=event, message=values)

        if event in ('Show Window', sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED):
            window.un_hide()
            window.bring_to_front()
        elif event in ('Hide Window', sg.WIN_CLOSE_ATTEMPTED_EVENT):
            window.hide()
            tray.show_icon()        # if hiding window, better make sure the icon is visible
            # tray.notify('System Tray Item Chosen', f'You chose {event}')
        elif event == 'Happy':
            tray.change_icon(sg.EMOJI_BASE64_HAPPY_JOY)
        elif event == 'Sad':
            tray.change_icon(sg.EMOJI_BASE64_FRUSTRATED)
        elif event == 'Plain':
            tray.change_icon(sg.DEFAULT_BASE64_ICON)
        elif event == 'Hide Icon':
            tray.hide_icon()
        elif event == 'Show Icon':
            tray.show_icon()
        elif event == 'Change Tooltip':
            tray.set_tooltip(values['-IN-'])

    tray.close()            # optional but without a close, the icon may "linger" until moused over
    window.close()

if __name__ == '__main__':
    main()
```

# Limitations

The Windows implementation is working well.  The Linux GTK version, not as well.

Updating the Menu after initial creation is not yet supported.

# Requirements

In order to use this pacakge you'll also need these packages:

* PySimpleGUI
* pystray (licensed under LGPL3)

Currently only versions <= 0.18.0 of pystray are supported


## Release Notes

### psgtray 1.0.2  12-Jan-2022

* Changed pypi setup to indicate version of pystray needs to be <= 0.18.0


### psgtray 1.0.1  21-Jun-2021

* Initial Release

# Support

Please open Issues in the main PySimpleGUI GitHub by with using the `psgisues` utility, the PySimpleGUI test harness, or go to https://Issues.PySimpleGUI.org.


# Designed and written by

mike from PySimpleGUI.org

# Contributing

Like the PySimpleGUI project, the psgtray project is currently licensed under an open-source license, the project itself is structured like a proprietary product.  Pull Requests are not accepted.


# License
GNU Lesser General Public License (LGPL 3) +

# Copyright
Copyright 2021 PySimpleGUI