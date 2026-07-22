====================================================
For Loops with words
====================================================

A **for loop** repeats some code.

It works through one letter at a time.

----

Loop through a word
-------------------

.. code-block:: python

    from microbit import *

    word = "HELLO"

    while True:
        for letter in word:
            display.scroll(letter)

The loop scrolls one letter at a time.

It scrolls:

H

E

L

L

O

----

Remember

* ``word`` is the whole word.
* ``letter`` is one letter.
* The loop repeats until every letter has been shown.

----

Try it!

#. Change the word to **winner**.
#. Change the word to **Python**.
#. Change the word to your own name.

.. dropdown::
    :icon: codescan
    :color: primary
    :class-container: sd-dropdown-container

    .. tab-set::

        .. tab-item:: Question 1

            .. code-block:: python

                from microbit import *

                word = "winner"

                while True:
                    for letter in word:
                        display.scroll(letter)

        .. tab-item:: Question 2

            .. code-block:: python

                from microbit import *

                word = "Python"

                while True:
                    for letter in word:
                        display.scroll(letter)

        .. tab-item:: Question 3

            .. code-block:: python

                from microbit import *

                word = "Sam"

                while True:
                    for letter in word:
                        display.scroll(letter)

----

Adding another action
---------------------

You can do more than one thing inside the loop.

.. code-block:: python

    from microbit import *

    word = "CAT"

    while True:
        for letter in word:
            display.scroll(letter)
            display.show(Image.HEART)

A heart is shown after each letter.

----

Try it!

#. Show a smile after each letter.
#. Show a happy face after each letter.
#. Change the word to **DOG**.
