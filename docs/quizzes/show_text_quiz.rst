====================================================
micro:bit Text, Screen & Library Quiz
====================================================

Section 1: Multiple Choice
==========================

Question 1
----------

.. multichoice::

    Which line must be placed at the very top of every micro:bit program?
    [x] from microbit import * | Correct! This gives your program access to display, buttons, and sensors.
    [ ] import microbit | Incorrect. While valid Python, this forces you to write microbit.display.show() instead.
    [ ] from microbot import * | Incorrect. "microbit" is spelled wrong in this line.

----

Question 2
----------

.. multichoice::

    What happens to text when you display it using display.show()?
    [ ] The text slides across the screen horizontally. | Incorrect. Text displayed with show() stays still instead of moving.
    [x] The text does not move and letters appear one at a time. | Correct! display.show() displays stationary characters one by one.
    [ ] The letters flash on the screen all at the exact same time. | Incorrect. Each letter is shown sequentially, one after another.

----

Question 3
----------

.. multichoice::

    How long will sleep(1000) pause a micro:bit program?
    [ ] Half a second | Incorrect. Half a second is written as sleep(500).
    [x] 1 full second | Correct! 1000 milliseconds equals 1 full second.
    [ ] 10 seconds | Incorrect. 10 seconds would be written as sleep(10000).

----

Question 4
----------

.. multichoice::

    What does display.clear() do to the micro:bit LED screen?
    [ ] It scrolls the screen backward. | Incorrect. Scrolling is done with display.scroll().
    [x] It wipes the screen to make it completely blank. | Correct! display.clear() turns off all LEDs to blank the screen.
    [ ] It resets the micro:bit program back to line 1. | Incorrect. It only clears the screen lights, not the program state.

----

Question 5
----------

.. multichoice::

    Which setting makes text display faster when using display.show("Hi", delay=...)?
    [x] A smaller delay number (like 150) | Correct! A smaller delay time speeds up letter transitions.
    [ ] A larger delay number (like 2000) | Incorrect. Larger delay numbers make letter transitions slower.
    [ ] Setting delay=0 | Incorrect. Setting delay to 0 causes letters to flash by instantly without being readable.

----

Section 2: Cloze (Dropdown Selection)
=====================================

Question 6
----------

| Complete the standard import line used to start micro:bit Python programs.

.. cloze::

    from @@ microbit | microbot | display @@ import @@ * | all | display @@

----

Question 7
----------

| Complete the code to show the text "Hello" on the screen continuously.

.. cloze::

    from microbit import *

    while @@ True | true | 1 @@:
        display.@@ show | print | write @@("Hello")

----

Question 8
----------

| Complete the code to show a number quickly with a custom speed of 150ms.

.. cloze::

    from microbit import *

    while True:
        display.show(@@ 7 | "7" | seven @@, delay=@@ 150 | "150" | 150ms @@)

----

Question 9
----------

| Complete the code to pause for 1 second and then blank out the display grid.

.. cloze::

    from microbit import *

    display.show("Hi")
    @@ sleep | pause | wait @@(1000)
    display.@@ clear | wipe | blank @@()

----

Question 10
-----------

| Complete the shortcut parameter that automatically clears the display after showing "Hello".

.. cloze::

    from microbit import *

    while True:
        display.show("Hello", @@ clear=True | clear=False | erase=True @@)
        sleep(1000)

----

Section 3: Code Ordering
========================

Question 11
-----------

| Put the lines of code in order to start a program properly and display the name "Sam".

.. ordering::
    :theme: light

    from microbit import *

    while True:
        display.show("Sam")

----

Question 12
-----------

| Order the lines below to show the number 11 continuously with a slow delay of 500ms.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        display.show(11, delay=500)

----

Question 13
-----------

| Put the instructions in order to show "Hi", wait 1 second, clear the screen, and wait 1 second before repeating.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        display.show("Hi")
        sleep(1000)
        display.clear()
        sleep(1000)

----

Question 14
-----------

| Order the lines to show "I like" for 1 second, then show "Pizza" for 1 second continuously.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        display.show("I like")
        sleep(1000)
        display.show("Pizza")
        sleep(1000)

----

Question 15
-----------

| Order the code segments to show a message and automatically clear the screen using clear=True.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        display.show("Hello", clear=True)
        sleep(1000)

