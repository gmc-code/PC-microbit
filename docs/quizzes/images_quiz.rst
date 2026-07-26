====================================================
Built-in Images Quiz
====================================================

Section 1: Multiple Choice
==========================

Question 1
----------

.. multichoice::

    Which line of code correctly displays a built-in heart image on the micro:bit?
    [x] display.show(Image.HEART) | Correct! "Image" starts with a capital I and HEART is in ALL CAPS.
    [ ] display.show(image.HEART) | Incorrect. The word "Image" must start with a capital "I".
    [ ] display.show(Image.heart) | Incorrect. Built-in image names like HEART must be in ALL CAPS.

----

Question 2
----------

.. multichoice::

    How must all built-in image names be written in your Python code?
    [ ] In lower case letters | Incorrect. Built-in image names do not use lower case.
    [x] In ALL CAPS letters | Correct! All built-in image names must be written in ALL CAPS.
    [ ] Inside quotation marks | Incorrect. You do not put quotation marks around image names.

----

Question 3
----------

.. multichoice::

    Which function is used to show a single built-in image on the micro:bit screen?
    [ ] display.scroll() | Incorrect. scroll() is used for text words and messages.
    [x] display.show() | Correct! show() is used to display images on the screen.
    [ ] display.draw() | Incorrect. There is no draw() function in the microbit library.

----

Question 4
----------

.. multichoice::

    What happens when you type "Image." (with the dot) in the micro:bit Python editor?
    [ ] The micro:bit immediately turns on. | Incorrect. Code only runs when you download it.
    [x] A drop-down menu pops up showing available images. | Correct! The editor shows a list of images you can pick from.
    [ ] An error message appears on the screen. | Incorrect. Typing "Image." is correct syntax and will not trigger an error.

----

Question 5
----------

.. multichoice::

    When using "display.show(image_list, delay=500)", what does the delay number control?
    [x] How many milliseconds each image stays on the screen. | Correct! The delay sets the pause time between images in milliseconds.
    [ ] How many total images are in your list. | Incorrect. The list size depends on how many images you add to it.
    [ ] The brightness of the micro:bit LED lights. | Incorrect. Delay controls time, not screen brightness.

----

Section 2: Code Ordering
========================

Question 6
----------

| Put the lines of code in order to show a built-in HAPPY face on the micro:bit screen.

.. ordering::
    :theme: light

    from microbit import *

    display.show(Image.HAPPY)

----

Question 7
----------

| Order the lines below to make a heart picture flash on and off every half second (500ms).

.. ordering::
    :theme: light

    from microbit import *

    while True:
        display.show(Image.HEART)
        sleep(500)
        display.clear()
        sleep(500)

----

Question 8
----------

| Put the lines of code in order to save a list of three faces in a variable and animate them.

.. ordering::
    :theme: light

    from microbit import *

    face_list = [Image.HAPPY, Image.SMILE, Image.SAD]
    while True:
        display.show(face_list, delay=300)

----

Section 3: Cloze (Dropdown Selection)
=====================================

Question 9
----------

| Complete the code to import the micro:bit library and display a built-in duck picture.

.. cloze::

    from microbit @@ import | include | get @@ *

    display.@@ show | scroll | write @@(Image.DUCK)

----

Question 10
-----------

| Complete the code to show a built-in arrow image pointing North.

.. cloze::

    from microbit import *

    display.show(Image.@@ ARROW_N | arrow_n | "ARROW_N" @@)

----

Question 11
-----------

| Complete the code to animate a pre-made list of built-in clock images with a delay of 200 milliseconds.

.. cloze::

    from microbit import *

    while True:
        display.show(Image.@@ ALL_CLOCKS | ALL_ARROWS | CLOCK @@, delay=@@ 200 | "200" | 200ms @@)

----

Section 4: Fill in Gaps (Text Entry)
=====================================

Question 12
-----------

| Fill in the gaps to import all tools from the micro:bit library and show a happy face.

.. gapfill::

    from microbit import @@* | ALL@@

    display.@@show | scroll@@(Image.HAPPY)

----

Question 13
-----------

| Complete the code to clear the micro:bit display screen after waiting 1000 milliseconds.

.. gapfill::

    display.show(Image.GIRAFFE)
    @@sleep | wait@@(1000)
    display.@@clear() | reset()@@

----

Question 14
-----------

| Fill in the missing code to loop through a custom list variable of animal images with a 400ms delay.

.. gapfill::

    animal_list = [Image.RABBIT, Image.COW, Image.GIRAFFE]

    @@while | for@@ True:
        display.show(@@animal_list | Image.ALL_ANIMALS@@, delay=400)

