
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
for paragraph in document.paragraphs:
    strc+=paragraph.text

s = re.sub(r'[^\w]','',strc)

result = p.get_pinyin(s,' ') 
result=re.sub(r'\d','',result)


"""
映射关系
"""
table=[["iang","y"],["uang","m"],["ang","q"],["uan","x"],["ian","m"],["an","p"],["uai","t"],["ua","s"],["iong","n"],["iao","l"],["ing","t"],["ong","n"],["eng","r"],["en","c"],["ui","k"],["ai","f"],["in","k"],["ao","g"],["ie","s"],["ou","b"],["ei","h"],["un","z"],["iu","j"],["ue","d"],["uo","o"],["sh","o"],["ch","a"],["zh","v"],["ia","w"]]

for i in table: #应用映射关系
    result=re.sub(i[0],i[1],result)
# with open("1.txt","w") as f:
#     f.write(result)

d = {} 
for x in result:#新的输入法下计数
    if x!=" ":
        if x in d:
            d[x]+=1
        else:
            d[x]=1
print("改进输入法下的各个字母次数")
print (d)  


df = pd.DataFrame.from_dict(d, orient='index',columns=['times'])
means=df.mean()
df['times'] =df.apply(lambda x: x['times'] / means, axis=1)
print("以下为全拼输入法字母缩小后的平均数")
print(df.mean())#
print("以下为全拼输入法字母平均数为1的方差")
print(df.var())#

cf = configparser.ConfigParser()
cf.read("C.ini")
alph_dict={"a":30,"b":48,"c":46,"d":32,"e":18,"f":33,"g":34,"h":35,"i":23,"j":36,"k":37,"l":38,"m":50,"n":49,"o":24,"p":25,"q":16,"r":19,"s":31,"t":20,"u":22,"v":47,"w":17,"x":45,"y":21,"z":44}
sum=0
for i in alph_dict.keys():
    #print(i)
    cf['20210816']['sc'+str(alph_dict[i])]=str(d[i])
    sum+=d[i]

cf['20210816']['keystrokes']=str(sum)
cf.write(open("C.ini", 'w'))#写入ini文件

print("总共的键盘击打次数为",sum)
# sns.set()
# sns.heatmap(data=df,vmin=100,cmap = 'OrRd',vmax=1000,yticklabels=1)
# plt.xticks(fontsize=10) #x轴刻度的字体大小（文本包含在pd_data中了）
# plt.yticks(fontsize=10) #y轴刻度的字体大小（文本包含在pd_data中了）
# plt.title('title',fontsize=20) #图片标题文本和字体大小
# plt.show()