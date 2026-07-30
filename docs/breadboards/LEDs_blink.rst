==========================
LEDs blink
==========================

| In this lesson you will use the previous model with **three LEDs**.
| You will learn how to make LEDs blink **ON** and **OFF** using code.

----

Blinking an LED
----------------------------------------

Blinking means:

**ON → OFF → ON → OFF**

| The code below turns the LED connected to pin0 **ON** for 0.25 second, and then **OFF** for 0.25 second, then repeats.

.. cloze::
    :show-code:

    from microbit import *

    while True:
        pin0.write_digital(@@ 1 | 0 @@)
        sleep(250)
        pin0.write_digital(@@ 0 | 1 @@)
        sleep(250)

----

Blinking LEDs: one at a time
----------------------------------------

Try this:

* Button A → LEDs blink one at a time.
* First Red is turned ON then OFF, then the yellow LED and then the green LED.
* Hold down the A button to keep blinking the LEDs.

.. cloze::
    :show-code:

    from microbit import *

    while True:
        if button_a.is_pressed():
            pin0.write_digital(1)
            sleep(500)
            @@pin0@@.write_digital(0)

            pin1.write_digital(1)
            sleep(500)
            @@pin1@@.write_digital(0)

            pin2.write_digital(1)
            sleep(500)
            @@pin2@@.write_digital(0)

        sleep(500)

----

Blinking LEDs: all together
----------------------------------------

Try this:

* Button B → All LEDs blink together.
* All LEDs are turned ON then OFF.
* Hold down the B button to keep blinking the LEDs.

.. cloze::
    :show-code:

    from microbit import *

    while True:

        if button_b.is_pressed():
            pin0.write_digital(@@1@@)
            pin1.write_digital(@@1@@)
            pin2.write_digital(@@1@@)
            sleep(750)

            pin0.write_digital(@@0@@)
            pin1.write_digital(@@0@@)
            pin2.write_digital(@@0@@)
            sleep(750)

----

Try this:

* Button A → LEDs blink one at a time.
* Button B → All LEDs blink together.


----

Using a for-loop
----------------------------------------

| A **for-loop** repeats instructions.
| Instead of writing the same code many times, we can tell Python: "Repeat this."

Fix the indenting in the code below to do this:
Makes the red LED blink **3 times** in 3 seconds followed by a 3 second pause.


.. ordering::
    :no-padding:
    :no-reorder:
    :show-code:

    from microbit import *

    while True:
        for i in range(3):
            pin0.write_digital(1)
            sleep(500)
            pin0.write_digital(0)
            sleep(500)

        sleep(3000)

----

Try this:

* Blink the red LED **5 times** in 5 seconds followed by a 1 second pause.

----

Try this:

* All LEDs blink together **3 times** in 3 seconds followed by a 3 second pause.

