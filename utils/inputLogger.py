import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import traceback


class InputLogger(object):
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

    def append(self, inp):
        inp_str = ""
        for inp_tok, line in inp:
            inp_str += " " + inp_tok
        if not isinstance(inp_str, str):
            try:
                inp_str = str(inp_str)
            except:
                traceback.print_exc()
            else:
                print(inp_str)

                self.file.write(inp_str + "\n")
                self.file.flush()
        else:
            print(inp_str)
            self.file.write(inp_str + "\n")
            self.file.flush()

    def close(self):
        if self.file is not None:
            self.file.close()
