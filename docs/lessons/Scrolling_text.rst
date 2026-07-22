====================================================
Scrolling Text
====================================================

What is ``display.scroll()``?
----------------------------------------

``display.scroll()`` moves text or numbers across the micro:bit screen.

You can scroll:

* text
* numbers

Example: Scroll text
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from microbit import *

    while True:
        display.scroll("Hi")

Example: Scroll a number
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from microbit import *

    while True:
        display.scroll(7)

----

.. admonition:: Try it

    #. Change the message to your name.
    #. Change the message to ``Hello``.
    #. Change the number to your age.
    #. Change the number to your favourite number.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Name

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll("Sam")

            .. tab-item:: Hello

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll("Hello")

            .. tab-item:: Age

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll(11)

            .. tab-item:: Favourite number

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll(8)

----

Challenge
----------------------------------------

Make your micro:bit scroll:

* your name
* your age
* your favourite number


