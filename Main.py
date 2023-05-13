import stellarisReader
import mergeDict
#f=open("D:\\output.txt",'r',encoding='UTF-8')
#MainDict=stellarisReader.stellarisLoad(f)
#
#wf=open("D:\\print.txt",'w',encoding='UTF-8')
#stellarisReader.stellarisPrint(wf,MainDict)

mod1dict=stellarisReader.stellarisEach("D:\\mod1")
print(mod1dict)
mod2dict=stellarisReader.stellarisEach("D:\\mod2")
print(mod2dict)
Dict=mergeDict.mainMerge(mod1dict,mod2dict)
print(Dict)