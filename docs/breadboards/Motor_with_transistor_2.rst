==========================
Motor_with_transistor_2
==========================

Changing Motor Speed
==========================

In the last lesson you learned how to:

* Turn a motor ON.
* Turn a motor OFF.
* Use buttons to control a motor.

In this lesson you will learn how to:

* Change the speed of a motor.
* Use ``write_analog()``.
* Use lists and loops to control speed.


----

Digital and analog control
----------------------------------------

With ``write_digital()`` the motor has only two choices:

``1``

Motor ON


``0``

Motor OFF


Now we will use:

``write_analog()``


This lets us choose different motor speeds.


----

Write analog
----------------------------------------

.. py:function:: pinx.write_analog(value)
    :no-index:

    | ``pinx`` is the motor pin.
    |
    | Examples:
    |
    | * ``pin0``
    | * ``pin1``
    | * ``pin2``
    |
    | ``value`` controls the motor speed.
    |
    | The value can be from **0 to 1023**.


The number controls the motor speed:


* ``0`` → Motor OFF
* ``250`` → Slow speed
* ``350`` → Medium speed
* ``1023`` → Full speed


Remember:

**Bigger number = faster motor**


----

Changing motor speed
----------------------------------------

This program changes the motor speed.

Press:

**Button A**

The motor will:

1. Stop.
2. Move slowly.
3. Move faster.
4. Move at full speed.


.. code-block:: python

    from microbit import *


    power_levels = [0, 250, 350, 1023]


    while True:
        if button_a.is_pressed():
            for power in power_levels:
                pin0.write_analog(power)
                sleep(1000)

        sleep(500)


----

Understanding the list
----------------------------------------

The program uses this list:


``power_levels = [0, 250, 350, 1023]``


The motor follows these steps:

* ``0`` → Stop
* ``250`` → Slow
* ``350`` → Medium
* ``1023`` → Full speed


A **list** stores many values together.


A **for-loop** moves through each value in the list.


----

Challenge 1
----------------------------------------

Change the program so it has only three speeds:

* Stop → ``0``
* Medium speed → ``350``
* Full speed → ``1023``


.. dropdown:: Challenge 1 Solution
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. code-block:: python

            from microbit import *


            power_levels = [0, 350, 1023]

            while True:
                if button_a.is_pressed():
                    for power in power_levels:
                        pin0.write_analog(power)
                        sleep(1000)

                sleep(500)


----

Challenge 2
----------------------------------------

Change the program so it has three speeds:

* Slow → ``250``
* Medium → ``350``
* Fast → ``1023``


After each speed:

* Stop the motor for 500 milliseconds.


.. dropdown:: Challenge 2 Solution
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. code-block:: python

            from microbit import *

            power_levels = [250, 350, 1023]

            while True:
                if button_a.is_pressed():
                    for power in power_levels:
                        pin0.write_analog(power)
                        sleep(1000)

                        pin0.write_analog(0)
                        sleep(500)

                sleep(500)


----

Using numbers to change speed
----------------------------------------

We can also change motor speed using:

``range()``


A **for-loop** repeats instructions.


This program:

* Starts at speed 100.
* Adds 20 each time.
* Repeats 10 times.


.. code-block:: python

    from microbit import *


    sleep_time = 500
    start_val = 100

    while True:
        if button_a.is_pressed():
            for i in range(10):
                pin0.write_analog(start_val + 20 * i)
                sleep(sleep_time)

        pin0.write_analog(0)
        sleep(1000)


----

Understanding range()
----------------------------------------

``range(10)`` means:

Repeat 10 times.


The variable ``i`` counts:

* 0
* 1
* 2
* 3
* 4
* and so on


The speed changes because we use:


``start_val + 20 * i``


Each time the loop repeats:

The motor speed increases by 20.


----

Challenge 3
----------------------------------------

Change the program so:

* The motor starts at speed 150.
* The speed increases by 50.
* The program uses 5 speed steps.


.. dropdown:: Challenge 3 Solution
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. code-block:: python

            from microbit import *


            sleep_time = 500
            start_val = 150

            while True:
                if button_a.is_pressed():
                    for i in range(6):
                        pin0.write_analog(start_val + 50 * i)
                        sleep(sleep_time)

                pin0.write_analog(0)
                sleep(1000)


----

Challenge 4
----------------------------------------

Change the program so:

* The motor starts at speed 320.
* The speed decreases by 80.
* The program uses 4 steps.


.. dropdown:: Challenge 4 Solution
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. code-block:: python

            from microbit import *


            sleep_time = 500
            start_val = 320

            while True:
                if button_a.is_pressed():
                    for i in range(5):
                        pin0.write_analog(start_val - 80 * i)
                        sleep(sleep_time)

                pin0.write_analog(0)
                sleep(1000)


----

Lesson Review
----------------------------------------

Before moving to the next lesson, check that you can do these things.

.. admonition:: ✔ Lesson Checklist

    Can you:

    ☐ Explain what ``write_analog()`` does.

    ☐ Use ``write_analog()`` to change the speed of a motor.

    ☐ Explain that motor speed values can be from ``0`` to ``1023``.

    ☐ Predict what happens when you use a larger or smaller value.

    ☐ Use a list to store motor speed values.

    ☐ Use a ``for`` loop to repeat instructions.

    ☐ Change ``range()`` to make a program repeat more or fewer times.

    ☐ Change a program to make the motor speed up or slow down.