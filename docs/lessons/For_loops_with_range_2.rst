====================================================
Changing the Numbers
====================================================

You can change each number before you show it.

----

Count from 1

.. code-block:: python

    from microbit import *

    while True:
        for number in range(5):
            display.show(number + 1)
            sleep(500)

This shows:

1

2

3

4

5

----

Count in twos

.. code-block:: python

    from microbit import *

    while True:
        for number in range(5):
            display.show(number * 2)
            sleep(500)

This shows:

0

2

4

6

8

----

Try it!

#. Show **1 to 3**.
#. Show **0, 3, 6, 9**.
#. Show **5, 6, 7, 8**.

.. dropdown::
    :icon: codescan
    :color: primary
    :class-container: sd-dropdown-container

    .. tab-set::

        .. tab-item:: Question 1

            .. code-block:: python

                from microbit import *

                while True:
                    for number in range(3):
                        display.show(number + 1)
                        sleep(500)

        .. tab-item:: Question 2

            .. code-block:: python

                from microbit import *

                while True:
                    for number in range(4):
                        display.show(number * 3)
                        sleep(500)

        .. tab-item:: Question 3

            .. code-block:: python

                from microbit import *

                while True:
                    for number in range(4):
                        display.show(number + 5)
                        sleep(500)

----

Challenge
---------

Can you make these number patterns?

* 10 11 12 13
* 0 5 10 15
* 2 4 6 8
