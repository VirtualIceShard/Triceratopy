#!/usr/bin/env python3
import triceratopy
class simpleob(object):
    pass
@triceratopy.capsule("wow")
def capsule1 (name=None, capsule=None, exports=None):
    exports.sum = lambda x,y: x + y
    exports.wow = "wow"
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

@triceratopy.functions.multiple_calls
def sum_nums(a, b):
    print(a, b)
    return a + b
print(sum_nums(3, 5)(5, 8)(8, 90)(50, 45).__return__)
print(sum_nums(33, 51)(59, 84).__return__)

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