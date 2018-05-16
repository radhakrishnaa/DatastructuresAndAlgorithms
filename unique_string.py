import string

def unique(str):
    d = dict.fromkeys(string.ascii_lowercase, "")
    j = 0
    for i in str:
        if len(d[i]) == 0:
            d[i] += i
        else:
            print "not unique"
            return False
    for k in d:
        if len(d[k]) > 1:
            j += 1
    if j == 1:
        print "unique"
        return True

unique("abca")
