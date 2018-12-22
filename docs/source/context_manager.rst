Context manager
^^^^^^^^^^^^^^^^^

**ToDo:** Read about context manager. Pass three levels for a better understanding.

**Learn:** Context manager

**Working directory:**  `**context_manager** <https://github.com/An4ik/Python-TDD/tree/master/context_manager>`_

**Context managers** are a way of allocating and releasing some sort of resource exactly where you need it. The most widely used example of context managers is the 'with' statement.

If you forget to close the file or let's say the database, it will later lead to big consequences. But with context manager, you don’t need to remember this, it will close everything for you.

We can implement context manager as generator::

    from contextlib import contextmanager
    @contextmanager

or as class by using magic functions::

    __init__
    __enter__
    __exit__

We want you to pass three levels for a better understanding of **context manager**

<<<<<<< HEAD


LEVEL-1
-------
=======
Context manager as class
------------------------

1. Look at the file context_manager_as_class.py

2. Look at the test_context_manager_as_class.py in tests folder

3. Run tests with command::

    python3 -m unittest tests/test_context_manager_as_class.py

   As you see all your tests are failed

4. Now, complete the functions in context_manager_as_class.py

5. Run tests and all of them should be passed.

6. Compare your answer with mine located in answers/change_directory.py

7. Congratulations, you have passed first level. Commit and push your changes.

Write into file
---------------
>>>>>>> cdb42cc1efb71900fdcfa9b0e9831c25313b30ee

1. Look at the file write_into_file.py

2. Look at the tests in tests folter

3. Run tests with command::

<<<<<<< HEAD
    python3 -m unittest tests/tests_for_level_one.py
=======
    python3 -m unittest tests/tests_write_into_file.py
>>>>>>> cdb42cc1efb71900fdcfa9b0e9831c25313b30ee

   As you see all your tests are failed

4. Now, complete the functions in write_into_file.py

5. Run tests and all of them should be passed.

6. Compare your answer with mine located in answers/write_into_file.py

7. Congratulations, you have passed first level. Commit and push your changes.

<<<<<<< HEAD
LEVEL-2
-------

=======
Change directory
----------------
1. Look at the file change_directory.py

2. Look at the test_change_directory.py in tests folder

3. Run tests with command::

    python3 -m unittest tests/test_change_directory.py

   As you see all your tests are failed

4. Now, complete the functions in change_directory.py

5. Run tests and all of them should be passed.

6. Compare your answer with mine located in answers/change_directory.py

7. Congratulations, you have passed second level. Commit and push your changes.
>>>>>>> cdb42cc1efb71900fdcfa9b0e9831c25313b30ee
