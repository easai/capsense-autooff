# CapSense AutoOff

## Overview
CapSense AutoOff is a touch‑activated lighting solution powered by the RP2040 Zero. A capacitive sensor connected to GPIO15 lets you switch a NeoPixel on and off with a single touch. Built‑in auto shutoff ensures the light turns off after a set delay, saving power and adding convenience.

Key Features
- Touch control: switch the NeoPixel with a tap
- Auto shutoff: light turns off after a preset delay
- RP2040 Zero microcontroller at the core
- NeoPixel output on GPIO16

Benefits
- No mechanical switches, just smooth touch activation
- Saves energy with automatic shut-off
- Reliable operation with MicroPython

## Hardware
- RP2040 Zero board
- Capacitive touch sensor switch
- Onboard NeoPixel connected to GPIO16
- Sensor output connected to GPIO15

## Pin Configuration
| Component              | RP2040 Zero Pin | Notes                  |
|------------------------|-----------------|------------------------|
| Capacitive Sensor OUT  | GPIO15          | Digital input          |
| NeoPixel Data In       | GPIO16          | Single LED control     |
| Power (VCC)            | 3V3             | Sensor and NeoPixel    |
| Ground (GND)           | GND             | Common ground          |

## Functionality
- Touching the capacitive sensor toggles the NeoPixel state.
- The NeoPixel turns on when activated and shuts off automatically after a set delay.
- The sensor input is read through GPIO15.
- The NeoPixel output is controlled through GPIO16.

## Usage
1. Connect the capacitive sensor to GPIO15 and ground.
2. Connect the NeoPixel to GPIO16 with appropriate power and ground.
3. Load the MicroPython script onto the RP2040 Zero.
4. Touch the sensor to toggle the NeoPixel. It will turn off automatically after the configured delay.
