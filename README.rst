
====================
pibooth-extra-lights
====================

|PythonVersions| |PypiPackage| |Downloads|

``pibooth-extra-lights`` is a plugin for the `pibooth <https://github.com/pibooth/pibooth>`_
application.

It adds 3 extra lights:

- **startup**  : light on at ``pibooth`` startup
- **sequence** : light on during the entire capture sequence
- **flash**    : light on when the capture is taken

Install
-------

::

    $ pip3 install pibooth-extra-lights

Configuration
-------------

This is the extra configuration options that can be added in the ``pibooth``
configuration (`physical pin numbering <https://pinout.xyz>`_ is used):

.. code-block:: ini

    [CONTROLS]

    # Physical GPIO OUT pin to light a LED at pibooth startup
    startup_led_pin = 29

    # Physical GPIO OUT pin to light a LED during the entire capture sequence
    preview_led_pin = 31

    # Physical GPIO OUT pin to light a LED when the capture is taken
    flash_led_pin = 33

.. note:: Edit the configuration by running the command ``pibooth --config``.

States description
------------------

Here is the `pibooth state sequence <https://github.com/pibooth/pibooth#states-and-lights-management>`_
with features added by this plugin:

.. image:: https://raw.githubusercontent.com/pibooth/pibooth-extra-lights/master/templates/state_sequence.png
   :align: center
   :alt: State sequence

Circuit diagram
---------------

Here is the diagram for hardware connections.

.. image:: https://raw.githubusercontent.com/pibooth/pibooth-extra-lights/master/templates/sketch.png
   :align: center
   :alt: Electronic sketch


.. |PythonVersions| image:: https://img.shields.io/badge/python-2.7+ / 3.6+-red.svg
   :target: https://www.python.org/downloads
   :alt: Python 2.7+/3.6+

.. |PypiPackage| image:: https://badge.fury.io/py/pibooth-extra-lights.svg
   :target: https://pypi.org/project/pibooth-extra-lights
   :alt: PyPi package

.. |Downloads| image:: https://img.shields.io/pypi/dm/pibooth-extra-lights?color=purple
   :target: https://pypi.org/project/pibooth-extra-lights
   :alt: PyPi downloads
