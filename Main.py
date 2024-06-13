import stellarisReader
import mergeDict
import local
#f=open("D:\\output.txt",'r',encoding='UTF-8')
#MainDict=stellarisReader.stellarisLoad(f)
#
#wf=open("D:\\print.txt",'w',encoding='UTF-8')
#stellarisReader.stellarisPrint(wf,MainDict)
def write_title_span(title,content):
    return '<span title='+content+''' style="border-bottom:1px dotted">'''+title+'</span>\n'
civic_dict=stellarisReader.stellarisEach("E://lqz//git//Ethics-Civics-Infinity-new//common//governments//civics")
#print(civic_dict.keys())
local_dict=local.local_dict("E://lqz//git//Ethics-Civics-Infinity-new//localisation")
safe_local_dict=lambda x:local_dict[x] if x in local_dict and type(x)!= dict else x
def dict_local_dict(d,f):
    normal_dict={'authority':'政体',
                 'potential':'前置条件',
                 'random_weight':'随机权重',
                 'possible':'需求',
                 'has_ethic':'拥有思潮',
                 'modifier':'修正',}
    safe_normal_dict=lambda x:normal_dict[x] if x in normal_dict else x
    for x in d :
        f.write(safe_normal_dict(x)+':')
        if type(d[x])==dict:
            f.write('{')
            dict_local_dict(d[x],f)
            #f.write('}\n')
            return 
        elif type(d[x])==list:
            f.write('\n')
            for item in d[x]:
                if type(item)==dict:
                    return dict_local_dict(item,f)
                else:
                    f.write('   '+safe_local_dict(item)+'\n')
            f.write('\n')
        else:
            f.write('   '+safe_local_dict(d[x])+'\n')
with open('test.md','w',encoding='UTF-8') as f:
    for civic in civic_dict:
        #f.write() #png
        if civic_dict[civic]=={}:
            continue
        #print(civic,civic_dict[civic],'\n\n')
        if 'is_origin' in civic_dict[civic]:
            continue

        f.write(write_title_span(safe_local_dict(civic),civic))

        for item in civic_dict[civic]:
            dict_local_dict({item:civic_dict[civic][item]},f)
        #f.write(write_title_span())
        #print(civic_dict[civic])
#mod2dict=stellarisReader.stellarisEach("D:\\mod2")
#print(mod2dict)
#Dict=mergeDict.mainMerge(mod1dict,mod2dict)
#print(Dict)
