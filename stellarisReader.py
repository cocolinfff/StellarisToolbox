#dict = {'name':"xxx",'sub':{'add':1,'dec':-1}}
import re
import copy
import string
from eachFile import eachFile
def mergeDict(d1,d2):
    d2_keys_not_in_d1 = d2.keys() - d1.keys()
    d1_keys_not_in_d2 = d1.keys() - d2.keys()
    common_keys = d2.keys() & d1.keys()
    d={}
    for i in common_keys:
        if type(d1[i])==list and type(d2[i])!=list:
            d[i] = d1[i]+[d2[i]]
        else:
            d[i] = [d1[i],d2[i]]
    for i in d1_keys_not_in_d2:
        d[i] = d1[i]
    for i in d2_keys_not_in_d1:
        d[i] = d2[i]
    return d
class stringStream:
    def __init__(self,raw):
        self.raw=raw
        self.Maxlen=len(raw)
        self.pt=0
    def next(self):
        if self.pt==-1:
            return ''
        tmpReturn =self.raw[self.pt]
        self.pt=self.pt+1
        if (self.pt == self.Maxlen):
            self.pt = -1
        return tmpReturn
    def clear(self):
        self.pt==0




def stellarisRead(origin):
    dict={}
    key=[]
    value=[]
    txt=[]
    flag=0
    ignoreflag=0
    letter = origin.next()
    while(origin.pt>0):
        if ignoreflag==1 and letter != '\n':
            letter = origin.next()
            continue
        if ignoreflag==1 and letter == '\n':
            letter = origin.next()
            ignoreflag=0
            continue
        if letter == '#':
            ignoreflag = 1
        elif letter == '=':
            key=copy.deepcopy(txt)
            txt.clear()
            flag=1
        elif letter =='{':
            if flag==1:
                dict=mergeDict(dict,{"".join(key):stellarisRead(origin)})
                key.clear()
                flag=0
        elif letter =='}':
            if flag==1:
                value=copy.deepcopy(txt)
                dict=mergeDict(dict,{"".join(key):"".join(value)})
                key.clear()
                value.clear()
                txt.clear()
                flag=0
            break
        elif letter=='\n':
            if flag==1:
                value=copy.deepcopy(txt)
                dict=mergeDict(dict,{"".join(key):"".join(value)})
                key.clear()
                value.clear()
                txt.clear()
                flag=0
        elif letter==' ' or letter == '\t':
            pass
        else:
            txt.append(letter)

        letter = origin.next()

    return  dict

def stellarisLoad(f):
    rawDict = f.read()
    Dict = eval(rawDict)
    return Dict

def stellarisPrint(f,Dict,tab=0):
    for key,values in Dict.items():
        if type(values)==dict:
            for i in range(tab):
                f.write('\t')
            f.write(key + '= { \n')
            stellarisPrint(f,values,tab+1)
            for i in range(tab):
                f.write('\t')
            f.write('}\n')
        elif type(values)==list:
            for item in values:
                stellarisPrint(f,{key:item},tab)
        else:
            for i in range(tab):
                f.write('\t')
            f.write(key + ' = '+values+'\n')
def stellarisEach(filedir):
    dictMain = {}
    #print(eachFile(filedir))
    for fileName in eachFile(filedir):
        with open(fileName, 'r', encoding='UTF-8') as f:
            origin = stringStream(f.read())
            if origin.Maxlen<1:
                continue
            dictMain = mergeDict(dictMain, stellarisRead(origin))
    return dictMain
#from eachFile import eachFile
#mod1List=eachFile("C:\\Users\\16049\\Documents\\Paradox Interactive\\Stellaris\\mod\\ECI Local\\common\\pop_jobs")
#dictMain={}
#for fileName in mod1List:
#    with open(fileName,'r',encoding='UTF-8') as f:
#        origin=stringStream(f.read())
#        dictMain=mergeDict(dictMain,stellarisRead(origin))
#with open("D:\\output.txt",'w') as f:
#    f.write(str(dictMain))