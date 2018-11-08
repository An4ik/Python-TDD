Context managers are a way of allocating and releasing some sort of resource exactly where you need it. The most widely used example of context managers is the 'with' statement.

If you forget to close the file or let's say the database, it will later lead to big consequences. But with context manager, you don’t need to remember this, it will close everything for you.

We can implement context manager as generator 

```
from contextlib import contextmanager
@contextmanager
```
or as class by using magic functions
```
__init__
__enter__
__exit__
```
### LEVEL-1.

1. Look at the file write_into_file.py

2. Look at the tests in tests folter 

3. Run tests with command:

    ```python3 -m unittest tests/tests_for_level_one.py```
   As you see all your tests are failed

4. Now, complete the functions in write_into_file.py

5. Run tests and all of them should be passed.

6. Compare your answer with mine located in answers/write_into_file.py

7. Congratulations, you have passed first level. Commit and push your changes. 

### LEVEL-2