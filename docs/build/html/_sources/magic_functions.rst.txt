Magic functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Magic function** is a function that you deal with, especially, when you are working with classes and objects. These functions are similar to ordinary functions, but the main difference is that they don't have to be called directly as other created methods.  
Magic function's name starts and ends with double underscores (*__*). For example, __init__(), __str__(), etc. 
These methods allow us to emulate built-in types or implement operator overloading. For example, when you want to add two objects of the same type, you can just implement magic function __add__() and use binary operator '+' to add them, instead of creating special method with arguments and call it. 

**ToDo:** Implementing simple functions.

**Learn:** Magic functions.

**Working directory:**  `**magic_functions** <https://github.com/An4ik/Python-TDD/tree/master/magic_functions>`_


Number
-------------

1. Look at the file **number.py**.

2. We have tests in (**tests/test_number.py**)

3. Run tests::

    python3 -m unittest tests/test_number.py
    # Runs 12 tests and all of them are FAILED (failures=12)

4. Now, complete the first failed function in **number.py**.

5. Run the tests *(step 3)* and make sure you have +1 passed test.


6. Repeat the steps *4 and 5* until all of them are passed.


7. Compare your answer with mine located in **answers/number.py**


You can commit your changes
