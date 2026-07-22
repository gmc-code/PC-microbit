====================================================
Microbit library
====================================================

Import the microbit library
----------------------------------------

Every micro:bit program starts the same way.

The first line tells Python to use the micro:bit library.

Always begin your program with:

.. code-block:: python

    from microbit import *

This gives your program access to the micro:bit's buttons, display, sensors and other features.

----

.. admonition:: Try it

    Which line is written correctly?

    #. ``from microbit import *``
    #. ``from microbit import``
    #. ``from microbot import *``
    #. ``from microbit *``

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                ✔ Correct!

                .. code-block:: python

                    from microbit import *

            .. tab-item:: Q2

                Missing the ``*``.

                .. code-block:: python

                    from microbit import *

            .. tab-item:: Q3

                ``microbit`` is spelt incorrectly.

                .. code-block:: python

                    from microbit import *

            .. tab-item:: Q4

                Missing the word ``import``.

                .. code-block:: python

                    from microbit import *

----

Blank lines
----------------------------------------

A blank line makes your code easier to read.

Leave **one blank line** after the import line.

Good example:

.. code-block:: python

    from microbit import *

    while True:
        display.show("Hi")

Another good example:

.. code-block:: python

    from microbit import *

    age = 11

    while True:
        display.show(age)

----

.. admonition:: Try it

    #. Find the extra blank line.
    #. Find the missing blank line.

    .. code-block:: python

        from microbit import *


        while True:
            display.show("Hi")

    .. code-block:: python

        from microbit import *
        number = 7

        while True:
            display.show(number)

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Remove the extra blank line.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show("Hi")

            .. tab-item:: Q2

                Add one blank line after the import.

                .. code-block:: python

                    from microbit import *

                    number = 7

                    while True:
                        display.show(number)

----

Why do we use ``from microbit import *``?
----------------------------------------

There are different ways to import a library.

For beginners we use:

.. code-block:: python

    from microbit import *

This lets us write short code like:

.. code-block:: python

    display.show("Hi")

Instead of:

.. code-block:: python

    microbit.display.show("Hi")

The shorter version is easier to read and type.

----

Remember
----------------------------------------

Every micro:bit program should:

1. Start with ``from microbit import *``.
2. Leave one blank line.
3. Then write the rest of your code.

Example:

.. code-block:: python

    from microbit import *

    while True:
        display.show("Hello")

----

Challenge
----------------------------------------

Can you write a program that:

1. Starts with the correct import line.
2. Leaves one blank line.
3. Shows your name on the micro:bit screen.