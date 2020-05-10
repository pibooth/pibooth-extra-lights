# -*- coding: utf-8 -*-

"""Pibooth plugin for extra lights management."""

import pibooth
from gpiozero import LED


__version__ = "1.0.0"


@pibooth.hookimpl
def pibooth_configure(cfg):
    """Declare the new configuration options"""
    cfg.add_option('CONTROLS', 'startup_led_pin', 29,
                   "Physical GPIO OUT pin to light a LED at pibooth startup")
    cfg.add_option('CONTROLS', 'preview_led_pin', 31,
                   "Physical GPIO OUT pin to light a LED during the entire capture sequence")
    cfg.add_option('CONTROLS', 'flash_led_pin', 33,
                   "Physical GPIO OUT pin to light a LED when the capture is taken")


@pibooth.hookimpl
def pibooth_startup(app, cfg):
    """Create the LED instances.

    .. note :: gpiozero is configured as BCM, use a string with "BOARD" to
               use BOARD pin numbering.
    """
    app.led_startup = LED("BOARD" + cfg.get('CONTROLS', 'startup_led_pin'))
    app.led_sequence = LED("BOARD" + cfg.get('CONTROLS', 'preview_led_pin'))
    app.led_flash = LED("BOARD" + cfg.get('CONTROLS', 'flash_led_pin'))

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
