#!/usr/bin/env python3

import sys

class obj(object):
    pass

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
            