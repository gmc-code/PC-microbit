====================================================
micro:bit Selection & Buttons Quiz
====================================================

Section 1: Multiple Choice
==========================

Question 1
----------

.. multichoice::

    Which method is used to check if Button A is currently being held down on the micro:bit?
    [x] button_a.is_pressed() | Correct! is_pressed() returns True if the button is currently pressed.
    [ ] button_a.was_pressed() | Incorrect. was_pressed() checks if the button was pressed since the last check.
    [ ] button_a.get_presses() | Incorrect. get_presses() returns the total count of button presses.

----

Question 2
----------

.. multichoice::

    In Python, which keyword is used for "otherwise, check this condition"?
    [ ] else if | Incorrect. In Python, "elif" is used instead of "else if".
    [x] elif | Correct! "elif" stands for "else if" in Python.
    [ ] otherwise | Incorrect. "otherwise" is not a valid Python keyword.

----

Question 3
----------

.. multichoice::

    When does the code inside an `else:` block run?
    [ ] Whenever any button is pressed. | Incorrect. It runs when preceding if/elif conditions evaluate to False.
    [x] When none of the preceding `if` or `elif` conditions are True. | Correct! `else` acts as the fallback option when no prior condition matches.
    [ ] Only when the program first starts up. | Incorrect. `else` evaluates every time through the loop when previous conditions are False.

----

Question 4
----------

.. multichoice::

    What happens if both button_a and button_b are pressed at the same time in an if/elif chain in which button_a is first checked?
    [x] Only the code inside the `if button_a.is_pressed():` block executes. | Correct! Python checks conditions sequentially and executes only the first branch that is True.
    [ ] Both code blocks execute simultaneously. | Incorrect. Python evaluates sequentially and skips remaining elif blocks once a match is found.
    [ ] An error occurs and the micro:bit resets. | Incorrect. Python safely executes the first valid conditional branch.

----

Question 5
----------

.. multichoice::

    Which built-in image object would you use to show a heart image on the display?
    [x] Image.HEART | Correct! Image.HEART is the standard built-in image constant.
    [ ] display.HEART | Incorrect. Built-in images belong to the `Image` module, not `display`.
    [ ] image.heart | Incorrect. Image constants are capitalized and referenced on `Image`.

----

Section 2: Cloze
=====================================

Question 6
----------

| Complete the code to check if button A is pressed and show a happy face.

.. cloze::

    from microbit import *

    while True:
        if @@ button_a.is_pressed() | button_a.pressed() | button_a.is_pressed @@:
            display.show(Image.@@ HAPPY | happy | Happy @@)

----

Question 7
----------

| Complete the structure to show a happy face if A is pressed, otherwise show a sad face.

.. cloze::

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show(Image.HAPPY)
        @@ else | elif | then @@:
            display.show(Image.SAD)

----

Question 8
----------

| Complete the conditional chain to check Button A first, then Button B.

.. cloze::

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show(Image.HAPPY)
        @@ elif | else if | else @@ button_b.is_pressed():
            display.show(Image.SAD)

----

Question 9
----------

| Complete the code to check both buttons and show CONFUSED if neither is pressed.

.. cloze::

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show(Image.HOUSE)
        elif button_b.is_pressed():
            display.show(Image.HEART)
        @@ else | elif | otherwise @@:
            display.show(Image.@@ CONFUSED | SAD | SMILE @@)

----

Question 10
-----------

| Complete the code to scroll your name when button A is pressed.

.. cloze::

    from microbit import *

    while True:
        if @@ button_a.is_pressed() | button_a.pressed() | button_a.is_pressed @@:
            display.@@ scroll | show | print @@("Sam")

----

Section 3: Code Ordering
========================

Question 11
-----------

| Put the lines of code in order to check if Button A is pressed and display a HAPPY image.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show(Image.HAPPY)

----

Question 12
-----------

| Order the lines to show a HAPPY face when Button A is pressed, and a SAD face otherwise.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show(Image.HAPPY)
        else:
            display.show(Image.SAD)

----

Question 13
-----------

| Order the lines to check Button A (shows HAPPY) and Button B (shows SAD).

.. ordering::
    :theme: light

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show(Image.HAPPY)
        elif button_b.is_pressed():
            display.show(Image.SAD)

----

Question 14
-----------

| Put the lines in order for three choices: Button A (HOUSE), Button B (HEART), or neither (SMILE).

.. ordering::
    :theme: light

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show(Image.HOUSE)
        elif button_b.is_pressed():
            display.show(Image.HEART)
        else:
            display.show(Image.SMILE)

----

Question 15
-----------

| Order the lines to scroll "Sam" if Button A is pressed, scroll "12" if Button B is pressed, or show a HEART otherwise.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.scroll("Sam")
        elif button_b.is_pressed():
            display.scroll("12")
        else:
            display.show(Image.HEART)



