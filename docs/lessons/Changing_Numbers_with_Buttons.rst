====================================================
Changing Numbers with Buttons
====================================================

The buttons can change the value of a variable.

* Press **A** to make the number bigger.
* Press **B** to make the number smaller.

----

Increase a number
-----------------

.. code-block:: python

    from microbit import *

    number = 5

    while True:
        if button_a.was_pressed():
            number = number + 1

        display.show(number)

The number starts at **5**.

Each time you press **A**, the number gets **1 bigger**.

----

Try it!

#. Start at **1**.
#. Start at **9**.
#. Change the number by **2** each time.

.. dropdown::
    :icon: codescan
    :color: primary
    :class-container: sd-dropdown-container

    .. tab-set::

        .. tab-item:: Question 1

            .. code-block:: python

                from microbit import *

                number = 1

                while True:
                    if button_a.was_pressed():
                        number = number + 1

                    display.show(number)

        .. tab-item:: Question 2

            .. code-block:: python

                from microbit import *

                number = 9

                while True:
                    if button_a.was_pressed():
                        number = number + 1

                    display.show(number)

        .. tab-item:: Question 3

            .. code-block:: python

                from microbit import *

                number = 5

                while True:
                    if button_a.was_pressed():
                        number = number + 2

                    display.show(number)

----

Increase and decrease
----------------------

You can use **both** buttons.

.. code-block:: python

    from microbit import *

    number = 5

    while True:

        if button_a.was_pressed():
            number = number + 1

        elif button_b.was_pressed():
            number = number - 1

        display.show(number)

Press **A** to count up.

Press **B** to count down.

----

Try it!

#. Start at **3**.
#. Change the number by **2** each time.
#. Start at **0**.

.. dropdown::
    :icon: codescan
    :color: primary
    :class-container: sd-dropdown-container

    .. tab-set::

        .. tab-item:: Question 1

            .. code-block:: python

                from microbit import *

                number = 3

                while True:

                    if button_a.was_pressed():
                        number = number + 1

                    elif button_b.was_pressed():
                        number = number - 1

                    display.show(number)

        .. tab-item:: Question 2

            .. code-block:: python

                from microbit import *

                number = 5

                while True:

                    if button_a.was_pressed():
                        number = number + 2

                    elif button_b.was_pressed():
                        number = number - 2

                    display.show(number)

        .. tab-item:: Question 3

            .. code-block:: python

                from microbit import *

                number = 0

                while True:

                    if button_a.was_pressed():
                        number = number + 1

                    elif button_b.was_pressed():
                        number = number - 1

                    display.show(number)

----

Challenge
---------

Can you make a simple counter?

* Start at **0**.
* Press **A** to count up.
* Press **B** to count down.

Try to count from **0** to **9**.

