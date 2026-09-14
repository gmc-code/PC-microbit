====================================================
For loops with lists
====================================================

| Make the following programs in edublocks.
| Try them on the simulator first and then on your micro:bit.

----

Words in a list
---------------

.. image:: images/eb_scroll_helloworld.png
    :scale: 25 %

----
.. code-block:: python

    from microbit import *

    animals = [
        "Duck",
        "Rabbit",
        "Cow",
    ]

    while True:
        for animal in animals:
            display.scroll(animal)

The loop scrolls each animal.

----

Try it!

#. Change the list to three colours.
#. Change the list to three names.
#. Add another animal.

----

Numbers in a list
-----------------

.. code-block:: python

    from microbit import *

    numbers = [1, 2, 3, 4]

    while True:
        for number in numbers:
            display.show(number)
            sleep(500)

Each number is shown.

----

Try it!

#. Show 5, 6, 7.
#. Show 9 down to 1.
#. Make the numbers change faster.

----


Images in a list
---------------------------

.. code-block:: python

    from microbit import *

    images = [
        Image.DUCK,
        Image.RABBIT,
        Image.COW,
    ]

    while True:
        for image in images:
            display.show(image)
            sleep(1000)

The loop shows each image.

----

Try it!

#. Add another animal image.
#. Change the list to three shapes.
#. Change the list to three faces.
