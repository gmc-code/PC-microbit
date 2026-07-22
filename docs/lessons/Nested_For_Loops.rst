====================================================
Nested For Loops
====================================================

A **nested loop** is a loop inside another loop.

----

Example

.. code-block:: python

    from microbit import *

    letters = ["A", "B"]
    numbers = ["1", "2", "3"]

    while True:
        for letter in letters:
            for number in numbers:
                display.scroll(letter + number)

The program shows:

A1

A2

A3

B1

B2

B3

----

Try it!

#. Use X and Y instead of A and B.
#. Use the numbers 1 to 5.
#. Use your own letters.

----

Challenge
---------

Can you light every pixel on the micro:bit?

.. code-block:: python

    from microbit import *

    while True:
        for x in [0,1,2,3,4]:
            for y in [0,1,2,3,4]:
                display.set_pixel(x, y, 9)
                sleep(100)
                display.set_pixel(x, y, 0)
