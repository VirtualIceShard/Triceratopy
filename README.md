
# Triceratopy
_Currently under development_
Triceratopy is a python utilities module to make easier and simplier working with dictionaries, or even using capsules(_see capsules_), a way of using modules inside modules. 
### Utilitiesd
#### Dicts and objects setters and getters
**Dicts setters and getters**
Dictionary setters and getters make the task of setting unseted sub-values in keys much easier, using recursion to check and create each key with a sub-dictionary value, without the need to create each one of them. The methods to set and get are, respectively: `set_dict_index(dict, index, value` and `get_dic_index(dict, index`.
##### Examples:
    my_dict = {}
    triceratopy.set_dict_index(my_dict, ("key1","keyr2","key3", "a value"))
    #my_dict {'key1': {'key2:{'key3: "a value"}}}
    
    triceratopy.set_dict_index(my_dict, ("key1","keyr2","key4", "another value")) 
    #would make {'key1': {'key2:{'key3: "a value", 'key4': "another value"}}}
This can be useful if you need to store the values in a path-like structure (example: you need to store in the `("/", "projects", "triceratopy")` the object`triceratopy_webpage` object. The other utility is the dictionary getter, that can get the dicionary value or sub-dictionary from the specified index. Example:
   
    my_dict = {}
    triceratopy.set_dict_index(my_dict, ("key1","keyr2","key3", "a value"))
    #my_dict {'key1': {'key2:{'key3: "a value"}}}
    
    triceratopy.set_dict_index(my_dict, ("key1","keyr2","key4", "another value")) 
    #would make {'key1': {'key2:{'key3: "a value", 'key4': "another value"}}}
    
    print(triceratopy.get_dict_index(my_dict, ("key1", "key2", "key4")
    #prints "another value in the console
    print(triceratopy.get_dict_index(my_dict, ("key1")
    #prints {'key2': {'key3': 'a value', 'key4': 'another value'
**Objects setters and getters**
Triceratopy also includes the object equivalent of the methods above, they are `set_obj_index` and `get_obj_index`, and work at the same way as the methods shown above, except for the fact that getting a key that contains an object as value will return that object, and not a sub-dictionary.

>wow
>rly

