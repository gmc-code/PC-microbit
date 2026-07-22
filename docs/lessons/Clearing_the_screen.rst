====================================================
Clearing the Screen
====================================================

WHne using show, the last letter stays on the screen.

You can clear the screen to make it blank.

Sometimes you want to **pause** before clearing the screen.

Use ``sleep()`` to pause your program.

``sleep(1000)`` pauses for **1 second**.

Useful times:

* ``250`` = quarter of a second
* ``500`` = half a second
* ``1000`` = 1 second
* ``2000`` = 2 seconds

----

Using ``display.clear()``
----------------------------------------

.. code-block:: python

    from microbit import *

    while True:
        display.show("Hi")
        sleep(1000)
        display.clear()
        sleep(1000)

The program:

1. shows **Hi**
2. waits for 1 second
3. clears the screen
4. waits for 1 second
5. repeats

----

.. admonition:: Try it

    #. Show your name.
    #. Wait 1 second.
    #. Clear the screen.
    #. Wait 1 second.
    #. Show your age.
    #. Wait 1 second.
    #. Clear the screen.
    #. Wait 1 second.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Solution

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show("Sam")
                        sleep(1000)
                        display.clear()
                        sleep(1000)

                        display.show(11)
                        sleep(1000)
                        display.clear()
                        sleep(1000)

----

Changing the pause
----------------------------------------

Change the number inside ``sleep()`` to change how long the pause lasts.

Example

.. code-block:: python

    sleep(500)

waits for **half a second**.

.. code-block:: python

    sleep(2000)

waits for **2 seconds**.

----

.. admonition:: Try it

    #. Change every sleep to ``500``.
    #. Change every sleep to ``2000``.
    #. Make the first sleep ``500`` and the second sleep ``2000``.

----

Using ``clear=True``
----------------------------------------

Instead of writing

.. code-block:: python

    display.clear()

you can write

.. code-block:: python

    display.show("Hi", clear=True)

The screen is cleared automatically after the text is shown.

Example

.. code-block:: python

    from microbit import *

    while True:
        display.show("Hello", clear=True)
        sleep(1000)

----

Show two messages
----------------------------------------

You can show more than one message.

.. code-block:: python

    from microbit import *

    while True:
        display.show("My name")
        sleep(1000)
        display.show("Sam")
        sleep(1000)
        display.clear()
        sleep(1000)

Another example

.. code-block:: python

    from microbit import *

    while True:
        display.show("I like")
        sleep(1000)
        display.show("Pizza")
        sleep(1000)
        display.clear()
        sleep(1000)

----

.. admonition:: Try it

    #. Show "My name" then your name.
    #. Show "I like" then your favourite food.
    #. Show "I am" then your age.

----

Challenge
----------------------------------------

Create a short introduction.

Show:

* your name
* your favourite food
* your favourite animal

Pause for **1 second** after each message and clear the screen before the program repeats.

