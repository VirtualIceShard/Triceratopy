# Triceratopy
_Currently under development_ (*version 0.1.0*)  
Triceratopy is a collection of utilities, that includes a variety of decorators and functions to make some tasks easier or even to organize your code better. Triceratopy includes:  
- **Function decorator utilities(simple logs, multiple calls in one line, multiple calls sequence, set interval, set timeout)**
- **Objects and dictionaries setters and getters using an index thats automatically do the work of creating sub-dicionaries and objects**
- **A multi-use flatten that accepts lists, tuples and dictionaries**
### Function decorators (triceratopy.functiond)
##### **simple log**
Triceratopy contains a decorator to simple function logging, it's called *simple log*. This decorator returns the fucntion arguments, the execution start and end time and the return, simple informations that are very useful when you need to log something simple and less complex.
    
**Use:** `@triceratopy.functiond.simple_log`  
  
Here's an example:

    @triceratopy.functiond.simple_log
    def say_smth(num, strng, add="wow", add2=3):
        print(num,strng,add,add2)
        return num
    say_smth(3,"hey", add2=55)
    say_smth(34,"nop")
    say_smth(23, "uhu", add="hah", add="rly?")

Here's the log:

	[17:51]Calling say_smth(3,"hey",rlly=55)
	[17:51]Started running
	3 hey wow 55
	[17:51]Ended
	[17:51]Returned: 3
	[17:51]Calling say_smth(34,"nop")
	[17:51]Started running
	34 nop wow 3
	[17:51]Ended
	[17:51]Returned: 34
	[17:51]Calling say_smth(23,"uhu","add='hah'","rlly='rly?'")
	[17:51]Started running
	23 uhu hah rly?
	[17:51]Ended
	[17:51]Returned: 23
___
##### **multiple calls and multiple calls list**
These two decoratos add a very interesting behavior to the function. The first, `multiple_calls` makes possible to call a function as many times as you want in one line, then you can get the return of all the calls as a _tuple_ by using `_return`.
  
**Use:** `@triceratopy.functiond.multiple_calls`  
  
See below:

    @triceratopy.functionds.multiple_calls
    def sum_nums(a, b):
        print(a, b)
        return a + b
    print(sum_nums(3, 5)(5, 8)(8, 90)(50, 45)._return)
    print(sum_nums(33, 51)(59, 84)._return)
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
  
**Use:** `@triceratopy.functiond.multiple_calls_list(function2, function3)`  
  
Take a look at this code:

    def wow1(a, b):
        print(a, b)
        return a * b
    def wow2():
        print("rlly?")
        return 33
    @triceratopy.functionds.multiple_calls_list(wow1, wow2)
    def wow(msg):
        print("wow", msg) 
    print(wow("hello")(5, 7)())
The code above doesn't use return by the fact that the last call returns a tuple containing all the function returns, just like `_return`. This can be very useful too because you can chain function calls in one line and make easier to call functions that have an order and are related.
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

### PyEzCmd (triceratopy.pyezcmd)
*PyEzCmd* is a module that contains the `PyEzCmdConsole` class to help building simple consoles in an easy way. *PyEzCmd* can be used to create bots or simple command line programs.
##### Creating the console
To create a *PyEzCmd* console, you just need to invoke `PyEzCmdConsole()`, which has 2 key arguments: `out` and `prefix`. The key argument named `out` is the output stream used by the command to write, and has `sys.stdout` as default value. The other argument `prefix`, is the prefix used in your commands, and has an empty string as default value.

Example of console creating:

    import triceratopy
    my_console = triceratopy.pyezcmd.PyEzCmdConsole(prefix="!")

##### Creating commands for the console
To create a command for the console, you need to have a function that represents the command, just like this:

    def cmd_help(args, out=None, objs=None):
    if args:
        out.write("Displaying help for: " + args[0] + "\n")
        return "Success"
    else:
        out.write("Usage: help [command]\n")
        return "Needs one arg, use shown"
        
The command must return a message when it's called. The first argument is a tuple containing the arguments for that command. There's a key argument called `objs` too, which can contain a list of objects needed to be passed to the command function (like an object representing the who ran the command).
After creating the function, you need a word representing the command, like *help* or *print*. When calling the command, the user will need to type *prefix* + *word* to call the command. There's 2 other optional arguments, `min_args` and `max_args`, these two are the limit of arguments that the command will have. If you want infinite args set `max_args` to *-1*.


To creating a new command, invoke `add_cmd` on the *PyEzCmdCOnsole* object.  
Example:
    
    cmd_console.add_cmd("help", cmd_help, min_args=0, max_args=1)

If thres's another command using the same word, the funciton will return `False`.
##### Calling the command
Calling the command is very simple, you just need to invoke `cmd()` on the *PyEzCmdCOnsole* object. The arguments of the function are `cmdstr` and `objs`. The fisrt is the whole command line, containing the prefix, word, and arguments, which will be split by the funcion. The second was explained before, and is optional, with default value to `None`. The function will return a tuple with a length of 2. The first item can be `True`, if everything went ok, or `False`, if an error ocurred. Possible erros can be the number of arguments or the inexistent word on the commands. The second item will be the error message or a message returned by the command function.  
Example of use:

    print(cmd_console.cmd("!help make")[1])
    #Success (function command was called)
    print(cmd_console.cmd("!help")[1])
    #Needs one arg, use shown (function command was called)
    print(cmd_console.cmd("!help make do")[1])
    #Args above max args: 2 (error)
    print(cmd_console.cmd("!hel")[1])
    #Command not found! (error)
    print(cmd_console.cmd("help")[1])
    #Invalid prefix! (error)


