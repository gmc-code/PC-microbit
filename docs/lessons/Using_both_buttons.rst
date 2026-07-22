====================================================
Using Both Buttons
====================================================

Your program can check **both** buttons.

It can make **three choices**:

* Button **A**
* Button **B**
* Neither button

----

Three choices
-------------

.. code-block:: python

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show(Image.HAPPY)

        elif button_b.is_pressed():
            display.show(Image.SAD)

        else:
            display.show(Image.CONFUSED)

Press **A** for a happy face.

Press **B** for a sad face.

If no button is pressed, a confused face is shown.

----

Remember

* ``if`` checks the first choice.
* ``elif`` checks another choice.
* ``else`` runs if none of the other choices are true.

----

Try it!

#. Button **A** shows a **HEART**, button **B** shows a **SMILE**, otherwise show a **SAD** face.
#. Button **A** shows a **GIRAFFE**, button **B** shows a **RABBIT**, otherwise show a **DUCK**.
#. Button **A** scrolls your name, button **B** scrolls your age, otherwise show a **HEART**.

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

                    else:
                        display.show(Image.SAD)

        .. tab-item:: Question 2

            .. code-block:: python

                from microbit import *

                while True:
                    if button_a.is_pressed():
                        display.show(Image.GIRAFFE)

                    elif button_b.is_pressed():
                        display.show(Image.RABBIT)

                    else:
                        display.show(Image.DUCK)

        .. tab-item:: Question 3

            .. code-block:: python

                from microbit import *

                while True:
                    if button_a.is_pressed():
                        display.scroll("Sam")

                    elif button_b.is_pressed():
                        display.scroll("12")

                    else:
                        display.show(Image.HEART)

----

Challenge
---------

Write your own program.

Choose something different for:

* Button **A**
* Button **B**
* No button pressed

Ideas:

* Three different animals.
* Three different faces.
* Two words and one picture.
* A smile, a heart and a house.

Example

.. code-block:: python

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show(Image.HOUSE)

        elif button_b.is_pressed():
            display.show(Image.HEART)

        else:
            display.show(Image.SMILE)



