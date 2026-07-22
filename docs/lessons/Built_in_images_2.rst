====================================================
Image Lists
====================================================

Sometimes you want to use the same list of images more than once.

You can save the list in a **variable**.

----

Using a variable
----------------

.. code-block:: python

    from microbit import *

    face_list = [
        Image.HAPPY,
        Image.SMILE,
        Image.SAD,
    ]

    while True:
        display.show(face_list, delay=500)

The variable ``face_list`` stores three images.

``display.show()`` uses the variable to show all the images.

----

Remember

* A variable gives something a name.
* The variable can have any sensible name.
* ``face_list`` is a good name because it stores face images.

----

Try it!

#. Change the faces to three animals.
#. Change the delay to **300** milliseconds.
#. Add another image to the list.

.. dropdown::
    :icon: codescan
    :color: primary
    :class-container: sd-dropdown-container

    .. tab-set::

        .. tab-item:: Question 1

            .. code-block:: python

                from microbit import *

                animal_list = [
                    Image.RABBIT,
                    Image.COW,
                    Image.GIRAFFE,
                ]

                while True:
                    display.show(animal_list, delay=500)

        .. tab-item:: Question 2

            .. code-block:: python

                from microbit import *

                face_list = [
                    Image.HAPPY,
                    Image.SMILE,
                    Image.SAD,
                ]

                while True:
                    display.show(face_list, delay=300)

        .. tab-item:: Question 3

            .. code-block:: python

                from microbit import *

                face_list = [
                    Image.HAPPY,
                    Image.SMILE,
                    Image.SAD,
                    Image.CONFUSED,
                ]

                while True:
                    display.show(face_list, delay=500)

----

Built-in image lists
--------------------

The micro:bit already has some image lists.

Two useful ones are:

* ``Image.ALL_ARROWS``
* ``Image.ALL_CLOCKS``

You can use them without making your own list.

Example

.. code-block:: python

    from microbit import *

    while True:
        display.show(Image.ALL_ARROWS, delay=300)

The arrows point in different directions.

----

Try it!

#. Show ``Image.ALL_CLOCKS``.
#. Make the arrows change more slowly.
#. Make the clocks change faster.

.. dropdown::
    :icon: codescan
    :color: primary
    :class-container: sd-dropdown-container

    .. tab-set::

        .. tab-item:: Question 1

            .. code-block:: python

                from microbit import *

                while True:
                    display.show(Image.ALL_CLOCKS, delay=300)

        .. tab-item:: Question 2

            .. code-block:: python

                from microbit import *

                while True:
                    display.show(Image.ALL_ARROWS, delay=700)

        .. tab-item:: Question 3

            .. code-block:: python

                from microbit import *

                while True:
                    display.show(Image.ALL_CLOCKS, delay=100)

----

Challenge
---------

Can you make your own image list?

Choose a theme.

Ideas:

* Animals
* Faces
* Shapes
* Arrows

Give your list a sensible variable name.

Example:

.. code-block:: python

    from microbit import *

    animal_list = [
        Image.RABBIT,
        Image.COW,
        Image.DUCK,
        Image.GIRAFFE,
    ]

    while True:
        display.show(animal_list, delay=400)


