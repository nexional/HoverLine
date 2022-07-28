```
 __   __ _______ __   __ _______ ______   ___     ___ __    _ _______ 
|  | |  |       |  | |  |       |    _ | |   |   |   |  |  | |       |
|  |_|  |   _   |  |_|  |    ___|   | || |   |   |   |   |_| |    ___|
|       |  | |  |       |   |___|   |_||_|   |   |   |       |   |___ 
|       |  |_|  |       |    ___|    __  |   |___|   |  _    |    ___|
|   _   |       ||     ||   |___|   |  | |       |   | | |   |   |___ 
|__| |__|_______| |___| |_______|___|  |_|_______|___|_|  |__|_______|

```
# HoverLine

Ever wondered if there was a way to see a line in its entirety without scrolling to right or turning word-wrap on & off again. Specially when the file has long lines and you prefer
word-wrap off for better readability, say for log files.

**HoverLine** can help you there. This package shows the hovered-over line in its entirety as a tooltip, given:

* word-wrap is off for the current view
* the line has some part hidden on either side (gutter or right side)

If you have word-wrap on for the view or no part of the line is hidden then there's no tooltip.

## Installation

* Install [Sublime Text Package Control](https://packagecontrol.io). Skip if installed already
* Go to _Tools > Command Palette_. Select `Package Control: Install Package`
* Type or select `HoverLine` and hit Enter
* Wait for installation to finish

## How to use

Just hover over the line which is not fully visible. It'll show a tooltip showing entire line,
wrapped within given space. By default the tooltip is shown for 3 seconds which is configurable.

Tooltip can be disabled if desired (see **Customization**)

## Customization

You can override the default settings in two ways:

* From _Command Palette_ you can run following commands:
    * `HoverLine: toggle tooltip`
    * `HoverLine: configure tooltip timeout`

* User Settings file (_Preferences > Package Settings > HoverLine > Settings_):
```
{
    // Enable/disable the package
    "enable": true

    // Tooltip timeout in seconds
    "tooltip_timeout": 3
}
```

## License

[GNU General Public License v3.0](https://github.com/nexional/HoverLine/blob/master/LICENSE)

## Issues

Please report any bugs/issues [here](https://github.com/nexional/HoverLine/issues/new)

## My other work

* [CompareBuff](https://packagecontrol.io/packages/CompareBuff)
* [ConvertEpochToDate](https://packagecontrol.io/packages/ConvertEpochToDate)