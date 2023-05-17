# -*- coding: utf-8 -*-

"""Pibooth plugin for extra lights management."""

import pibooth
from gpiozero import LEDBoard


__version__ = "1.0.2"


@pibooth.hookimpl
def pibooth_configure(cfg):
    """Declare the new configuration options"""
    cfg.add_option('CONTROLS', 'startup_led_pin', 29,
                   "Physical GPIO OUT pin to light a LED at pibooth startup (list of pins accepted)")
    cfg.add_option('CONTROLS', 'startup_led_active_high', True,
                   "If True, startup LED is lighting by setting pin(s) to HIGH else by setting to LOW")
    cfg.add_option('CONTROLS', 'preview_led_pin', 31,
                   "Physical GPIO OUT pin to light a LED during the entire capture sequence (list of pins accepted)")
    cfg.add_option('CONTROLS', 'preview_led_active_high', True,
                   "If True, preview LED is lighting by setting pin(s) to HIGH else by setting to LOW")
    cfg.add_option('CONTROLS', 'flash_led_pin', 33,
                   "Physical GPIO OUT pin to light a LED when the capture is taken (list of pins accepted)")
    cfg.add_option('CONTROLS', 'flash_led_active_high', True,
                   "If True, flash LED is lighting by setting pin(s) to HIGH else by setting to LOW")


@pibooth.hookimpl
def pibooth_startup(app, cfg):
    """Create the LED instances.

    .. note:: gpiozero is configured as BCM, use a string with "BOARD" to
               use BOARD pin numbering.
    """
    app.led_startup = LEDBoard(*("BOARD{}".format(pin)
                               for pin in cfg.gettuple('CONTROLS', 'startup_led_pin', int)),
                               active_high=cfg.getboolean('CONTROLS', 'startup_led_active_high'))

    app.led_sequence = LEDBoard(*("BOARD{}".format(pin)
                                for pin in cfg.gettuple('CONTROLS', 'preview_led_pin', int)),
                                active_high=cfg.getboolean('CONTROLS', 'preview_led_active_high'))

    app.led_flash = LEDBoard(*("BOARD{}".format(pin)
                             for pin in cfg.gettuple('CONTROLS', 'flash_led_pin', int)),
                             active_high=cfg.getboolean('CONTROLS', 'flash_led_active_high'))

    # Initial state
    app.led_startup.on()
    app.led_sequence.off()
    app.led_flash.off()


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
