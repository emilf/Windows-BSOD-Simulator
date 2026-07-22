# Windows BSOD Simulator

NOTE: This doesn't work on my machine anymore, so probably requires some fixes.
      Also, when running this on non-windows machines, you need to comment out
      the DPI aware line and make sure you have the right fonts installed.

      Also, Dependabot keeps complaining about security issues in the library
      versions this code uses, though, as this is local, non-networked code,
      I'm not sure how the issues would affect you.

A simple Windows Blue Screen of Death (BSOD) simulator using Python and Pygame.
Some of the code was provided by ChatGPT (GPT4)

## Description

This project provides a graphical simulation of the Windows BSOD screen.
The program features:

- Full screen BSOD simulation with accurate colors and fonts
- Progress counter simulating the error information collection process
- Random stop code message selection from an external text file
- Display of a QR code similar to the one found in recent Windows BSOD screens with a configurable URL in the code (defaults to rickrolling)

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

## License

This project is in the public domain - see the LICENSE file for details
