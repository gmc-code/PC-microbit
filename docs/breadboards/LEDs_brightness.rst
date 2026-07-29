==========================
LEDs brightness
==========================

In the last lesson we used:

| ``write_digital(1)`` command to turn an LED ON.
| ``write_digital(0)`` command to turn an LED OFF.


Now we will use: ``write_analog()`` to control the **brightness** of an LED.

----

Write analog
----------------------------------------

| Use the ``write_analog(1023)`` command to turn an LED ON.
| Use the ``write_analog(0)`` command to turn an LED OFF.

| The value in ``write_analog()`` can be from **0 to 1023**.
| The bigger the number: **the brighter the LED becomes**

| For example:
| Turn on the LED connected to pin0:
| ``pin0.write_analog(1023)``

| Turn off the LED connected to pin0:
| ``pin0.write_analog(0)``


Brightness examples:

* ``pin0.write_analog(0)`` → LED is OFF
* ``pin0.write_analog(256)`` → very dim
* ``pin0.write_analog(512)`` → about half brightness
* ``pin0.write_analog(768)`` → about three-quarter brightness
* ``pin0.write_analog(1023)`` → full brightness

----

Changing red LED brightness
----------------------------------------

| This program changes the brightness of the red LED.
| Press: **Button A**
| The LED will:

1. Turn on dimly.
2. Get brighter.
3. Become fully bright.
4. Turn off.


.. code-block:: python

    from microbit import *

    while True:
        if button_a.is_pressed():
            pin0.write_analog(256)
            sleep(500)

            pin0.write_analog(512)
            sleep(500)

            pin0.write_analog(768)
            sleep(500)

            pin0.write_analog(1023)
            sleep(500)

            pin0.write_analog(0)
            sleep(500)

        sleep(500)


----

Try These
----------------------------------------

Remember:

* Red LED → pin0
* Yellow LED → pin1
* Green LED → pin2


**Challenge 1**

Press **A**:

* Turn all three LEDs on.
* Set them to half brightness.


Press **B**:

* Turn all LEDs off.

----

**Challenge 2**

Press **A**:

Set the LEDs to:

* Red → half brightness
* Yellow → three-quarter brightness
* Green → full brightness


Press **B**:

* Turn all LEDs off.

----

Using a list of brightness values
----------------------------------------

A **list** stores many values together.

Example:

``brightness_list = [0, 256, 512, 768, 1023]``


This list stores five brightness levels:

* 0 → Off
* 256 → Dim
* 512 → Half bright
* 768 → Three-quarter bright
* 1023 → Full bright

| A **for-loop** can go through each value in the list.
| Fix the indenting in the code below to do this:
| Press **Button A** → Red LED slowly gets brighter.


.. ordering::
    :no-padding:
    :no-reorder:
    :show-code:

    from microbit import *

    brightness_list = [0, 256, 512, 768, 1023]
    sleep_time = 250

    while True:
        if button_a.is_pressed():
            for i in brightness_list:
                pin0.write_analog(i)
                sleep(sleep_time)

        sleep(500)


----

Making an LED dimmer
----------------------------------------

| This program uses the list in reverse.
| Fix the indenting in the code below to do this:
| Press **Button A** → Red LED slowly gets darker.


.. ordering::
    :no-padding:
    :no-reorder:
    :show-code:

    from microbit import *

    brightness_list = [1023, 768, 512, 256, 0]
    sleep_time = 250

    while True:
        if button_b.is_pressed():
            for i in brightness_list:
                pin0.write_analog(i)
                sleep(sleep_time)
        sleep(500)


----

Try These
----------------------------------------

**Challenge 1**

Change the program so:

* All three LEDs get brighter together.

----

**Challenge 2**

Change the program so:

* All three LEDs get dimmer together.

