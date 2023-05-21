# Windows BSOD Simulator

A simple Windows Blue Screen of Death (BSOD) simulator using Python and Pygame.
Some of the code was provided by ChatGPT (GPT4)

## Description

This project provides a graphical simulation of the Windows BSOD screen. The program features:

- Full screen BSOD simulation with accurate colors and fonts
- Progress counter simulating the error information collection process
- Random stop code message selection from an external text file
- Display of a QR code similar to the one found in recent Windows BSOD screens

## Installation

Make sure you have Python 3 installed on your machine. 

You can download Python [here](https://www.python.org/downloads/).

Then, install the required packages using pip:

```bash
pip install -r requirements.txt
```
## Usage
```bash
python bsod.py
```

To exit the program, press the escape key.

## Known issue
If the Windows UI is scaled, the BSOD might look like shit. To fix this I found the python executable, opened its properties dialog, selected the compatability tab and there opened the Change high DPI settings dialog. There I checked both checkboxes and selected "Application" in High DPI settings override.
I've not looked into this issue at all, but if someone does, send me a pull request, open an issue or send a carrier pigeon and I'll patch it.
## License
This project is in the public domain - see the LICENSE file for details
