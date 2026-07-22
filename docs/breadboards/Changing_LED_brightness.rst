==========================
Changing LED brightness
==========================

In the last lesson we used:

``write_digital()``

This could only do two things:

* ``1`` = ON
* ``0`` = OFF


Now we will use:

``write_analog()``


This lets us control the **brightness** of an LED.

----

Write analog
----------------------------------------

.. py:function:: pinx.write_analog(value)

    | ``pinx`` is the LED pin.
    |
    | Examples:
    |
    | * ``pin0``
    | * ``pin1``
    | * ``pin2``
    |
    | ``value`` controls the brightness.
    |
    | The value can be from **0 to 1023**.


The bigger the number:

**the brighter the LED becomes**


Brightness examples:

* ``0`` → LED is OFF
* ``256`` → very dim
* ``512`` → about half brightness
* ``768`` → about three-quarter brightness
* ``1023`` → full brightness


Try changing the numbers.

What happens to the LED?


----

Changing red LED brightness
----------------------------------------

This program changes the brightness of the red LED.

Press:

**Button A**

The LED will:

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


**Challenge 2**

Press **A**:

Set the LEDs to:

* Red → half brightness
* Yellow → three-quarter brightness
* Green → full brightness


Press **B**:

* Turn all LEDs off.


.. dropdown:: Challenge Solutions
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Challenge 1 Solution

                .. code-block:: python

                    from microbit import *

                    while True:
                        if button_a.is_pressed():
                            pin0.write_analog(512)
                            pin1.write_analog(512)
                            pin2.write_analog(512)

                        elif button_b.is_pressed():
                            pin0.write_analog(0)
                            pin1.write_analog(0)
                            pin2.write_analog(0)

                        sleep(500)


            .. tab-item:: Challenge 2 Solution

                .. code-block:: python

                    from microbit import *

                    while True:
                        if button_a.is_pressed():
                            pin0.write_analog(512)
                            pin1.write_analog(768)
                            pin2.write_analog(1023)

                        elif button_b.is_pressed():
                            pin0.write_analog(0)
                            pin1.write_analog(0)
                            pin2.write_analog(0)

                        sleep(500)


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


A **for-loop** can go through each value in the list.


The next program makes the red LED slowly get brighter.


.. code-block:: python

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

This program uses the list in reverse .

This time the LED slowly gets darker.


.. code-block:: python

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


**Challenge 2**

Change the program so:

* All three LEDs get dimmer together.


.. dropdown:: Challenge Solutions
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Challenge 1 Solution

                .. code-block:: python

                    from microbit import *

                    brightness_list = [0, 256, 512, 768, 1023]
                    sleep_time = 250

                    while True:
                        if button_a.is_pressed():
                            for i in brightness_list:
                                pin0.write_analog(i)
                                pin1.write_analog(i)
                                pin2.write_analog(i)
                                sleep(sleep_time)
                        sleep(500)


            .. tab-item:: Challenge 2 Solution

                .. code-block:: python

                    from microbit import *

                    brightness_list = [1023, 768, 512, 256, 0]
                    sleep_time = 250

                    while True:

                        if button_b.is_pressed():
                            for i in brightness_list:
                                pin0.write_analog(i)
                                pin1.write_analog(i)
                                pin2.write_analog(i)
                                sleep(sleep_time)

                        sleep(500)
