#!/usr/bin/env python3

import time
import threading

class obj(object):
    pass

def simple_log(f):
    def funcwrapper(*args, **kargs):
        nArgs = args
        kArgs = kargs
        argsStr = []
        kargsStr = []
        willHaveComma = ""
        if len(args):
            for i in nArgs:
                if type(i) == str:
                    argsStr.append("\"" + str(i) + "\"")
                else:
                    argsStr.append(str(i))  
        if len (kArgs):
            willHaveComma = ","
            for k, v in kArgs.items ():
                if type(v) == str:
                    kargsStr.append("%s=%s" % ("\"" + k, v.__repr__() + "\""))
                else:
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