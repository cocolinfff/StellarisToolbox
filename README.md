# StellarisToolbox
## 群星mod开发工具箱,for python  
  
刚开始摸，定位是类似于json包的一个paradox script导入/导出/解包库  
现阶段实现的功能：格式化导入,格式化导出  

----

## Examples:
##### origin mod txt
```
A = {
    name="xxx"
    pos = "yy"
    sub = {
         add= 3
    }
sub = {
         add= 5
    }
}

```
##### Code 
```
mod1dict=stellarisReader.stellarisEach("D:\\mod1") 
# to read all the files in the dir and subdir

print(mod1dict)


{'A': {'sub': [{'add': '3'}, {'add': '5'}], 'name': '"xxx"', 'pos': '"yy"'}}
```
##### Print Code and Print files
```
with open("D:\\test.txt",'w',encoding='UTF-8') as f:
    stellarisReader.stellarisPrint(f,mod1dict)
```
```
A= { 
	sub= { 
		add = 3
	}
	sub= { 
		add = 5
	}
	name = "xxx"
	pos = "yy"
}

```
