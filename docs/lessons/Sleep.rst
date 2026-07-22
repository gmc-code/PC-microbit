====================================================
Sleep
====================================================

The ``sleep()`` command pauses your program for a short time.

Sleep
-----

.. py:function:: sleep(time)

    Pause the program for a number of milliseconds.

Remember:

* ``1000`` milliseconds = **1 second**
* ``500`` milliseconds = **half a second**
* ``250`` milliseconds = **quarter of a second**

Example:

.. code-block:: python

    from microbit import *

    display.show(Image.HAPPY)
    sleep(1000)
    display.show(Image.SAD)

The happy face stays on the screen for **1 second** before changing.

----

Another example

.. code-block:: python

    from microbit import *

    while True:
        display.scroll("Hello")
        sleep(1000)
        display.scroll("World")
        sleep(1000)

The program waits for **1 second** after each word.

----

.. admonition:: Try it!

    Change the program above.

    #. Change the **first** sleep to **500** milliseconds (half a second).
    #. Change the **second** sleep to **250** milliseconds (quarter of a second).
    #. Change **both** sleeps to **2000** milliseconds (2 seconds).

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Question 1

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll("Hello")
                        sleep(500)
                        display.scroll("World")
                        sleep(1000)

            .. tab-item:: Question 2

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll("Hello")
                        sleep(1000)
                        display.scroll("World")
                        sleep(250)

            .. tab-item:: Question 3

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll("Hello")
                        sleep(2000)
                        display.scroll("World")
                        sleep(2000)