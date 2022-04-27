import os
import sys
import pandas as pd

def openSheeshfile(filename):
    """
    Args: filename [string] name of the sheesh file
    returns file object
    """
    try:
        foo = open(filename, "r+")
        return foo
    except:
        # check if file exists
        if not os.path.exists(filename):
            print("ERR: File does not exists")
            FileNotFoundError()
            sys.exit(1)


def getFileSize(filename):
    """
    Args: filename [string] name of the sheesh file
    returns file filesize
    """
    try:
        file_size = os.path.getsize(filename)
        return file_size
    except:
        # check if file exists
        if not os.path.exists(filename):
            print("ERR: File does not exists")
            FileNotFoundError()
            sys.exit(1)

def extract_data(filename):
    """
    Args: filename [string] name of the sheesh file
    returns dataframe of data
    """
    try:
        data = pd.read_csv(filename, sep="\t")
        return data
    except:
        # check if file exists
        if not os.path.exists(filename):
            print("ERR: File does not exists")
            FileNotFoundError()
            sys.exit(1)