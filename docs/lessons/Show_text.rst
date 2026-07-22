====================================================
Show Text
====================================================

What is ``display.show()``?
----------------------------------------

``display.show()`` shows text or numbers on the micro:bit screen.

The text does **not** move.

Each letter is shown one at a time.

You can show:

* text
* numbers

Example: Show text
^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from microbit import *

    while True:
        display.show("Hi")

.. note::

    ``while True:`` tells the micro:bit to keep running the code again and again.

    Nearly every micro:bit program uses ``while True:``.


Example: Show a number
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from microbit import *

    while True:
        display.show(7)

----

.. admonition:: Try it

    #. Change the text to your name.
    #. Show the word ``Hello``.
    #. Show your age.
    #. Show your favourite number.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Name

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show("Sam")

            .. tab-item:: Hello

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show("Hello")

            .. tab-item:: Age

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show(11)

            .. tab-item:: Number

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show(8)

----

Show faster or slower
----------------------------------------

You can change how long each letter stays on the screen.

A **smaller** delay is faster.

A **larger** delay is slower.

Fast example

.. code-block:: python

    from microbit import *

    while True:
        display.show("Hello", delay=150)

Slow example

.. code-block:: python

    from microbit import *

    while True:
        display.show("Hello", delay=500)

----

.. admonition:: Try it

    #. Make your name show quickly.
    #. Make your name show slowly.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Fast

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show("Sam", delay=150)

            .. tab-item:: Slow

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show("Sam", delay=500)

----

Challenge
----------------------------------------

Can you make the micro:bit show:

* your name
* your age
* your favourite number

Try changing the speed for each one.

