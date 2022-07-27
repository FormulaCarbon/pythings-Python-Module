def test():
    print('Test Complete. Pythings DictTools working.')
    return 'DictTools Working'

def j2dict(obj, remove=None):
    import json
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    if remove != None:
        text = text.replace(remove, '')
    return text
def list2dict(key, content):
    looper = 0
    l2d = {}
    if len(key) == len(content):
        while looper <= len(key) - 1:
            l2d[key[looper]] = content[looper]
            looper = looper + 1
        return l2d.copy()
    else:
        raise RuntimeError('Length of keys is not equal to length of values. Key length is '+len(key)+', and values length is '+ len(content)+'.')
