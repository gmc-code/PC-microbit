====================================================
Built-in Images
====================================================

The micro:bit has lots of pictures you can use.

Examples:

* ``Image.HEART``
* ``Image.SMILE``
* ``Image.HAPPY``
* ``Image.GIRAFFE``

Remember

* ``Image`` starts with a capital **I**.
* Image names are in **CAPITAL LETTERS**.
* Do **not** use quotation marks.

----

Show one image
--------------

Use ``display.show()`` to show a picture.

.. code-block:: python

    from microbit import *

    display.show(Image.HEART)

The micro:bit shows a heart.

----

Try it!

Change the code to show:

#. ``Image.SMILE``
#. ``Image.GIRAFFE``
#. ``Image.ARROW_N``

.. dropdown::
    :icon: codescan
    :color: primary
    :class-container: sd-dropdown-container

    .. tab-set::

        .. tab-item:: Question 1

            .. code-block:: python

                from microbit import *

                display.show(Image.SMILE)

        .. tab-item:: Question 2

            .. code-block:: python

                from microbit import *

                display.show(Image.GIRAFFE)

        .. tab-item:: Question 3

            .. code-block:: python

                from microbit import *

                display.show(Image.ARROW_N)

----

Flashing an image
-----------------

You can make an image flash.

.. code-block:: python

    from microbit import *

    while True:
        display.show(Image.HEART)
        sleep(500)
        display.clear()
        sleep(500)

The heart turns on and off.

----

Try it!

#. Change the picture to ``Image.SMILE``.
#. Make the picture stay on for **1 second**.
#. Make the picture flash faster.

.. dropdown::
    :icon: codescan
    :color: primary
    :class-container: sd-dropdown-container

    .. tab-set::

        .. tab-item:: Question 1

            .. code-block:: python

                from microbit import *

                while True:
                    display.show(Image.SMILE)
                    sleep(500)
                    display.clear()
                    sleep(500)

        .. tab-item:: Question 2

            .. code-block:: python

                from microbit import *

                while True:
                    display.show(Image.HEART)
                    sleep(1000)
                    display.clear()
                    sleep(500)

        .. tab-item:: Question 3

            .. code-block:: python

                from microbit import *

                while True:
                    display.show(Image.HEART)
                    sleep(200)
                    display.clear()
                    sleep(200)

----

Show several images
-------------------

You can show more than one image.

.. code-block:: python

    from microbit import *

    while True:
        display.show(
            [Image.HAPPY, Image.SMILE, Image.SAD],
            delay=500
        )

Each picture is shown for half a second.

----

Try it!

#. Show three animals.
#. Show four arrows.
#. Show three shapes.

.. dropdown::
    :icon: codescan
    :color: primary
    :class-container: sd-dropdown-container

    .. tab-set::

        .. tab-item:: Question 1

            .. code-block:: python

                from microbit import *

                while True:
                    display.show(
                        [Image.RABBIT, Image.COW, Image.GIRAFFE],
                        delay=500
                    )

        .. tab-item:: Question 2

            .. code-block:: python

                from microbit import *

                while True:
                    display.show(
                        [Image.ARROW_N, Image.ARROW_E,
                         Image.ARROW_S, Image.ARROW_W],
                        delay=500
                    )

        .. tab-item:: Question 3

            .. code-block:: python

                from microbit import *

                while True:
                    display.show(
                        [Image.TRIANGLE, Image.DIAMOND,
                         Image.SQUARE],
                        delay=500
                    )



