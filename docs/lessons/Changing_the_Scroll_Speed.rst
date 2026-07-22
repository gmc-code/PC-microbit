====================================================
Changing the Scroll Speed
====================================================

You can change how fast the message moves.

A **small** delay scrolls faster.

A **large** delay scrolls slower.

----

Fast scroll
-----------

.. code-block:: python

    from microbit import *

    while True:
        display.scroll("Fast", delay=60)

Slow scroll
-----------

.. code-block:: python

    from microbit import *

    while True:
        display.scroll("Slow", delay=250)

----

.. admonition:: Try it

    #. Make your name scroll quickly.
    #. Make your name scroll slowly.
    #. Try your own delay number.

----

More than one message
---------------------

You can scroll more than one message.

.. code-block:: python

    from microbit import *

    while True:
        display.scroll("My name is")
        display.scroll("Sam")

Another example

.. code-block:: python

    from microbit import *

    while True:
        display.scroll("I like")
        display.scroll("Pizza")

----

.. admonition:: Try it

    #. Scroll "My name is" then your name.
    #. Scroll "I like" then your favourite food.
    #. Scroll "I am" then your age.

----

Challenge
----------

Create a short introduction using two or three messages.

