==========================
LEDs_blink
==========================

| In this lesson you will use the previous model with **three LEDs**.
| You will learn how to make LEDs blink **ON** and **OFF** using code.

----

Blinking LEDs
----------------------------------------

Blinking means:

**ON → OFF → ON → OFF**

Try this:

* Button A → LEDs blink one at a time.

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

Try this:

* Button B → All LEDs blink together.

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
Makes the red LED blink **3 times** every 6 seconds.


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

* Blink the red LED **5 times** every 6 seconds.

----

Try this:

* All LEDs blink together **3 times** every 6 seconds.

