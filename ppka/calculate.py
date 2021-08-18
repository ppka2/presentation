
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
print(result[:10]) 
d = {} 
for x in result:
    if x!=" ":
        if x in d:
            d[x]+=1
        else:
            d[x]=1
df = pd.DataFrame.from_dict(d, orient='index',columns=['times'])
sumC=df.sum()
print(sumC)
means=df.mean()
print(df.mean())
df['times'] =df.apply(lambda x: x['times'] / means, axis=1)
print(df.mean())
print(df.var())
cf = configparser.ConfigParser()
cf.read("KMCounter.ini")
alph_dict={"a":30,"b":48,"c":46,"d":32,"e":18,"f":33,"g":34,"h":35,"i":23,"j":36,"k":37,"l":38,"m":50,"n":49,"o":24,"p":25,"q":16,"r":19,"s":31,"t":20,"u":22,"v":47,"w":17,"x":45,"y":21,"z":44}
sum=0
label=[]
size=[]

d_sub={'i': 3997, 'u': 2277, 'e': 2516, 'n': 5745, 'o': 2641, 'g': 2880, 'a': 4000, 's': 1371, 'h': 3575, 'c': 816, 'z': 1388}

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
d_sort=sorted(d.items(), key=lambda x: x[1])
for key,value in d_sort:
    label.append(key)
    size.append(value)
plt.bar(label,size)
for a, b, label in zip(label, size, size):
    plt.text(a, b,label, ha='center', va='bottom')
plt.show()

# for i in alph_dict.keys():
#     #print(i)
#     cf['20210816']['sc'+str(alph_dict[i])]=str(d[i])
#     sum+=d[i]

# cf['20210816']['keystrokes']=str(sum)
# print(sum)
# cf.write(open("KMCounter.ini", 'w'))


# sns.set()
# sns.heatmap(data=df,vmin=100,cmap = 'OrRd',vmax=1000,yticklabels=1)
# plt.xticks(fontsize=10) #x轴刻度的字体大小（文本包含在pd_data中了）
# plt.yticks(fontsize=10) #y轴刻度的字体大小（文本包含在pd_data中了）
# plt.title('title',fontsize=20) #图片标题文本和字体大小
# plt.show()