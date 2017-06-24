#!/usr/bin/env python3
"""
Below you can see the uses of Triceratopy
"""
import triceratopy
class simpleob(object):
    pass
@triceratopy.capsule("wow")
def capsule1 (name=None, capsule=None, exports=None):
    exports.sum = lambda x,y: x + y
    exports.wow = "wow"

triceratopy.import_from(triceratopy.function, "simple_log", "multiple_calls")

@simple_log
def say_smth(num, str, add="wow", rlly=3):
    print(num,str,add,rlly)
    return num
cps1 = capsule1()
print(cps1.sum(3,8))
print(cps1.wow)
say_smth(3,"hey", rlly=55)
say_smth(34,"nop")
say_smth(23, "uhu", add="hah", rlly="rly?")
simple_dict = {}
triceratopy.utils.set_dict_index(simple_dict, ("wow", "much", "doge"), 3)
triceratopy.utils.set_dict_index(simple_dict, ["wow", "much", "doge2"], "99")
triceratopy.utils.set_dict_index(simple_dict, ["wow", "much", "doge3", "doge4","doge5"], lambda: print(4))
triceratopy.utils.set_dict_index(simple_dict, ["wow", "much", "doge3", "doge4","doge6"], lambda x: x + 2)
print(triceratopy.utils.get_dict_index(simple_dict, ["wow"]))
print(triceratopy.utils.get_dict_index(simple_dict, ("wow", "much", "doge3", "doge4","doge6"))(5))
print(simple_dict)
so = simpleob()
triceratopy.utils.set_obj_index(so, ("wow", "much", "dogee"), 3)
triceratopy.utils.set_obj_index(so, ("wow", "much", "dogee2"), 30)
print(triceratopy.utils.get_obj_index(so, ("wow", "much", "dogee2")))
print(so.wow.much.dogee)
print(so.wow.much.dogee2)
def printargs(f):
    def wrapper(*args, **kargs):
        if args:
            print("args", args)
        if kargs:
            print("key args", kargs)
        return f(*args, **kargs)
    return wrapper
@multiple_calls
def sum_nums(a, b):
    print(a, b)
    return a + b
print(sum_nums(3, 5)(5, 8)(8, 90)(50, 45)._return)
print(sum_nums(33, 51)(59, 84)._return)

def wow1(a, b):
    print(a, b)
    return a * b
def wow2():
    print("rlly?")
    return 33
@triceratopy.function.multiple_calls_list(wow1, wow2)
def wow(msg):
    print("wow", msg) 
print(wow("hello")(5, 7)())


@triceratopy.function.thread_execute
def onetoten(end):
    for i in range(1, 11):
        print(i)
    print(end)
onetoten("#")
print("seriously? one to ten?")
triceratopy.import_from(triceratopy.utils, "flatten", "set_dict_index")
print(flatten([3, (5, 7, [8])]))
print(triceratopy.utils.__info__)
kvpd = triceratopy.utils.dict_keyval_str("wow=3;  heynow=imarockstar;")
print(kvpd)
kvp_file = triceratopy.utils.dict_keyval_config("test_keyval.config")
print(kvp_file)

def cmd_help(args, out=None, objs=None):
    if args:
        out.write("Displaying help for: " + args[0] + "\n")
        return "Success"
    else:
        out.write("Usage: help [command]\n")
        return "Needs one arg, use shown"
cmd_console = triceratopy.pyezcmd.PyEzCmdConsole(prefix="!")
cmd_console.add_cmd("help", cmd_help, min_args=0, max_args=1)
print(cmd_console.cmd("!help make")[1])
print(cmd_console.cmd("!help")[1])
print(cmd_console.cmd("!help make do")[1])
print(cmd_console.cmd("!hel")[1])
print(cmd_console.cmd("help")[1])
