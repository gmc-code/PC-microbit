==========================
Motor_with_transistor_2
==========================

In the last lesson we used:

| ``write_digital(1)`` command to turn the motor ON.
| ``write_digital(0)`` command to turn the motor OFF.


Now we will use: ``write_analog()`` to control the **speed** of the motor.

----

Write analog
----------------------------------------

| Use the ``write_analog(1023)`` command to turn the motor ON.
| Use the ``write_analog(0)`` command to turn the motor OFF.

| The value in ``write_analog()`` can be from **0 to 1023**.
| The bigger the number: **the faster the motor turns**

| For example:
| Turn on the motor connected to pin0:
| ``pin0.write_analog(1023)``

| Turn off the motor connected to pin0:
| ``pin0.write_analog(0)``


Speed examples:

* ``pin0.write_analog(0)`` → the motor is OFF
* ``pin0.write_analog(250)`` → slow
* ``pin0.write_analog(350)`` → faster
* ``pin0.write_analog(1023)`` → full speed


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

Fix the indenting in the code below:

.. ordering::
    :no-padding:
    :no-reorder:
    :show-code:

    from microbit import *

    power_levels = [0, 250, 350, 1023]

    while True:
        if button_a.is_pressed():
            for power in power_levels:
                pin0.write_analog(power)
                sleep(1000)

        sleep(500)

----

Challenge 1
----------------------------------------

| Fix the indenting in the code below to do this:
| Change the program so it has only three speeds:

* Stop → ``0``
* Medium speed → ``350``
* Full speed → ``1023``


.. ordering::
    :no-padding:
    :no-reorder:
    :show-code:

    from microbit import *

    power_levels = [0, 350, 1023]

    while True:
        if button_a.is_pressed():
            for power in power_levels:
                pin0.write_analog(power)
                sleep(1000)

        sleep(500)


----

Creating motor speed patterns
----------------------------------------

| A motor does not have to stay at one speed.
| We can create patterns by changing the speed.
| A list can store the speed pattern.

Example:

``power_levels = [150, 250, 350, 1023, 350, 250]``

Try out different patterns of power levels.

Try using diffferent motor speed patterns for button A and button B.

