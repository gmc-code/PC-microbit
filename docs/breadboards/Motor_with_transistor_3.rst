==========================
Motor_with_transistor_3
==========================

Motor Speed Patterns
==========================

In this lesson you will learn how to:

* Find the speed where a motor starts moving.
* Use variables to control motor power.
* Create motor speed patterns.
* Use lists and loops to control a motor.


----

Finding the motor starting speed
----------------------------------------

Different motors need different amounts of power.

Some motors start moving with a small value.

Other motors need a larger value.

We can test different power values to find the smallest value that makes the motor move.


----

Testing motor power
----------------------------------------

This program:

* Starts with a chosen speed.
* Slowly increases the speed.
* Shows the speed value on the micro:bit display.
* Tests different power levels.


.. code-block:: python

    from microbit import *


    power_level_start = 150
    power_step = 5

    while True:
        if button_a.is_pressed():
            for power_rep in range(20):
                power = power_level_start + power_step * power_rep
                display.scroll(power)
                pin0.write_analog(power)
                sleep(1000)

                pin0.write_analog(0)
                sleep(500)

        sleep(500)


----

Understanding the program
----------------------------------------

The program uses **variables**.

A variable stores a value that we can use later.


Example:


``power_level_start = 150``


This stores the first motor speed.


----

Starting speed
----------------------------------------

``power_level_start``

is the first speed the motor tries.


Example:


``power_level_start = 150``


The motor starts testing at speed 150.


----

Speed increase
----------------------------------------

``power_step``

controls how much the speed increases each time.


Example:


``power_step = 5``


The motor speed increases by 5 each step.


----

The counter
----------------------------------------

``power_rep``

counts how many times the loop repeats.


The speed is calculated using:


``power = power_level_start + power_step * power_rep``


Example:

Starting speed:

``150``


The motor tries:

* 150
* 155
* 160
* 165
* 170


The speed continues increasing.


----

Finding your motor starting speed
----------------------------------------

Try changing:


``power_level_start``


Test different values:

* 100
* 120
* 170


Think about:

* Does the motor start moving?
* Is the value too low?
* Is the value too high?


Find the smallest number that starts your motor.


----

Challenge 1
----------------------------------------

Change the program so:

* It starts at speed 100.
* It increases by 10.
* It tests 15 steps.


.. dropdown:: Challenge 1 Solution
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. code-block:: python

            from microbit import *


            power_level_start = 100
            power_step = 10


            while True:

                if button_a.is_pressed():
                    for power_rep in range(15):
                        power = power_level_start + power_step * power_rep
                        display.scroll(power)
                        pin0.write_analog(power)
                        sleep(1000)

                        pin0.write_analog(0)
                        sleep(500)

                sleep(500)


----

Creating motor speed patterns
----------------------------------------

A motor does not have to stay at one speed.

We can create patterns by changing the speed.


Example:


``Slow → Fast → Slow``


A list can store the speed pattern.


Example:


``speed_pattern = [150, 250, 350, 1023, 350, 250]``


The motor follows each value in order.


----

Motor speed wave
----------------------------------------

This program creates a speed wave.


.. code-block:: python

    from microbit import *


    speed_pattern = [100, 300, 600, 1023, 600, 300]

    while True:
        if button_a.is_pressed():
            for speed in speed_pattern:
                pin0.write_analog(speed)
                sleep(500)

        sleep(500)


----

Understanding the speed pattern
----------------------------------------

The list:


``speed_pattern = [100, 300, 600, 1023, 600, 300]``


creates this pattern:


* 100 → Slow
* 300 → Faster
* 600 → Fast
* 1023 → Full speed
* 600 → Slowing down
* 300 → Slower


The pattern repeats.


----

Challenge 2
----------------------------------------

Create your own motor speed pattern.


Your program must:

* Use a list.
* Have at least 5 speed values.
* Use a for-loop.
* Use ``write_analog()``.


Ideas:

Create:

* A heartbeat pattern.
* A warning signal.
* A pulsing motor.
* A wave pattern.


----

Final Challenge
----------------------------------------

Create a motor controller.


Button A:

* Slowly increase the motor speed.


Button B:

* Slowly decrease the motor speed.


Nothing pressed:

* Stop the motor.


Hint:

Use:

* A variable to store speed.
* ``write_analog()``.
* ``if`` statements.
* A loop.


----

Lesson Review
----------------------------------------

Before moving on, check that you can do these things.

.. admonition:: ✔ Lesson Checklist

    Can you:

    ☐ Change the starting power of a motor by editing a variable.

    ☐ Change the size of each speed step.

    ☐ Create a list of motor speed values.

    ☐ Change a program to test different motor speeds.

    ☐ Design your own motor speed pattern.