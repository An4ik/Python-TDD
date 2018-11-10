###Decorators

#####Part-1. Simple decorator - stringify.

**Problem**: *add, multiply* functions return int, but we want it to be str.

**Solution**: Implement *stringify* function which is changes return type of the given function to str type and wrap (decorate) *add, multiply* methods.

**To Do:**

1. Look at the file **stringify.py**. 

2. Run tests:
   
        python3 -m unittest tests/test_stringify.py
        
    You will see that it ran 4 tests and all of them FAILED (failures=4)

3. Now, complete that functions in **stringify.py**.

4. Run tests (step 3) and all of them should be passed.

5. Compare your answer with mine located in **answers/stringify.py**

6. Commit and push your changes

#####Part-2. Decorator with arguments - registration

**Problem**: We want to register/unregister subject. Know subject's status (is active or not). Print all active subjects.

**Solution**: Implement *register* function which set attribute *is_active* equals to the *is_active* param and add it to the *registered* set if is_active otherwise discard it from registered.

**To Do:**

1. Look at the file **registration.py**. 

2. Run tests:
   
        python3 -m unittest tests/test_registration.py
        
    You will see that it ran 11 tests and all of them FAILED (failures=11)

3. Now, complete that functions in **registration.py**.

4. Run tests (step 3) and all of them should be passed.

5. Compare your answer with mine located in **answers/registration.py**

6. Commit and push your changes