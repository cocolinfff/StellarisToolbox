<!--
 * @Author: Colin colin_1@sjtu.edu.cn
 * @Date: 2024-06-13 14:11:15
 * @LastEditors: Colin colin_1@sjtu.edu.cn
 * @LastEditTime: 2024-06-13 14:30:40
 * @FilePath: \StellarisToolbox\README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
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
```
```
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
<span title="A= { 
	sub= { 
		add = 3
	}
	sub= { 
		add = 5
	}
	name = xxx
	pos = yy
}" style="border-bottom:1px dotted">sdfsdf</span>