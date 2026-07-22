==========================
Potentiometer
==========================

Reading a Potentiometer
==========================

In this lesson you will learn how to:

* Connect a potentiometer.
* Read its value.
* Display the value on the micro:bit.
* Scale the value to a smaller range.

----

What is a potentiometer?
----------------------------------------

A **potentiometer** is a variable resistor.

It is sometimes called a **pot**.

You can turn the knob to change its value.

As you turn it:

* The reading changes.
* The micro:bit can measure the change.

You can use a potentiometer to control things such as:

* Motor speed
* LED brightness
* Sound volume


----

Build the circuit
----------------------------------------

Follow these steps:

#. Place the potentiometer.
#. Connect the jumper wires.


.. image:: images/potentiometer1_bb.png
    :scale: 50 %

.. image:: images/potentiometer_1.jpg
    :scale: 30 %

----

Reading the potentiometer
----------------------------------------

To read the potentiometer we use:

``pin2.read_analog()``

The value can be between:

* ``0`` (one end)
* ``1023`` (the other end)

Turn the knob slowly.

Watch the numbers change.

.. code-block:: python

    from microbit import *

    while True:
        pot_val = pin2.read_analog()
        display.scroll(pot_val, delay=80)
        sleep(20)

----

Think about it
----------------------------------------

Try turning the knob.

Can you answer these questions?

* What is the smallest number you can see?
* What is the largest number you can see?
* Do the numbers increase or decrease as you turn the knob?

----

Scaling the value
----------------------------------------

Sometimes we do not need numbers from:

``0`` to ``1023``

It is easier to work with smaller numbers.

For example:

``0`` to ``9``

The micro:bit has a function called:

``scale()``

It changes a value from one range into another range.

Example:

* ``0`` becomes ``0``
* ``1023`` becomes ``9``

Everything in between is changed to a matching value.

----

Using scale()
----------------------------------------

.. py:function:: scale(value, from_, to)

    Converts a value from one range into another range.

    Example:

    ``scale(512, from_=(0,1023), to=(0,9))``

----

Scaling the potentiometer
----------------------------------------

This program:

* Reads the potentiometer.
* Changes the value to a number between 0 and 9.
* Displays the new value.

.. code-block:: python

    from microbit import *

    while True:
        pot_val = pin2.read_analog()

        scaled_pot_val = scale(
            pot_val,
            from_=(0.0, 1023.0),
            to=(0, 9)
        )

        display.scroll(scaled_pot_val, delay=80)
        sleep(20)

----

Try These
----------------------------------------

**Challenge 1**

Run the program.

Turn the potentiometer.

Can you make it display:

* 0
* 3
* 5
* 9

----

**Challenge 2**

Change the program so it scales the value from:

* ``0`` to ``5``

instead of:

* ``0`` to ``9``

What numbers can you make?

----

Extension
----------------------------------------

Power meter
----------------------------------------

The micro:bit LEDs can show the potentiometer value as a bar.

As you turn the knob:

* The bar grows.
* The bar shrinks.

.. image:: images/potentiometer_level.png
    :scale: 50 %
    :align: center

The program below creates a simple power meter.

.. code-block:: python

    from microbit import *

    while True:
        level = pin2.read_analog()
        val = int((level % 200) * 9 / 200)
        # Work out which row to draw
        y_val = max(0, 4 - (level // 50)) if level > 0 else 5
        # Draw the display
        for x in range(5):
            if y_val < 5:
                display.set_pixel(x, y_val, val)
            for y in range(5):
                display.set_pixel(x, y, 9 if y >= y_val else 0)

        sleep(20)

----

Challenge 3
----------------------------------------

Run the power meter program.

Turn the potentiometer slowly.

Can you answer these questions?

* What happens when you turn it clockwise?
* What happens when you turn it anticlockwise?
* Does the display fill up or empty?

----

Lesson Review
----------------------------------------

Before moving to the next lesson, check that you can do these things.

.. admonition:: ✔ Lesson Checklist

    Can you:

    ☐ Explain what a potentiometer is.

    ☐ Use ``read_analog()`` to read a potentiometer value.

    ☐ Explain that ``read_analog()`` returns a value from ``0`` to ``1023``.

    ☐ Use ``scale()`` to change one range of numbers into another.

    ☐ Change a program to display scaled values.

    ☐ Explain how a potentiometer can control another device.

    ☐ Run the power meter program and explain how the LED display changes when the potentiometer is turned.