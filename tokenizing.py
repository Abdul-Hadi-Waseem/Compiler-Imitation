from lookuptable import lookuptable

def token_val(token):
    try:
        return lookuptable[token]
    except:
        lookuptable[token] = len(lookuptable)
        return lookuptable[token]
