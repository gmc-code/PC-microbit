==========================
Piezo_Buzzer_3
==========================

Changing the Speed of Music
==========================

In this lesson you will learn how to:

* Make music play faster.
* Make music play slower.
* Use ``music.set_tempo()``.
* Experiment with different speeds.

----

What is tempo?
----------------------------------------

**Tempo** means:

**How fast the music plays.**

A slow tempo plays the notes slowly.

A fast tempo plays the notes quickly.

----

Setting the tempo
----------------------------------------

To change the speed, use:

``music.set_tempo()``

The number is called **beats per minute (BPM)**.

Some examples are:

* ``60`` = Slow
* ``120`` = Normal
* ``180`` = Fast

----

Playing a tune slowly
----------------------------------------

This program plays a tune slowly.

.. code-block:: python

    from microbit import *
    import music

    speaker.off()

    music.set_tempo(bpm=60)

    while True:

        if button_a.is_pressed():

            music.play(music.NYAN)

        sleep(200)

----

Playing the same tune faster
----------------------------------------

Now change the tempo.

The tune is exactly the same.

Only the speed changes.

.. code-block:: python

    from microbit import *
    import music

    speaker.off()

    music.set_tempo(bpm=180)

    while True:

        if button_a.is_pressed():

            music.play(music.NYAN)

        sleep(200)

----

Think About It
----------------------------------------

Play both programs.

Can you hear the difference?

Which one is:

* Slow?
* Fast?

Which one do you like best?

----

Using both buttons
----------------------------------------

Press:

* **Button A** → Slow tune.
* **Button B** → Fast tune.

.. code-block:: python

    from microbit import *
    import music

    speaker.off()

    while True:

        if button_a.is_pressed():

            music.set_tempo(bpm=60)

            music.play(music.BIRTHDAY)

        elif button_b.is_pressed():

            music.set_tempo(bpm=180)

            music.play(music.BIRTHDAY)

        sleep(200)

----

Worked Example
----------------------------------------

This program has three speeds.

* Slow
* Medium
* Fast

The same tune is played each time.

.. code-block:: python

    from microbit import *
    import music

    speaker.off()

    tempos = [60, 120, 180]

    while True:

        if button_a.is_pressed():

            for speed in tempos:

                music.set_tempo(bpm=speed)

                music.play(music.NYAN)

        sleep(200)

----

Try These
----------------------------------------

**Example 1**

Change:

``60``

to

``80``

Does it sound faster?

----

**Example 2**

Change:

``180``

to

``200``

Can you hear the difference?

----

**Example 3**

Make a list with:

* 80
* 120
* 160

Run the program.

----

**Example 4**

Make a list with:

* 50
* 100
* 150
* 200

Which speed do you like best?

----

**Example 5**

Change the built-in tune.

Try:

* ``music.WEDDING``
* ``music.ODE``
* ``music.ENTERTAINER``

Which tune changes the most when the tempo changes?

----

Challenge 1
----------------------------------------

Press:

* **Button A** → Play the tune slowly.

* **Button B** → Play the tune quickly.

Use your favourite built-in tune.

----

Challenge 2
----------------------------------------

Create a speed test.

Play the same tune at:

* Slow
* Medium
* Fast

Which speed sounds best?

----

.. dropdown::
    :icon: codescan
    :color: primary
    :class-container: sd-dropdown-container

    .. tab-set::

        .. tab-item:: Challenge 1 Solution

            .. code-block:: python

                from microbit import *
                import music

                speaker.off()

                while True:

                    if button_a.is_pressed():

                        music.set_tempo(bpm=70)

                        music.play(music.WEDDING)

                    elif button_b.is_pressed():

                        music.set_tempo(bpm=190)

                        music.play(music.WEDDING)

                    sleep(200)

        .. tab-item:: Challenge 2 Solution

            .. code-block:: python

                from microbit import *
                import music

                speaker.off()

                tempos = [60, 120, 180]

                while True:

                    if button_a.is_pressed():

                        for speed in tempos:

                            music.set_tempo(bpm=speed)

                            music.play(music.BIRTHDAY)

                    sleep(200)

----

Lesson Review
----------------------------------------

Before moving to the next lesson, check that you can do these things.

.. admonition:: ✔ Lesson Checklist

    Can you:

    ☐ Explain what **tempo** means.

    ☐ Use ``music.set_tempo()`` to change the speed of music.

    ☐ Make music play slower.

    ☐ Make music play faster.

    ☐ Change the BPM value.

    ☐ Use a list to store different tempos.

    ☐ Use a ``for`` loop to play the same tune at different speeds.

    ☐ Choose the best tempo for your favourite tune.