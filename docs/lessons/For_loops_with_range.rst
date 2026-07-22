====================================================
For Loops with range()
====================================================

The ``range()`` function repeats code a set number of times.

It counts from **0**.

Example

.. code-block:: python

    from microbit import *

    while True:
        for number in range(3):
            display.show(number)
            sleep(500)

This shows:

0

1

2

The loop stops before **3**.

----

Remember

``range(3)`` means:

0, 1, 2

``range(5)`` means:

0, 1, 2, 3, 4

It always stops **before** the number.

----

Try it!

#. Change the loop to show **0 to 4**.
#. Change the loop to show **0 to 6**.
#. Change the loop to show **0 to 9**.

.. dropdown::
    :icon: codescan
    :color: primary
    :class-container: sd-dropdown-container

    .. tab-set::

        .. tab-item:: Question 1

            .. code-block:: python

                from microbit import *

                while True:
                    for number in range(5):
                        display.show(number)
                        sleep(500)

        .. tab-item:: Question 2

            .. code-block:: python

                from microbit import *

                while True:
                    for number in range(7):
                        display.show(number)
                        sleep(500)

        .. tab-item:: Question 3

            .. code-block:: python

                from microbit import *

                while True:
                    for number in range(10):
                        display.show(number)
                        sleep(500)


