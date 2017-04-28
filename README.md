# Triceratopy
_Currently under development_(*version 0.1.0*)  
Triceratopy is a collection of utilities, that includes a variety of decorators and functions to make some tasks easier or even to organize your code better. Triceratopy includes:  
- **Function decorator utilities(simple logs, multiple calls in one line, multiple calls sequence, set interval, set timeout)**
- **Objects and dictionaries setters and getters using an index thats automatically do the work of creating sub-dicionaries and objects**
- **A multi-use flatten that accepts lists, tuples and dictionaries**
- **The use of capsules(_see capsules_) to make code organization easier and create the possibility to separate modules into "sub-modules" _(triceratopy uses capsules to store its own functions, organizing them in sections that you will see below)_**
### Function decorators (triceratopy.function)
##### **simple log**
Triceratopy contains a decorator to simple function logging, it's called *simple log*. This decorator returns the fucntion arguments, the execution start and end time and the return, simple informations that are very useful when you need to log something simple and less complex.
    
**Use:** `@triceratopy.function.simple_log`  
  
Here's an example:

    @triceratopy.functions.simple_log
    def say_smth(num, str, add="wow", add2=3):
        print(num,str,add,add2)
        return num
    cps1 = capsule1()
    print(cps1.sum(3,8))
    print(cps1.wow)
    say_smth(3,"hey", add2=55)
    say_smth(34,"nop")
    say_smth(23, "uhu", add="hah", add="rly?")

Here's the log:

    [17:11]Calling say_smth(3,hey,add2=55)
    [17:11]Started running
    3 hey wow 55
    [17:11]Ended
    [17:11]Returned: 3
    [17:11]Calling say_smth(34,nop)
    [17:11]Started running
    34 nop wow 3
    [17:11]Ended
    [17:11]Returned: 34
    [17:11]Calling say_smth(23,uhu,add='hah',add2='rly?')
    [17:11]Started running
    23 uhu hah rly?
    [17:11]Ended
    [17:11]Returned: 23
___
##### **multiple calls and multiple calls list**
These two decoratos add a very interesting behavior to the function. The first, `multiple_calls` makes possible to call a function as many times as you want in one line, then you can get the return of all the calls as a _tuple_ by using `__return__`.
  
**Use:** `@triceratopy.function.multiple_calls`  
  
See below:

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
The tuples are the return of all the function calls. This method is very useful if you want to run various tests with one function without the need to rewrite it and get all the returns in one tuple.
The next decorator is `multiple_calls_list`, and it's very interesting too, because it makes to possible to make multiple calls but with different functions. The first function to be called is the decorated one.
  
**Use:** `@triceratopy.function.multiple_calls_list(function2, function3)`  
  
Take a look at this code:

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
### Utilities (triceratopy.utils)
#### Triceratopy's flatten
Triceratopy includes a version of the `flatten(list)` method that also supports tuples and vene dictionaries. The function can also make _tuples_ with _lists_ inside or _lists_ with _tuples_ inside into flat _lists_ or _tuples_. Using _flatten_ is simple, because it's used the same way as before:  
`flatten(list_tuple_or_dict)`  
  
_Note: using flatten on dictionaries will ignore empty sub-dicionaries. If you want them to be present, use the key argument `show_empty_subdict = True`_  
  
Example of use:  
  
    ar = [4, [5, "*"], [7,9, ["+", [90,7], "&",":"]]]
    print(flatten (ar))
    #[4, 5, '*', 7, 9, '+', 90, 7, '&', ':']
    
    print (flatten ((3, (8, "==", (83)),88)))
    #(3, 8, '==', 83, 88)
    
    print (flatten ((4, "&&", [";;", 4, (69, "&&:"), 99], (5, 8))))
    #(4, '&&', ';;', 4, 69, '&&:', 99, 5, 8)
    
    print (flatten ([4, "::", (8, 9, [";;"])],["^^", 8]))
    #[4, '::', 8, 9, ';;']
    print (flatten ({"oww":{"rlt":67, "k":{"foo3":88, "e": {}}}, "n": 990},\
    show_empty_subdict=True))
    #{'rlt': 67, 'foo3': 88, 'e': {}, 'n': 990}
    print (flatten ({"oww":{"rlt":67, "k":{"foo3":88, "e": {}}}, "n": 990}))
    #{'rlt': 67, 'foo3': 88, 'n': 990}
___
#### Dicts and objects setters and getters
**Dicts setters and getters**
Dictionary setters and getters make the task of setting unseted sub-values in keys much easier, using recursion to check and create each key with a sub-dictionary value, without the need to create each one of them. The methods to set and get are, respectively: `set_dict_index` and `get_dic_index`.  
  
**Use:** `set_dict_index(dic, index, value`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`get_dict_index(dict, index)`  
  
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
  
**Use:** `set_obj_index(obj, index, value`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`get_dobj_index(obj, index)`  
___
## Capsules
Triceratopy uses capsules to organize it's code. Capsules are just like objects, but they follow a structure inspired in the _Nodejs_ modules structure. Declaring a capsule is very simple, and using capsules makes your code more organized, also it makes possible to have all organized setions in one module, different from the packages. Capsules are defined as functions, as you can see below (both _description_ and _version_ are optional):

    @triceratopy.capsule(name="MyCapsule", description="optional", version="2.01")
    def my_capsule(name=None, capsule=None, exports=None):
    #Very similar to Node.js, but instead of module we have capsule
        exports.sum_nums = lambda x,y: x + y
        def wow():
            print("wow"
            print("Im impressed!")
        exports.wow = wow
        
#### To get the capsule object just do:

    capsule1 = my_capsule()
    #Then
    print(capsule1.sum_ums(3, 9))
    #12
    capsule1.wow()
    #wow
    #Im impressed

_Note_: Capsules export by default the variable `__info__`, that is a dicitonary containing the capsule's name, version and description.
    
    print(capsule1.__info__)
    #{'name': 'MyCapsule', 'description': 'optional', 'version': '2.01'}

### Importing methods and variables from capsule
If you don't want to use the capsule object reference to call any method or any variable, you can _import_ these elements from the capsule by using `import_from(capsule, "method1", "mehod2, "var1".....)`  
  
_Note1_: This is different from Python's import, keep in mind that this does not work with `triceratopy.capsule` , for example. The reason is that `capsule` is not inside any capsule, it's inside a module.  
  
_Note2_: Your editor may consider an error calling any imported variable or method because they are defined in the runtime, so the editor can't figure out that it's going to be imported, don't worry, it's not an error.  
  
_Note 3_: If you still have a variable with the same name as the one that will be imported the import_from will show a warning in the console, and that variable will not be created.  
  
#### Examples of use:  

**Importing `flatten` and `set_dict_index`  using `import_from`**

    triceratopy.import_from(triceratopy.utils, "flatten", "set_dict_index")
    print(flatten([3, (5, 7, [8])]))
    #[3, 5, 7, 8]

**Importing `multiple_calls` and `simple_log`**

    triceratopy.import_from(triceratopy.function, "simple_log", "multiple_calls")

    @simple_log
    def say_smth(num, str, add="wow", rlly=3):
        print(num,str,add,rlly)
        return num
    say_smth(3,"hey", rlly=55)
    
    """
    [10:36]Calling say_smth(3,hey,rlly=55)
    [10:36]Started running
    3 hey wow 55
    [10:36]Ended
    [10:36]Returned: 3
    """
    @multiple_calls
    def sum_nums(a, b):
        print(a, b)
        return a + b
    print(sum_nums(3, 5)(5, 8)(8, 90)(50, 45).__return__)
    
    """
    30
    3
    30
    3 5
    5 8
    8 90
    50 45
    (8, 13, 98, 95)
    """
    
 

