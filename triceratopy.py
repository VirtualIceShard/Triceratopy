import time
def simplelog(f):
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
#!/usr/bin/env python3

''' 
  Copyright 2017 VirtualIceShard
  
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 
     http://www.apache.org/licenses/LICENSE-2.0
 
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
'''

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
            return f.capsule.exports
        return inner_wrapper
    return outer_wrapper
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
