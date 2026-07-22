====================================================
Buttons
====================================================

The micro:bit has two buttons.

* Button A
* Button B

You can make your program do something when a button is pressed.

----

Button A
---------

Use ``button_a.is_pressed()`` to check if button A is being pressed.

.. code-block:: python

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show(Image.HAPPY)

Press button **A** to see the happy face.

----

Try it!

#. Show a smile.
#. Show a giraffe.
#. Scroll your name.

.. dropdown::
    :icon: codescan
    :color: primary
    :class-container: sd-dropdown-container

    .. tab-set::

        .. tab-item:: Question 1

            .. code-block:: python

                from microbit import *

                while True:
                    if button_a.is_pressed():
                        display.show(Image.SMILE)

        .. tab-item:: Question 2

            .. code-block:: python

                from microbit import *

                while True:
                    if button_a.is_pressed():
                        display.show(Image.GIRAFFE)

        .. tab-item:: Question 3

            .. code-block:: python

                from microbit import *

                while True:
                    if button_a.is_pressed():
                        display.scroll("Sam")

----

Button B
---------

Button B works the same way.

.. code-block:: python

    from microbit import *

    while True:
        if button_b.is_pressed():
            display.show(Image.SAD)

----

Try it!

#. Show a heart.
#. Show your favourite animal.
#. Scroll your age.
