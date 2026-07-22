====================================================
while True Loops
====================================================

A ``while True:`` loop repeats the same code **again and again**.

It only stops when the micro:bit is turned off or the program is stopped.

Example

.. code-block:: python

    from microbit import *

    while True:
        display.scroll("Hello")

The word **Hello** scrolls across the screen over and over.

Remember

* ``while`` starts with a **lower case** ``w``.
* ``True`` starts with a **capital** ``T``.
* The line must end with a **colon** ``:``.
* The code inside the loop is **indented** (moved in).

----

Another example

.. code-block:: python

    from microbit import *

    while True:
        display.show(Image.HAPPY)
        sleep(1000)
        display.show(Image.SAD)
        sleep(1000)

The micro:bit keeps changing between a happy face and a sad face.

----

.. admonition:: Try it!

    Find and fix the mistake in each loop.

    #. ``while true:``
    #. ``While True:``
    #. ``while True``

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Question 1

                ``True`` needs a capital **T**.

                .. code-block:: python

                    while True:

            .. tab-item:: Question 2

                ``while`` needs a lower case **w**.

                .. code-block:: python

                    while True:

            .. tab-item:: Question 3

                Add the missing colon ``:``.

                .. code-block:: python

                    while True: