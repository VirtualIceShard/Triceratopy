#!/usr/bin/env python3


import time
import threading
import inspect
import sys

def capsule(name, description="No description provided",\
      version="0.0.1"):
    def outer_wrapper (f):
        def inner_wrapper (*args, **kargs):
            class exports_return (object):
                pass
            class capsule_return(object):
                def __init__(self, name, desc, ver):
                    self.name = name
                    self.descritpion = desc
                    self.version = ver
            class exports_return (object):
                def __init__(self):
                    pass
            f.capsule = capsule_return(name, description, version)
            f.capsule.exports = exports_return ()
            f (name=name, capsule=f.capsule, exports=f.capsule.exports)
            f.capsule.exports.__info__ = {"name": name, "description": description, "version": version}
            return f.capsule.exports
        return inner_wrapper
    return outer_wrapper
def import_from(capsule_exports, *args):
    def check_exists(name, module):
        try:
            module.__dict__[a]
            return True
        except KeyError:
            return False
    for a in args:
        if not check_exists(a, inspect.getmodule(inspect.stack()[1][0])):
            for attr, val in capsule_exports.__dict__.items():
                if attr == a:
                    inspect.getmodule(inspect.stack()[1][0]).__dict__[a] = val
        else:
            print("Already used names. Can't import.")
class obj(object):
    pass
@capsule("functiond", description="a collection of function decorators utils", version="0.0.1")
def functiond_capsule(name=None, capsule=None, exports=None):
    def simple_log(f):
        def funcwrapper(*args, **kargs):
            nArgs = args
            kArgs = kargs
            argsStr = []
            kargsStr = []
            willHaveComma = ""
            if len(args):
                for i in nArgs:
                    argsStr.append(str(i))  
            if len (kArgs):
                willHaveComma = ","
                for k, v in kArgs.items ():
                    kargsStr.append("%s=%s" % (k, v.__repr__()))
            print ("[%02i:%02i]Calling %s" %(time.localtime ().tm_hour, time.localtime ().tm_min,\
            str(f.__name__ + "(" + ",".join(argsStr) + willHaveComma + ",".join(kargsStr)) + ")"))
            print("[%02i:%02i]Started running" %(time.localtime ().tm_hour, time.localtime ().tm_min))
            toret = f (*args, **kargs)
            print("[%02i:%02i]Ended" %(time.localtime ().tm_hour, time.localtime ().tm_min))
            print ("[%02i:%02i]Returned: %s" % (time.localtime ().tm_hour, time.localtime ().tm_min, toret.__repr__()))
            return toret
        return funcwrapper
    
    def multiple_calls(f):
        def wrapper(*args, **kargs):
            func = f
            def ff(*args1, **kargs1):
                ff._return = list(ff._return)
                ff._return.append(func(*args1, **kargs1))
                ff._return = tuple(ff._return)
                return ff
            ff._return = ()
            ff(*args, **kargs)
            return ff
        return wrapper
    def multiple_calls_list(*f_args):
        def outer_wrapper(f):
            def inner_wrapper(*args, **kargs):
                func = f
                def ff(*args1, **kargs1):
                    ff._return = list(ff._return)
                    ff._return.append(ff.__nextf__[0](*args1, **kargs1))
                    ff._return = tuple(ff._return)
                    if len(ff.__nextf__) > 1:
                        ff.__nextf__.pop(0)
                    else:
                        return ff._return
                    return ff
                ff.__nextf__ =  [f] + list(f_args)
                ff._return = ()
                ff(*args, **kargs)
                return ff
            return inner_wrapper
        return outer_wrapper
    def thread_execute(f):
        def wrapper(*args, **kargs):
            ExecuteThread(f, args, kargs).start()
            return None
        return wrapper
    class ExecuteThread(threading.Thread):
        def __init__(self, f, args, kargs):
            self.f = f
            self.args = args
            self.kargs = kargs
            threading.Thread.__init__(self)
        def run(self):
            self.f(*self.args, **self.kargs)
    
    class ThreadExecutorTime (threading.Thread):
        def __init__(self, f, args, kargs, ms, repeat):
            self.f = f
            self.args = args
            self.kargs = kargs
            self.ms = ms/1000
            self.repeat = repeat
            threading.Thread.__init__(self)
        def run (self):
            if self.repeat:
                while True:
                    self.f (*self.args, **self.kargs)
                    time.sleep (self.ms)
            else:
                time.sleep (self.ms)
                self.f (*self.args, **self.kargs)
    def set_interval(interval):
        def outer_wrapper (f):
            def inner_wrapper (*args, **kargs):
                ThreadExecutorTime (f, args, kargs, interval, True).start ()
                return None
            return inner_wrapper
        return outer_wrapper
    
    def set_timeout(interval):
        def outer_wrapper (f):
            def inner_wrapper (*args, **kargs):
                ThreadExecutorTime (f, args, kargs, interval, False).start ()
                return None
            return inner_wrapper
        return outer_wrapper     
    exports._name__ = name
    exports.simple_log = simple_log
    exports.multiple_calls = multiple_calls
    exports.multiple_calls_list = multiple_calls_list
    exports.set_interval = set_interval
    exports.set_timeout = set_timeout
    exports.thread_execute = thread_execute
@capsule("utils", description="utilities to make easier the task of programming", version="0.0.1")
def utils_capsule(name=None, capsule=None, exports=None):   
    def set_obj_index (objref, index, value, recursive=False, rlist=[]):
        index = list(index)
        if not recursive:
            obret = objref
            rlist = []
            rlist.append(index[0])
            obret.__dict__[index [0]] = set_obj_index (objref, index [1:], value, recursive=True, rlist=rlist)
            return obret
        else:
            if len (index) > 0:
                if get_obj_index (objref, rlist, show_has_returned=True)[1]:
                    subret = get_obj_index (objref, rlist, show_has_returned=True)[0]
                else:
                    subret = obj()
                rlist.append(index[0])
                subret.__dict__ [index [0]] = set_obj_index (objref, index [1:], value, recursive=True, rlist=rlist)
                return subret
            else:
                return value
    def get_obj_index (objref, index, recursive=False, show_has_returned = False):
        index = list(index)
        try:
            if len(index) > 0:
                return get_obj_index(objref.__dict__[index[0]], index[1:], show_has_returned = show_has_returned)
            else:
                if show_has_returned:
                    return (objref, True)
                else:
                    return objref
        except KeyError:
            if show_has_returned:
                return (None, False)
            else:
                return None
    
    def set_dict_index (objref, index, value, recursive=False, rlist=[]):
        index = list(index)
        if not recursive:
            obret = objref
            rlist = []
            rlist.append(index[0])
            obret[index [0]] = set_dict_index (objref, index [1:], value, recursive=True, rlist=rlist)
            return obret
        else:
            if len (index) > 0:
                if get_dict_index (objref, rlist, show_has_returned=True)[1]:
                    subret = get_dict_index (objref, rlist, show_has_returned=True)[0]
                else:
                    subret = {}
                rlist.append(index[0])
                subret [index [0]] = set_dict_index (objref, index [1:], value, recursive=True, rlist=rlist)
                return subret
            else:
                return value
    def get_dict_index (objref, index, recursive=False, show_has_returned = False):
        index = list(index)
        try:
            if len(index) > 0:
                return get_dict_index(objref[index[0]], index[1:], show_has_returned = show_has_returned)
            else:
                if show_has_returned:
                    return (objref, True)
                else:
                    return objref
        except KeyError:
            if show_has_returned:
                return (None, False)
            else:
                return None
    def flatten (target, show_empty_subdict = False):
        def flat_array (arr):    
            arr2 = []
            for i in arr:
                if isinstance (i, list) or isinstance (i, tuple):
                    arr2 += flatten (i)
                else: 
                    arr2.append (i)
            return arr2
        
        def flat_tuple (tup):
            arr2 = []
            for i in tup:
                if isinstance (i, list) or isinstance (i, tuple):
                    arr2 += flatten (i)
                else:
                    arr2.append (i)
            return tuple(arr2)
        def flat_dict (dic, ses):
            dic2 = {}
            for i, v in dic.items ():
                if isinstance (v, dict) and (bool (v) or not ses):
                    for j, k in flat_dict (v, ses).items ():
                        dic2 [j] = k
                else:        
                    dic2 [i] = v
            return dic2
        if isinstance(target, list):
            return flat_array(target)
        elif isinstance (target, tuple):
            return flat_tuple (target)
        elif isinstance (target, dict):
            return flat_dict (target, show_empty_subdict)
    def dict_keyval_str(kvpstr, equals="=", val_end=";", strip=True, replace_newline=True):
        ret = {}
        if replace_newline:
            kvpstr = kvpstr.replace("\n", "")
        kv_pairs = kvpstr.split(val_end)
        for kvp in kv_pairs:
            if kvp:
                if strip:
                    k, v = list(map(lambda x: x.strip(), kvp.strip().split(equals)))
                else:
                    k, v = list(map(lambda x: x.strip(), kvp.split(equals)))
                ret[k] = v
        return ret
    def dict_keyval_config(configf, equals="=", val_end=";", strip=True):
        cflines = []
        with open(configf) as cfile:
            flines = cfile.read().split("\n")
            for fl in flines:
                if not fl.startswith(val_end):
                    cflines.append(fl)
        return dict_keyval_str("".join(cflines), equals=equals, val_end=val_end, strip=strip)
    exports._name__ = name
    exports.get_obj_index = get_obj_index
    exports.set_obj_index = set_obj_index
    exports.get_dict_index = get_dict_index
    exports.set_dict_index = set_dict_index
    exports.flatten = flatten
    exports.dict_keyval_str = dict_keyval_str
    exports.dict_keyval_config = dict_keyval_config
@capsule("pycmd", description="Command utilities to make easier create commands inside a python program",\
         version="0.0.1")
def pyezcmd_capsule(name=None, capsule=None, exports=None):
    class  PyEzCmdConsole(object):
        def __init__(self, out=sys.stdout, prefix=""):
            self.cmds = {}
            self.out = out
            self.prefix = prefix
        def cmd(self, cmdstr, objs=None):
            args = cmdstr.split(" ")[1:]
            if self.prefix:
                try:
                    cmds = cmdstr.split(" ")[0].split(self.prefix)[1]
                except IndexError:
                    return (False, "Invalid prefix!")
            else:
                cmds = cmdstr.split(" ")[0]
            try:
                cmdob = self.cmds[cmds]
            except KeyError:
                return (False, "Command not found!")
            if len(args) < cmdob.min_args:
                return (False, "Args below min args: " + str(len(args)))
            if not cmdob.inf_params:
                if len(args) > cmdob.max_args:
                    return (False, "Args above max args: " + str(len(args)))
            return (True,  cmdob.cmdf(tuple(args), out=self.out, objs=objs))
        def add_cmd(self, word, cmdf, min_args=0, max_args=-1):
            try:
                self.cmds[word]
            except KeyError:
                self.cmds[word] = self.PyEzCmdCommand(word, cmdf, min_args=min_args,\
                                                 max_args=max_args)
                return True
            return False
        class PyEzCmdCommand(object):
            def __init__(self, word, cmdf, min_args=0, max_args=-1):
                self.cmdf = cmdf
                self.min_args = min_args
                self.max_args = max_args
                if max_args == -1:
                    self.inf_params = True
                else:
                    self.inf_params = False
            
    exports.PyEzCmdConsole = PyEzCmdConsole
   
functiond = functiond_capsule()
utils = utils_capsule()
pyezcmd = pyezcmd_capsule()