==========================
Piezo_Buzzer_4
==========================

Make Your Own Music
==========================

In this lesson you will learn how to:

* Make your own tunes.
* Play notes for different lengths of time.
* Play high and low notes.
* Create your own music project.

----

Long and short notes
----------------------------------------

A note can be:

* Short
* Long

Add a number after the note.

For example:

* ``C:1`` = short
* ``C:2`` = longer
* ``C:4`` = very long

----

Playing notes with different lengths
----------------------------------------

This program plays some short and long notes.

.. code-block:: python

    from microbit import *
    import music

    speaker.off()
    notes = [
        "c:1",
        "d:1",
        "e:2",
        "g:4"
    ]

    while True:
        if button_a.is_pressed():
            music.play(notes)

        sleep(200)

----

Try These
----------------------------------------

Change the note lengths.

Try:

* ``c:2``
* ``c:4``
* ``g:2``

Which notes last the longest?

----

High and low notes
----------------------------------------

You can also change the pitch.

A higher number gives a higher note.

Examples:

* ``C4`` = lower note
* ``C5`` = middle note
* ``C6`` = higher note

----

Playing high and low notes
----------------------------------------

.. code-block:: python

    from microbit import *
    import music

    speaker.off()
    notes = [
        "c4",
        "c5",
        "c6",
        "c5",
        "c4"
    ]

    while True:
        if button_a.is_pressed():
            music.play(notes)

        sleep(200)

----

Worked Example
----------------------------------------

This tune starts low,

moves higher,

then comes back down.

.. code-block:: python

    from microbit import *
    import music

    speaker.off()
    notes = [
        "c4",
        "d4",
        "e5",
        "g5",
        "e5",
        "d4",
        "c4"
    ]

    while True:
        if button_a.is_pressed():
            music.play(notes)

        sleep(200)

----

Practice 1
----------------------------------------

Change the program.

Make it play:

* C4
* E4
* G4
* C5

----

Practice 2
----------------------------------------

Create a tune using:

* C4
* D4
* E4
* F4
* G4

Use at least six notes.

----

Practice 3
----------------------------------------

Use some short notes and some long notes.

For example:

* ``c:1``
* ``d:2``
* ``e:4``

What changes?

----

Playing a sound effect
----------------------------------------

Instead of music, you can play a sound.

For example:

.. code-block:: python

    from microbit import *
    import music

    speaker.off()

    while True:
        if button_a.is_pressed():
            music.pitch(440, 1000)

        sleep(200)

The first number is the pitch.

The second number is the time in milliseconds.

----

Try These
----------------------------------------

Change the pitch.

Try:

* 220
* 330
* 550
* 660
* 880

Which sounds highest?

----

Worked Example
----------------------------------------

Press:

* Button A → Low sound.
* Button B → High sound.

.. code-block:: python

    from microbit import *
    import music

    speaker.off()

    while True:
        if button_a.is_pressed():
            music.pitch(220, 1000)

        elif button_b.is_pressed():
            music.pitch(880, 1000)

        sleep(200)

----

Mini Project 1
----------------------------------------

Create your own tune.

Rules:

* At least 6 notes.
* Use three different note lengths.
* Play it with Button A.

.. dropdown:: Mini Project 1 Solution
    :icon: codescan
    :color: primary
    :class-container: sd-dropdown-container

    .. code-block:: python

        from microbit import *
        import music

        speaker.off()

        tune = [
            "c:1",
            "d:1",
            "e:2",
            "g:2",
            "e:1",
            "c:4"
        ]

        while True:
            if button_a.is_pressed():
                music.play(tune)

            sleep(200)

----

Mini Project 2
----------------------------------------

Create a musical quiz.

Button A:

* Plays a low note.

Button B:

* Plays a high note.

Ask a friend:

"Which note is higher?"

.. dropdown:: Mini Project 2 Solution
    :icon: codescan
    :color: primary
    :class-container: sd-dropdown-container

    .. code-block:: python

        from microbit import *
        import music

        speaker.off()

        while True:
            if button_a.is_pressed():
                music.pitch(220,1000)

            elif button_b.is_pressed():
                music.pitch(880,1000)

            sleep(200)

----

Extension Challenge
----------------------------------------

Can you make a tune that:

* Starts low.
* Gets higher.
* Ends low again.

Try using:

* C4
* D4
* E4
* F4
* G4
* C5

Experiment until you like the sound.

----

Lesson Review
----------------------------------------

Before moving to the next lesson, check that you can do these things.

.. admonition:: ✔ Lesson Checklist

    Can you:

    ☐ Create your own list of notes.

    ☐ Change how long a note is played.

    ☐ Play higher and lower notes.

    ☐ Use ``music.play()`` to play your own tune.

    ☐ Use ``music.pitch()`` to play a sound.

    ☐ Change the pitch value to make higher and lower sounds.

    ☐ Design your own short melody.

    ☐ Create your own simple music project.