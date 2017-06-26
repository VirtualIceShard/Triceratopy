#!/usr/bin/env python3

class obj(object):
    pass

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




