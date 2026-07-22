====================================================
Making Choices
====================================================

Your program can make different choices.

It uses:

* ``if``
* ``else``
* ``elif``

----

if ... else
------------

``if`` checks a condition.

``else`` runs when the condition is **not** true.

Example

.. code-block:: python

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show(Image.HAPPY)
        else:
            display.show(Image.SAD)

Press **A** to see the happy face.

When button **A** is not pressed, the sad face is shown.

----

Try it!

#. Show a **SMILE** instead of a sad face.
#. Scroll your name when button **A** is pressed and show a **HEART** when it is not.
#. Show a **GIRAFFE** when button **A** is pressed and a **DUCK** when it is not.

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
                        display.show(Image.HAPPY)
                    else:
                        display.show(Image.SMILE)

        .. tab-item:: Question 2

            .. code-block:: python

                from microbit import *

                while True:
                    if button_a.is_pressed():
                        display.scroll("Sam")
                    else:
                        display.show(Image.HEART)

        .. tab-item:: Question 3

            .. code-block:: python

                from microbit import *

                while True:
                    if button_a.is_pressed():
                        display.show(Image.GIRAFFE)
                    else:
                        display.show(Image.DUCK)

----

if ... elif
------------

``elif`` means **otherwise, check this**.

Example

.. code-block:: python

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show(Image.HAPPY)
        elif button_b.is_pressed():
            display.show(Image.SAD)

Press **A** for a happy face.

Press **B** for a sad face.

----

Try it!

#. Button **A** shows a **HEART**. Button **B** shows a **SMILE**.
#. Button **A** scrolls your name. Button **B** scrolls your age.
#. Button **A** shows a **GIRAFFE**. Button **B** shows a **RABBIT**.

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
                        display.show(Image.HEART)
                    elif button_b.is_pressed():
                        display.show(Image.SMILE)

        .. tab-item:: Question 2

            .. code-block:: python

                from microbit import *

                while True:
                    if button_a.is_pressed():
                        display.scroll("Sam")
                    elif button_b.is_pressed():
                        display.scroll("12")

        .. tab-item:: Question 3

            .. code-block:: python

                from microbit import *

                while True:
                    if button_a.is_pressed():
                        display.show(Image.GIRAFFE)
                    elif button_b.is_pressed():
                        display.show(Image.RABBIT)

----

Challenge
---------

Write your own program.

* Button **A** does one thing.
* Button **B** does something different.

Ideas:

* Show two different animals.
* Show two different faces.
* Scroll two different words.

