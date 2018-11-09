Decorators
^^^^^^^^^^^
Decorator - dynamically alter the functionality of a function, method, or class
without having to directly use subclasses or change the source code of the
function being decorated.

**ToDo:**
    1. Research & Read about functions and decorators.

    2. Implement simple decorator.

    3. Implement decorator with arguments.

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

1. Look at the file `stringify.py <https://github.com/An4ik/Python-TDD/blob/master/decorator/stringify.py/>`_

2. Run tests::

    python3 -m unittest tests/test_stringify.py
    # Runs 4 tests and all of them are FAILED (failures=4)

4. Now, complete the first failed function in **stringify.py**.

5. Run the tests *(step 3)* and make sure you have +1 passed test.


6. Repeat the steps *4 and 5* until all of them are passed.


7. Compare your answer with mine located in **answers/stringify.py**

You can commit your changes


Python's Decorator Syntax
-----------------------------

Python makes creating and using decorators a bit cleaner and nicer for
the programmer through some syntactic sugar To decorate get_text we don't
have to get_text = p_decorator(get_text) There is a neat shortcut for that,
which is to mention the name of the decorating function before the function
to be decorated. The name of the decorator should be perpended with an @ symbol.

Example
++++++++++++++
::

    def p_decorate(func):
        def func_wrapper(name):
            return "<p>{0}</p>".format(func(name))
        return func_wrapper

    @p_decorate
    def get_text(name):
       return "lorem ipsum, {0} dolor sit amet".format(name)

    print(get_text("John"))
    # Outputs <p>lorem ipsum, John dolor sit amet</p>

Composition of Decorators
++++++++++++++++++++++++++

::

        def p_decorate(func):
            def func_wrapper(name):
               return "<p>{0}</p>".format(func(name))
            return func_wrapper

        def strong_decorate(func):
            def func_wrapper(name):
                return "<strong>{0}</strong>".format(func(name))
            return func_wrapper

        def div_decorate(func):
            def func_wrapper(name):
                return "<div>{0}</div>".format(func(name))
            return func_wrapper

        get_text = div_decorate(p_decorate(strong_decorate(get_text)))
        print get_text("John")

        # Or pythonic approach
        @div_decorate
        @p_decorate
        @strong_decorate
        def get_text(name):
           return "lorem ipsum, {0} dolor sit amet".format(name)

        print get_text("John")
        # Both output <div><p><strong>lorem ipsum, John dolor sit amet</strong></p></div>

Debugging decorated functions
+++++++++++++++++++++++++++++++

At the end of the day decorators are just wrapping our functions, in case of
debugging that can be problematic since the wrapper function does not carry
the name, module and docstring of the original function. Based on the example
above if we do:

::

    print get_text.__name__
    # Outputs func_wrapper


The output was expected to be get_text yet, the attributes __name__, __doc__,
and __module__ of get_text got overridden by those of the wrapper(func_wrapper).
Obviously we can reset them within func_wrapper but Python provides a much nicer way.

::

    from functools import wraps

    def tags(tag_name):
        def tags_decorator(func):
            @wraps(func)
            def func_wrapper(name):
                return "<{0}>{1}</{0}>".format(tag_name, func(name))
            return func_wrapper
        return tags_decorator

    @tags("p")
    def get_text(name):
        """returns some text"""
        return "Hello "+name

    print get_text.__name__ # get_text
    print get_text.__doc__ # returns some text
    print get_text.__module__ # __main__


Registration
-------------

1. Look at the file `registration.py <https://github.com/An4ik/Python-TDD/blob/master/decorator/registration.py/>`_

2. Run tests::

    python3 -m unittest tests/test_registration.py
    # Runs 4 tests and all of them are FAILED (failures=4)

4. Now, complete the first failed function in **registration.py**.

5. Run the tests *(step 3)* and make sure you have +1 passed test.


6. Repeat the steps *4 and 5* until all of them are passed.


7. Compare your answer with mine located in **answers/registration.py**

You can commit your changes