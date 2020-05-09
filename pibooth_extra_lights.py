# -*- coding: utf-8 -*-

"""Pibooth plugin for extra lights management.
"""

import pibooth
from gpiozero import LED


__version__ = "1.0.0"


@pibooth.hookimpl
def pibooth_configure(cfg):
    """Declare the new configuration entries.
    """
    pass


@pibooth.hookimpl
def pibooth_startup(app, cfg):
    """Create the LED instances.

    .. note :: gpiozero is configured as BCM, use a string with "BOARD" to
               convert on BOARD.
    """
    app.led_startup = LED("BOARD" + cfg.get('CONTROLS', 'startup_led_pin'))
    app.led_sequence = LED("BOARD" + cfg.get('CONTROLS', 'preview_led_pin'))
    app.led_flash = LED("BOARD" + cfg.get('CONTROLS', 'flash_led_pin'))

    app.led_startup.on()


@pibooth.hookimpl
def state_preview_enter(app):
    app.led_sequence.on()


@pibooth.hookimpl
def state_capture_enter(app):
    app.led_flash.on()


@pibooth.hookimpl
def state_capture_exit(app):
    app.led_flash.off()


@pibooth.hookimpl
def state_processing_enter(app):
    app.led_sequence.off()
