====================================================
Show text
====================================================

What is ``display.show()``?
----------------------------------------

``display.show()`` shows letters or numbers on the micro:bit screen.

Unlike ``display.scroll()``, the letters do **not** move across the screen.

Each letter or number is shown one at a time.

You can show:

* text (words)
* whole numbers
* decimal numbers

Example: Show text
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from microbit import *

    while True:
        display.show("Hi")

Example: Show a number
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from microbit import *

    while True:
        display.show(12)

Example: Show a decimal number
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from microbit import *

    while True:
        display.show(3.5)

----

.. admonition:: Try it

    #. Change the text to your name.
    #. Change the number to your age.
    #. Show the word "Hello".
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

            .. tab-item:: Age

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show(11)

            .. tab-item:: Hello

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show("Hello")

            .. tab-item:: Favourite number

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show(8)

----

Clear the screen
----------------------------------------

The last letter or number stays on the screen.

Use ``display.clear()`` to make the screen blank.

Example:

.. code-block:: python

    from microbit import *

    while True:
        display.show("Hi")
        display.clear()
        sleep(1000)

The ``sleep(1000)`` keeps the screen blank for 1 second.

----

.. admonition:: Try it

    #. Show "ABC", then clear the screen.
    #. Show your age, then clear the screen.
    #. Show your favourite number, then clear the screen.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: ABC

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show("ABC")
                        display.clear()
                        sleep(1000)

            .. tab-item:: Age

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show(11)
                        display.clear()
                        sleep(1000)

----

Using ``clear=True``
----------------------------------------

Instead of writing ``display.clear()``, you can use ``clear=True``.

The micro:bit clears the screen automatically after showing the text.

Example:

.. code-block:: python

    from microbit import *

    while True:
        display.show("Hi", clear=True)
        sleep(1000)

Another example:

.. code-block:: python

    from microbit import *

    while True:
        display.show(123, clear=True)
        sleep(1000)

----

.. admonition:: Try it

    #. Show your name using ``clear=True``.
    #. Show your age using ``clear=True``.
    #. Change the sleep time to 2 seconds.

----

Show faster or slower
----------------------------------------

You can change how long each letter stays on the screen.

A **small** delay number is **faster**.

A **large** delay number is **slower**.

Fast example

.. code-block:: python

    from microbit import *

    while True:
        display.show("Hello", delay=150, clear=True)
        sleep(1000)

Slow example

.. code-block:: python

    from microbit import *

    while True:
        display.show("Hello", delay=500, clear=True)
        sleep(1000)

----

.. admonition:: Try it

    #. Make your name show quickly.
    #. Make your name show slowly.
    #. Try a delay of 200.
    #. Try a delay of 600.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Fast

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show("Sam", delay=150, clear=True)
                        sleep(1000)

            .. tab-item:: Slow

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show("Sam", delay=500, clear=True)
                        sleep(1000)

----

Show two messages
----------------------------------------

You can show more than one message.

The first message finishes before the next one starts.

.. code-block:: python

    from microbit import *

    while True:
        display.show("My name is")
        display.show("Sam")
        display.clear()
        sleep(1000)

Another example:

.. code-block:: python

    from microbit import *

    while True:
        display.show("I like")
        display.show("Pizza")
        display.clear()
        sleep(1000)

----

.. admonition:: Try it

    #. Show "My name is" and then your name.
    #. Show "I like" and then your favourite food.
    #. Show "I am" and then your age.

----

Using variables
----------------------------------------

A **variable** stores information.

Instead of writing the same value many times, you can save it in a variable.

Example:

.. code-block:: python

    from microbit import *

    name = "Sam"

    while True:
        display.show(name)
        display.clear()
        sleep(1000)

Numbers can also be stored in variables.

.. code-block:: python

    from microbit import *

    age = 11

    while True:
        display.show(age)
        display.clear()
        sleep(1000)

You can use more than one variable.

.. code-block:: python

    from microbit import *

    name = "Sam"
    age = 11

    while True:
        display.show("Name")
        display.show(name)

        display.show("Age")
        display.show(age)

        display.clear()
        sleep(1000)

----

.. admonition:: Try it

    #. Change the name variable to your own name.
    #. Change the age variable to your age.
    #. Add a variable called ``colour``.
    #. Display your favourite colour.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Solution

                .. code-block:: python

                    from microbit import *

                    name = "Sam"
                    age = 11
                    colour = "Blue"

                    while True:
                        display.show("Name")
                        display.show(name)

                        display.show("Age")
                        display.show(age)

                        display.show("Colour")
                        display.show(colour)

                        display.clear()
                        sleep(1000)

----

Challenge
----------------------------------------

Can you make your micro:bit show:

1. Your name
2. Your age
3. Your favourite colour

Can you make one message show quickly and another show slowly?