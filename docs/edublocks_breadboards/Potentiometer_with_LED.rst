==========================
Potentiometer_with_LED
==========================

Building the circuit
----------------------------------------

.. image:: images/potentiometer_1_bb.png
    :scale: 50 %

.. image:: images/potentiometer_2_bb.png
    :scale: 50 %

.. image:: images/potentiometer_2.jpg
    :scale: 30 %

----

Controlling LED brightness
----------------------------------------

.. image:: images_edublocks/potentiometer_write.png
    :scale: 20 %

----

Think about it
----------------------------------------

Can you answer these questions?

* When is the LED brightest?
* When is the LED dimmest?
* What happens when the potentiometer is in the middle?

----

Challenge 1
----------------------------------------

* Add a second LED. Connect it to **pin1**.


.. image:: images_edublocks/potentiometer_write2.png
    :scale: 20 %

----

Challenge 2
----------------------------------------

| Make the LEDs have **opposite brightness**.

| Hint: use ``1023 - pot_val``

.. image:: images_edublocks/potentiometer_write2_reverse.png
    :scale: 20 %


----

Challenge 3
----------------------------------------

| If the value is: **500 or more**

    * Yellow LED turns ON.
    * Red LED turns OFF.

| Otherwise:

    * Red LED turns ON.
    * Yellow LED turns OFF.


.. image:: images_edublocks/potentiometer_write2_condition.png
    :scale: 20 %




