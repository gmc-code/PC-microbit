====================================================
Using Variables
====================================================

A **variable** stores information.

You can give it a name and use it later.

----

A text variable
---------------

.. code-block:: python

    from microbit import *

    name = "Sam"

    while True:
        display.scroll(name)

----

A number variable
-----------------

.. code-block:: python

    from microbit import *

    age = 11

    while True:
        display.scroll(age)

----

Using more than one variable
----------------------------

.. code-block:: python

    from microbit import *

    name = "Sam"
    age = 11

    while True:
        display.scroll(name)
        display.scroll(age)

----

.. admonition:: Try it

    #. Change the name to your own.
    #. Change the age.
    #. Add a variable called ``colour``.
    #. Display the colour.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Solution

                .. code-block:: python

                    from microbit import *

                    name = "Sam"
                    age = 11
                    colour = "Blue"

                    while True:
                        display.scroll(name)
                        display.scroll(age)
                        display.scroll(colour)

----

Challenge
----------

Create these variables:

* ``pet``
* ``age``
* ``place``

Display them one after another.

