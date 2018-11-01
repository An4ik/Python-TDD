**PART-1. Read and try to understand**

**be-fullstack-TDD**

Test Driven Development (TDD) - is a software development process that relies on the repetition of a very short development cycle: requirements are turned into very specific test cases, then the software is improved to pass the new tests, only.

Dear bratishka or sestrenka, We hope you have some knowledge about classmethods, staticmethods, property.
In any case, these are small explanations on these topics.

Classmethod:
    The @classmethod decorator, is a builtin function decorator that is an expression that gets evaluated after your function is defined. The result of that evaluation shadows your function definition.
    A class method receives the class as implicit first argument, just like an instance method receives the instance
    Syntax:
    class C(object):
        @classmethod
        def fun(cls, arg1, arg2, ...):
        ....
    fun: function that needs to be converted into a class method
    returns: a class method for function.
    -A class method is a method which is bound to the class and not the object of the class.
    -They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
    -It can modify a class state that would apply across all the instances of the class. For example it can modify a class variable that will be applicable to all the instances

Staticmethod:
    A static method does not receive an implicit first argument.
    Syntax:

    class C(object):
        @staticmethod
        def fun(arg1, arg2, ...):
            ...
    returns: a static method for function fun.
    -A static method is also a method which is bound to the class and not the object of the class.
    -A static method can’t access or modify class state.
    -It is present in a class because it makes sense for the method to be present in class.

Property:
    Getters and setters are used in many object oriented programming languages to ensure the principle of data encapsulation(is seen as the bundling of data with the methods that operate on these data.)
    These methods are of course the getter for retrieving the data and the setter for changing the data.
    According to this principle, the attributes of a class are made private to hide and protect them from other code.
    @property is basically a pythonic way to use getters and setters.
    Python has a great concept called property which makes the life of an object-oriented programmer much simpler.

P.S. Don't be upset, if not everything is clear. Google will help you

**PART-2. Hard work:)**
    
    1. Look at the file classmethods.py.
    2. To follow TDD the first thing you have to do is to write tests for the given functions.
       Fortunately for you I've already created tests. (look at the file tests/test_classmethods.py)
    3. Run tests for classmethods functions:
      
            `python3 -m unittest tests/test_classmethods.py`
                           
       You will see that it ran 1 test and all of them FAILED (failures=1).
    4. Now, complete that functions in classmethods.py.
    5. Run tests (step 3) and all of them should be passed.
    6. Compare your answer with mine located in answers/classmethods.py.
    7. Commit and push your changes.
    8. Do all the same for staticmethods and property.
    