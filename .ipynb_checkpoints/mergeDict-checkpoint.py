def mainMerge(d1,d2):
    d2_keys_not_in_d1 = d2.keys() - d1.keys()
    d1_keys_not_in_d2 = d1.keys() - d2.keys()
    common_keys = d2.keys() & d1.keys()
    d = {}
    for i in common_keys:
        if type(d1[i])==dict and type(d2[i])==dict:
            d[i]=mainMerge(d1[i],d2[i])
        elif type(d1[i])==str and type(d2[i])==str:
            d[i]=d1[i]
        elif type(d1[i])==list and type(d2[i])==list:
            d[i]=d1[i]+d2[i]
        elif type(d1[i]) == list and type(d2[i]) != list:
            d[i]=d1[i]+[d2[i]]
        elif type(d1[i]) != list and type(d2[i]) == list:
            d[i]=[d1[i]]+d2[i]
    for i in d1_keys_not_in_d2:
        d[i] = d1[i]
    for i in d2_keys_not_in_d1:
        d[i] = d2[i]
    return d

def mainMergeSub(D):
    for key,values in D.items():
        if key[0:8]=='scripted_':
            pass
        # to do