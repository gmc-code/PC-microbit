==========================
Piezo_Buzzer_2
==========================

Playing Built-in Tunes
==========================

In this lesson you will learn how to:

* Play built-in tunes.
* Use the A and B buttons.
* Choose different tunes.
* Use a list to play several tunes.

----

Built-in tunes
----------------------------------------

The ``music`` library already contains lots of tunes.

Instead of writing your own notes,

you can play a built-in tune.

For example:

``music.NYAN``

or

``music.ENTERTAINER``

----

Play one built-in tune
----------------------------------------

Press:

* **Button A** → Play the tune.

.. code-block:: python

    from microbit import *
    import music

    speaker.off()

    while True:

        if button_a.is_pressed():

            music.play(music.NYAN)

        sleep(200)

----

Try another tune
----------------------------------------

Change:

``music.NYAN``

to one of these:

* ``music.ENTERTAINER``
* ``music.PRELUDE``
* ``music.ODE``
* ``music.BIRTHDAY``
* ``music.FUNERAL``
* ``music.WEDDING``

Which tune is your favourite?

----

Using both buttons
----------------------------------------

Press:

* **Button A** → Nyan
* **Button B** → Birthday

.. code-block:: python

    from microbit import *
    import music

    speaker.off()

    while True:

        if button_a.is_pressed():

            music.play(music.NYAN)

        elif button_b.is_pressed():

            music.play(music.BIRTHDAY)

        sleep(200)

----

Worked Example
----------------------------------------

This program lets each button play a different tune.

Can you see what changed?

.. code-block:: python

    from microbit import *
    import music

    speaker.off()

    while True:

        if button_a.is_pressed():

            music.play(music.ODE)

        elif button_b.is_pressed():

            music.play(music.WEDDING)

        sleep(200)

----

Playing lots of tunes
----------------------------------------

We can store tunes in a list.

Then we can play them one after another.

.. code-block:: python

    from microbit import *
    import music

    speaker.off()

    tunes = [
        music.NYAN,
        music.BIRTHDAY,
        music.ODE
    ]

    while True:

        if button_a.is_pressed():

            for tune in tunes:

                music.play(tune)

        sleep(200)

----

Worked Example
----------------------------------------

This program plays four tunes.

.. code-block:: python

    from microbit import *
    import music

    speaker.off()

    tunes = [
        music.PRELUDE,
        music.NYAN,
        music.ENTERTAINER,
        music.WEDDING
    ]

    while True:

        if button_a.is_pressed():

            for tune in tunes:

                music.play(tune)

        sleep(200)

----

Try These
----------------------------------------

**Example 1**

Change the program to play:

* Birthday
* Wedding

----

**Example 2**

Change the list so it has:

* Three tunes.

----

**Example 3**

Change the list so it has:

* Four tunes.

----

**Example 4**

Can you put your favourite tune first?

----

**Example 5**

Can you make Button A play:

* Nyan
* Birthday

and Button B play:

* Ode
* Wedding

----

.. dropdown:: Challenge Solutions
    :icon: codescan
    :color: primary
    :class-container: sd-dropdown-container

    .. tab-set::

        .. tab-item:: Example 1

            .. code-block:: python

                from microbit import *
                import music

                speaker.off()

                tunes = [
                    music.BIRTHDAY,
                    music.WEDDING
                ]

                while True:

                    if button_a.is_pressed():

                        for tune in tunes:

                            music.play(tune)

                    sleep(200)

        .. tab-item:: Example 5

            .. code-block:: python

                from microbit import *
                import music

                speaker.off()

                tunes_a = [
                    music.NYAN,
                    music.BIRTHDAY
                ]

                tunes_b = [
                    music.ODE,
                    music.WEDDING
                ]

                while True:

                    if button_a.is_pressed():

                        for tune in tunes_a:

                            music.play(tune)

                    elif button_b.is_pressed():

                        for tune in tunes_b:

                            music.play(tune)

                    sleep(200)

----

Challenge
----------------------------------------

Create your own concert!

Choose four built-in tunes.

Play them one after another when you press **Button A**.

----

Lesson Review
----------------------------------------

Before moving to the next lesson, check that you can do these things.

.. admonition:: ✔ Lesson Checklist

    Can you:

    ☐ Use a built-in tune such as ``music.NYAN``.

    ☐ Change one built-in tune to another.

    ☐ Use Button A to play a tune.

    ☐ Use both A and B buttons to play different tunes.

    ☐ Store tunes in a list.

    ☐ Use a ``for`` loop to play several tunes.

    ☐ Change a program to play your favourite tunes.