Decorators
^^^^^^^^^^^
Decorator - is a function that get function as an argument and returns function.

**ToDo:**
    1. Read about functions and decorators.
    1. Implementing simple decorator.
    2. Implementing decorator with arguments.

**Learn:** Decorator.

**Working directory:**  `**decorator** <https://github.com/An4ik/Python-TDD/tree/master/decorator>`_

What you need to know about functions
-------------------------------------------

Before diving in, there are some prerequisites that should be clear.
In Python, functions are first class citizens, they are objects and
that means we can do a lot of useful stuff with them.

Assign functions to variables
++++++++++++++++++++++++++++++++
::

    def greet(name):
        return "hello " + name

    greet_someone = greet
    print (greet_someone("John"))

    # Outputs: hello John


Define functions inside other functions
++++++++++++++++++++++++++++++++++++++++++++
::

    def greet(name):
        def get_message():
            return "Hello "

        result = get_message() + name

        return result

    print (greet("John"))
    # Outputs: Hello John



Functions can return other functions
++++++++++++++++++++++++++++++++++++++++++++

In other words, functions generating other functions.
::

    def compose_greet_func():
        def get_message():
            return "Hello there!"
        return get_message

    greet = compose_greet_func()
    print (greet())
    # Outputs: Hello there!



Inner functions have access to the enclosing scope
++++++++++++++++++++++++++++++++++++++++++++++++++

More commonly known as a closure. A very powerful pattern that we will come
across while building decorators. Another thing to note, Python only allows
read access to the outer scope and not assignment. Notice how we modified
the example above to read a "name" argument from the enclosing scope of the
inner function and return the new function.

::

    def compose_greet_func():
        def get_message():
            return "Hello there!"
        return get_message

    greet = compose_greet_func()
    print (greet())
    # Outputs: Hello there!



Stringify
-------------

1. Look at the file **stringify.py**.

2. Run tests::

    python3 -m unittest tests/test_stringify.py
    # Runs 4 tests and all of them are FAILED (failures=4)

4. Now, complete the first failed function in **stringify.py**.

5. Run the tests *(step 3)* and make sure you have +1 passed test.


6. Repeat the steps *4 and 5* until all of them are passed.


7. Compare your answer with mine located in **answers/stringify.py**

You can commit your changes


What you need to know about functions
-------------------------------------------

Before diving in, there are some prerequisites that should be clear.
In Python, functions are first class citizens, they are objects and
that means we can do a lot of useful stuff with them.

Assign functions to variables
++++++++++++++++++++++++++++++++
::

    def greet(name):
        return "hello " + name

    greet_someone = greet
    print (greet_someone("John"))

    # Outputs: hello John
