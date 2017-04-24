#!/usr/bin/env python3
import triceratopy

@triceratopy.capsule("wow")
def capsule1 (name=None, capsule=None, exports=None):
    exports.sum = lambda x,y: x + y
    exports.wow = "wow"
@triceratopy.simplelog
def saySmth(num, str, add="wow", rlly=3):
    print(num,str,add,rlly)
cps1 = capsule1()
print(cps1.sum(3,8))
print(cps1.wow)
saySmth(3,"hey", rlly=55)
saySmth(34,"nop")
saySmth(23, "uhu", add="hah", rlly="rly?")
simple_dict = {}
triceratopy.set_dict_index(simple_dict, ("wow", "much", "doge"), 3)
triceratopy.set_dict_index(simple_dict, ["wow", "much", "doge2"], 99)
triceratopy.set_dict_index(simple_dict, ["wow", "much", "doge3", "doge4","doge5"], lambda: print(4))
triceratopy.set_dict_index(simple_dict, ["wow", "much", "doge3", "doge4","doge6"], lambda x: x + 2)
print(triceratopy.get_dict_index(simple_dict, ["wow"]))
print(triceratopy.get_dict_index(simple_dict, ("wow", "much", "doge3", "doge4","doge6"))(5))
print(simple_dict)