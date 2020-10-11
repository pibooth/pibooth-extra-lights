# -*- coding: utf-8 -*-

"""Pibooth plugin for extra lights management."""

import pibooth
from gpiozero import LEDBoard


__version__ = "1.0.1"


@pibooth.hookimpl
def pibooth_configure(cfg):
    """Declare the new configuration options"""
    cfg.add_option('CONTROLS', 'startup_led_pin', 29,
                   "Physical GPIO OUT pin to light a LED at pibooth startup (list of pins accepted)")
    cfg.add_option('CONTROLS', 'preview_led_pin', 31,
                   "Physical GPIO OUT pin to light a LED during the entire capture sequence (list of pins accepted)")
    cfg.add_option('CONTROLS', 'flash_led_pin', 33,
                   "Physical GPIO OUT pin to light a LED when the capture is taken (list of pins accepted)")


@pibooth.hookimpl
def pibooth_startup(app, cfg):
    """Create the LED instances.

    .. note:: gpiozero is configured as BCM, use a string with "BOARD" to
               use BOARD pin numbering.
    """
    app.led_startup = LEDBoard(*("BOARD{}".format(pin)
                               for pin in cfg.gettuple('CONTROLS', 'startup_led_pin', int)))

    app.led_sequence = LEDBoard(*("BOARD{}".format(pin)
                                for pin in cfg.gettuple('CONTROLS', 'preview_led_pin', int)))

    app.led_flash = LEDBoard(*("BOARD{}".format(pin)
                             for pin in cfg.gettuple('CONTROLS', 'flash_led_pin', int)))

    app.led_startup.on()


@pibooth.hookimpl
def state_preview_enter(app):
    """Start a new capture sequence."""
    app.led_sequence.on()


@pibooth.hookimpl
def state_capture_enter(app):
    """Ready to take a capture."""
    app.led_flash.on()


@pibooth.hookimpl
def state_capture_exit(app):
    """A capture has been taken."""
    app.led_flash.off()


@pibooth.hookimpl
def state_processing_enter(app):
    """The capture sequence is done."""
    app.led_sequence.off()
