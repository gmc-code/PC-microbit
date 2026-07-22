====================================================
Scroll text
====================================================

What is ``display.scroll()``?
----------------------------------------

``display.scroll()`` makes words or numbers move across the micro:bit screen.

You can scroll:

* text (words)
* whole numbers
* decimal numbers

Example: Scroll text
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from microbit import *

    while True:
        display.scroll("Hi")

Example: Scroll a number
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from microbit import *

    while True:
        display.scroll(7)

Example: Scroll a decimal number
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from microbit import *

    while True:
        display.scroll(3.5)

----

.. admonition:: Try it

    #. Change the message to your name.
    #. Change the number to your age.
    #. Change the message to "Hello".
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

            .. tab-item:: Age

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll(11)

            .. tab-item:: Hello

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll("Hello")

            .. tab-item:: Favourite number

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll(8)

----

Scroll faster or slower
----------------------------------------

You can change how fast the message moves.

A **small** delay number scrolls **faster**.

A **large** delay number scrolls **slower**.

Fast scroll
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from microbit import *

    while True:
        display.scroll("Fast", delay=60)

Slow scroll
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from microbit import *

    while True:
        display.scroll("Slow", delay=250)

----

.. admonition:: Try it

    #. Make your name scroll quickly.
    #. Make your name scroll slowly.
    #. Try a delay of 100.
    #. Try a delay of 300.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Fast

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll("Sam", delay=60)

            .. tab-item:: Slow

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll("Sam", delay=300)

----

Show two messages
----------------------------------------

You can scroll more than one message.

The computer shows one message, then the next.

.. code-block:: python

    from microbit import *

    while True:
        display.scroll("My name is")
        display.scroll("Sam")

Another example:

.. code-block:: python

    from microbit import *

    while True:
        display.scroll("I like")
        display.scroll("Soccer")

----

.. admonition:: Try it

    #. Show "My name is" and then your name.
    #. Show "I like" and then your favourite food.
    #. Show "I am" and then your age.

----

Using variables
----------------------------------------

A **variable** stores information.

Instead of writing the word every time, we can save it in a variable.

Example:

.. code-block:: python

    from microbit import *

    name = "Sam"

    while True:
        display.scroll(name)

Numbers can also be stored in variables.

.. code-block:: python

    from microbit import *

    age = 11

    while True:
        display.scroll(age)

You can use more than one variable.

.. code-block:: python

    from microbit import *

    name = "Sam"
    age = 11

    while True:
        display.scroll("Name")
        display.scroll(name)

        display.scroll("Age")
        display.scroll(age)

----

.. admonition:: Try it

    #. Change the name variable to your own name.
    #. Change the age variable to your age.
    #. Add a new variable called ``colour`` and store your favourite colour.
    #. Display the colour on the screen.

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
                        display.scroll("Name")
                        display.scroll(name)

                        display.scroll("Age")
                        display.scroll(age)

                        display.scroll("Colour")
                        display.scroll(colour)

----

Challenge
----------------------------------------

Can you make your micro:bit show:

1. Your name
2. Your age
3. Your favourite colour

Can you make some messages scroll fast and others scroll slowly?