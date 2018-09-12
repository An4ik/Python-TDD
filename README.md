# be-fullstack-TDD

Test Driven Development - 

### How to solve task?

1. Look at the file **find_min.py**. 

2. To follow TDD the first thing we have to do is write tests for given functions.
Fortunately for you I've already created tests. (look at the file **tests/find_min_test.py**)

3. Run tests:
   
        python3 -m unittest tests/find_min_test.py
        
    You will see that it ran 7 tests and all of them FAILED (failures=7)

4. Now, complete that functions in **find_min.py**

5. After running tests all of them should be passed.

6. Compare your answer with mine located in **answers/find_min.py**

7. Commit and push your changes

___

1. Look at the file **find_max.py**. You will find that there are empty functions.

2. Run tests for find_max functions:
        
        python3 -m unittest tests/find_max_test.py
   
   You will see that it Ran 7 tests without failures, because there is no body for
   test functions in **test/find_max_test.py**   

3. You have to do:
    
    1. Write documentation for function **get_max** inside **find_max.py**
    
    2. Write test for **get_max** function inside **tests/find_max.py**
    
    3. Run tests and see that one test failed (test_get_max)
    
    4. Implement **get_max** function
    
    5. Run tests, all of the tests shoud be passed.
    
    6. Do the same for every function one by one

4. Commit and push your changes

5. Smile cause you've done good job.