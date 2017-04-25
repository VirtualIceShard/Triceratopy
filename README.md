# Triceratopy
_Currently under development_(*version 0.0.1*)
##### &nbsp;
Triceratopy is a collection of utilities, that includes a variety of decorators and functions to make some tasks easier or even to organize your code better. Triceratopy includes:
- Function decorator utilities(simple logs, multiple calls in one line, multiple calls sequence)
- Objects and decorators setters and getters using an index thats automatically do the wor of creating sub-dicionaries and objects
- The use of capsules(_see capsules_) to make code organization easier and create the possibility to separate modules into "sub-modules"
### Function decorators
##### **simple log**
Triceratopy contains a decorator to simple function logging, it's called *simple log*. This decorator returns the fucntion arguments, the execution start and end time and the return, simple informations that are very useful when you need to log something simple and less complex. Here's an example:

    @triceratopy.functions.simple_log
    def say_smth(num, str, add="wow", rlly=3):
        print(num,str,add,rlly)
        return num
    cps1 = capsule1()
    print(cps1.sum(3,8))
    print(cps1.wow)
    say_smth(3,"hey", rlly=55)
    say_smth(34,"nop")
    say_smth(23, "uhu", add="hah", rlly="rly?")

Here's the log:

    [17:11]Calling say_smth(3,hey,rlly=55)
    [17:11]Started running
    3 hey wow 55
    [17:11]Ended
    [17:11]Returned: 3
    [17:11]Calling say_smth(34,nop)
    [17:11]Started running
    34 nop wow 3
    [17:11]Ended
    [17:11]Returned: 34
    [17:11]Calling say_smth(23,uhu,add='hah',rlly='rly?')
    [17:11]Started running
    23 uhu hah rly?
    [17:11]Ended
    [17:11]Returned: 23
___
##### **multiple calls and multiple calls list**
These two decoratos add a very interesting behavior to the function. The first, `multiple_calls` makes possible to call a function as many times as you want in one line, then you can get the return of all the calls as a _tuple_ by using `__return__`. See below:

    @triceratopy.functions.multiple_calls
    def sum_nums(a, b):
        print(a, b)
        return a + b
    print(sum_nums(3, 5)(5, 8)(8, 90)(50, 45).__return__)
    print(sum_nums(33, 51)(59, 84).__return__)
Take a look at the log:

    3 5
    5 8
    8 90
    50 45
    (8, 13, 98, 95)
    33 51
    59 84
    (84, 143)
The tuples are the return of all the function calls. This utility is very useful if you want to run various tests with one function without the need to rewrite it and get all the returns in one tuple.
The next decorator is `multiple_calls_list`, and it's very interesting too, because it makes to possible to make multiple calls but with different functions. Take a look at this code:

    def wow1(a, b):
        print(a, b)
        return a * b
    def wow2():
        print("rlly?")
        return 33
    @triceratopy.functions.multiple_calls_list(wow1, wow2)
    def wow(msg):
        print("wow", msg) 
    print(wow("hello")(5, 7)())
The code above doesn't use return by the fact that the last call returns a tuple containing all the function returns, just like `__return__`. This can be very useful too because you can chain function calls in one line and make easier to call functions that have an order and are related.
### Utilities
#### Dicts and objects setters and getters
**Dicts setters and getters**
Dictionary setters and getters make the task of setting unseted sub-values in keys much easier, using recursion to check and create each key with a sub-dictionary value, without the need to create each one of them. The methods to set and get are, respectively: `set_dict_index(dict, index, value` and `get_dic_index(dict, index)`.
##### Examples:
Dictionary setters and getters make the task of setting unseted sub-values in keys much easier, using recursion to check and create each key with a sub-dictionary value, without the need to create each one of them. The methods to set and get are, respectively: `set_dict_index(dict, index, value` and `get_dic_index(dict, index`.
##### Examples: 
    my_dict = {}
    triceratopy.utils.set_dict_index(my_dict, ('key1', 'keyr2', 'key3', 'a value'))
    #my_dict {'key1': {'key2: {'key3: 'a value'}}}
    
    triceratopy.utils.set_dict_index(my_dict, ('key1', 'keyr2', 'key4', 'another value')) 
    #would make {'key1': {'key2': {'key3': "a value", 'key4': "another value"}}}
    
This can be useful if you need to store the values in a path-like structure (example: you need to store in the `("/", "projects", "triceratopy")` the object `triceratopy_webpage` object). The other utility is the dictionary getter, that can get the dicionary value or sub-dictionary from the specified index. Example:
   
    my_dict = {}
    triceratopy.utils.set_dict_index(my_dict, ('key1', 'key2', 'key3', "a value"))
    #my_dict {'key1': {'key2: {'key3: 'a value'}}}
    
    triceratopy.utils.set_dict_index(my_dict, ('key1' ,'key2', 'key4', "another value")) 
    #would make {'key1': {'key2: {'key3: 'a value', 'key4': 'another value'}}}
    
    print(triceratopy.utils.get_dict_index(my_dict, ('key1', 'key2', 'key4')
    #prints "another value in the console
    print(triceratopy.utils.get_dict_index(my_dict, ('key1')
    #prints {'key2': {'key3': 'a value', 'key4': 'another value'}}
**Objects setters and getters**
Triceratopy also includes the object equivalent of the methods above, they are `set_obj_index` and `get_obj_index`, and work at the same way as the methods shown above, except for the fact that getting a key that contains an object as value will return that object, and not a sub-dictionary. They work exactly like the dict methods.

 

