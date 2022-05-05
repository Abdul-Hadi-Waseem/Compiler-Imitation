import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import traceback


class Logger(object):
    """Save training process to log file with simple plot function."""

    def __init__(self, fpath, resume=False):
        self.file = None
        self.resume = resume
        if os.path.isfile(fpath):
            if resume:
                self.file = open(fpath, "a")
            else:
                self.file = open(fpath, "w")
                self.file.truncate()
        else:
            self.file = open(fpath, "w")

    def append(self, stack):
        stack_str = ""
        for stack_tok in stack:
            stack_str += " " + stack_tok
        if not isinstance(stack_str, str):
            try:
                stack_str = str(stack_str)
            except:
                traceback.print_exc()
            else:
                print(stack_str)

                self.file.write(stack_str + "\n")
                self.file.flush()
        else:
            print(stack_str)
            self.file.write(stack_str + "\n")
            self.file.flush()

    def close(self):
        if self.file is not None:
            self.file.close()
