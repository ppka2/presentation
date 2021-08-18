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

s = re.sub(r'[^\w\s]','',strc)


result = p.get_pinyin(s,' ')


result=re.sub(r'\d','',result)
word_total=["iu","ei","uan","ue","un","uo","ie","ong","eng","ang","an","uai","ing","uang","iang","ou","ua","ao","ui","in","iao","ian","iong","ai","en","sh","ch","zh"]
word_good=["iu","ei","ue","un","uo","ie","eng","ang","uai","ing","uang","iang","ou","ui","iao","iong","sh","ch","zh"]
word_bad=["uan","an","ao","in","ua","ai","en","ian","ong","ia"]
dictC={}
for i in word_good:
    dictC[i]=len(re.findall(i,result))

dictC["uan"]=len(re.findall(r"uan(?!g)",result))#排除掉uang
dictC["an"]=len(re.findall(r"(?<![iu])an(?!g)",result))#排除掉iang uang等
dictC["ao"]=len(re.findall(r"(?<!i)ao",result))#排除掉iao
dictC["in"]=len(re.findall(r"in(?!g)",result))#排除掉ing
dictC["ua"]=len(re.findall(r"ua(?![ni])",result))#排除掉uai uan
dictC["ai"]=len(re.findall(r"(?<!u)ai",result))#排除掉uai
dictC["en"]=len(re.findall(r"en(?!g)",result))#排除掉eng
dictC["ian"]=len(re.findall(r"ian(?!g)",result))#排除掉iang
dictC["ong"]=len(re.findall(r"(?<!i)ong",result))#排除掉iong
dictC["ia"]=len(re.findall(r"ia(?![no])",result))#排除掉ian
dict_total={}
for key,value in dictC.items():
    for i in range(len(key)):
        if key[i] in dict_total:
            dict_total[key[i]]+=value
        else:
            dict_total[key[i]]=value
print(dict_total)
dict_average=0
total=53475
for key,value in dictC.items():
    total-=(len(key)-1)*value
print(total/26)
#合并
# dictC["ong_iong"]=dictC["iong"]+dictC["ong"]
# del dictC["iong"]
# del dictC["ong"]
# dictC["ua_ie"]=dictC["ie"]+dictC["ua"]
# del dictC["ie"]
# del dictC["ua"]
# dictC["uai_ing"]=dictC["ing"]+dictC["uai"]
# del dictC["ing"]
# del dictC["uai"]
# dictC["ui_in"]=dictC["in"]+dictC["ui"]
# del dictC["in"]
# del dictC["ui"]
# dictC["uang_ian"]=dictC["ian"]+dictC["uang"]
# del dictC["ian"]
# del dictC["uang"]
label=[]
size=[]
dictC_sort=sorted(dictC.items(), key=lambda x: x[1])
for key,value in dictC_sort:
    label.append(key)
    size.append(value)

plt.bar(label,size)
for a, b, label in zip(label, size, size):
    plt.text(a, b,label, ha='center', va='bottom')
plt.show()