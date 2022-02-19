import os
import sys


def openSheeshfile(filename):
    """
    Args: filename [string] name of the sheesh file
    returns file object
    """
    try:
        foo = open(filename,"r+")
        return foo
    except:
        # check if file exists
        if not os.path.exists(filename):
            print("ERR: File does not exists")
            FileNotFoundError()
            sys.exit(1)

def getFileSize(filename):
    try:
        file_size = os.path.getsize(filename)
        return file_size
    except:
        # check if file exists
        if not os.path.exists(filename):
            print("ERR: File does not exists")
            FileNotFoundError()
            sys.exit(1)