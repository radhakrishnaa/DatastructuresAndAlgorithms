def permutation(str, pr):
    if len(str) == 0 :
        print(pr)
    else:
        for i in range(len(str)):
            rem = str[:i]+str[i+1:]
            #pr += str[i]
            permutation(rem, pr+str[i])

permutation("abc","")