'''
计算 去除了多字符后各个字母的频次
'''
import re
import configparser
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from xpinyin import Pinyin
p = Pinyin() 
import docx
from docx import Document
path = "1.docx"
document = Document(path)
strc=""
for paragraph in document.paragraphs:#读取汉字字符串
    strc+=paragraph.text

s = re.sub(r'[^\w]','',strc)#排除标点符号

result = p.get_pinyin(s,' ') #汉字转拼音 ，以空格隔开

result=re.sub(r'\d','',result)#排除 数字

d = {} 
for x in result: #各个字母计数
    if x!=" ":
        if x in d:
            d[x]+=1
        else:
            d[x]=1

df = pd.DataFrame.from_dict(d, orient='index',columns=['times'])

sum=0
label=[]
size=[]

d_sub={'i': 3997, 'u': 2277, 'e': 2516, 'n': 5745, 'o': 2641, 'g': 2880, 'a': 4000, 's': 1371, 'h': 3575, 'c': 816, 'z': 1388} #根据calculate_yunmu.py中得到的排除的各个字母的次数

#排除字母
d["i"]-=d_sub["i"]
d["u"]-=d_sub["u"]
d["e"]-=d_sub["e"]
d["n"]-=d_sub["n"]
d["o"]-=d_sub["o"]
d["g"]-=d_sub["g"]
d["a"]-=d_sub["a"]
d["c"]-=d_sub["c"]
d["z"]-=d_sub["z"]
d["h"]-=d_sub["h"]
d["s"]-=d_sub["s"]
d_sort=sorted(d.items(), key=lambda x: x[1])#排序
for key,value in d_sort:
    label.append(key)
    size.append(value)
plt.bar(label,size)#得到了排除掉多字符后的条形图
for a, b, label in zip(label, size, size):
    plt.text(a, b,label, ha='center', va='bottom')
plt.show()





# sns.set()
# sns.heatmap(data=df,vmin=100,cmap = 'OrRd',vmax=1000,yticklabels=1)
# plt.xticks(fontsize=10) #x轴刻度的字体大小（文本包含在pd_data中了）
# plt.yticks(fontsize=10) #y轴刻度的字体大小（文本包含在pd_data中了）
# plt.title('title',fontsize=20) #图片标题文本和字体大小
# plt.show()