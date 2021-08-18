'''
统计word文字材料各个字母的次数
'''
import re
import configparser
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from xpinyin import Pinyin
import docx
from docx import Document
p = Pinyin()
path = "1.docx"
document = Document(path)#导入word
strc=""
for paragraph in document.paragraphs:
    strc+=paragraph.text #提取文字字符串


s = re.sub(r'[^\w]','',strc)#正则匹配除去标点

result = p.get_pinyin(s,' ')#以空格为分界符 文字转拼音
result=re.sub(r'\d','',result)# 正则匹配除去数字
d = {} 
for x in result: #各个字母计数
    if x!=" ":
        if x in d:
            d[x]+=1
        else:
            d[x]=1 


df = pd.DataFrame.from_dict(d, orient='index',columns=['times'])
means=df.mean()#平均数
df['times'] =df.apply(lambda x: x['times'] / means, axis=1)#缩小平均数倍，使平均数为1
print("以下为全拼输入法字母缩小后的平均数")
print(df.mean())#
print("以下为全拼输入法字母平均数为1的方差")
print(df.var())#




cf = configparser.ConfigParser()#编写ini文件 为了热力图可视化
cf.read("C.ini")
alph_dict={"a":30,"b":48,"c":46,"d":32,"e":18,"f":33,"g":34,"h":35,"i":23,"j":36,"k":37,"l":38,"m":50,"n":49,"o":24,"p":25,"q":16,"r":19,"s":31,"t":20,"u":22,"v":47,"w":17,"x":45,"y":21,"z":44} #ini文件中的对应关系
sum=0
for i in alph_dict.keys():
    #print(i)
    cf['20210816']['sc'+str(alph_dict[i])]=str(d[i])#更改ini文件
    sum+=d[i] 

cf['20210816']['keystrokes']=str(sum)
print("总共的键盘击打次数为",sum)
cf.write(open("C.ini", 'w'))
d_sort=sorted(d.items(), key=lambda x: x[1])
label=[]
size=[]
for key,value in d_sort:
    label.append(key)
    size.append(value)
plt.bar(label,size)
for a, b, label in zip(label, size, size):
    plt.text(a, b,label, ha='center', va='bottom')
plt.show()
# sns.set()
# sns.heatmap(data=df,vmin=100,cmap = 'OrRd',vmax=1000,yticklabels=1)
# plt.xticks(fontsize=10) #x轴刻度的字体大小（文本包含在pd_data中了）
# plt.yticks(fontsize=10) #y轴刻度的字体大小（文本包含在pd_data中了）
# plt.title('title',fontsize=20) #图片标题文本和字体大小
# plt.show()