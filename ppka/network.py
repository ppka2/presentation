#声母表以及韵母表
list_shimu=["b","p","m","f","d","t","n","l","g","k","h","j","q","x","zh","ch","sh","r","z","c","s","w","y"]
list_yunmu=["a","o","e","i","u","v","ia","ai","ei","ui","ao","ou","iu","ie","ve","er","an","en","in","un","vn","ang","eng","ing","ong"]

#各个韵母对应的声母
dictC={"iu":["d","j","l","m","n","q","x"],
        "ei":["b","d","ei","f","g","h","l","m","n","p","sh","w","z","zh"],
        "uan":["ch","c","d","g","h","j","k","l","n","q","r","s","sh","t","x","y","zh","z"],
        "ue":["j","l","n","q","x","y"],
        "un":["ch","c","d","g","h","j","k","l","n","q","r","s","sh","t","x","y","zh","z"],
        "uo":["ch","c","d","g","h","j","k","l","n","r","s","sh","t","zh","z"],
        "ie":["b","d","j","l","m","n","p","q","t","x"],
        "ong":["ch","c","d","g","h","k","l","n","r","s","t","y","zh","z"],
        "eng":["b","c","ch","d","eng","f","g","h","k","l","m","n","p","r","s","sh","t","w","z","zh"],
        "ang":["ang","b","c","ch","d","f","g","h","k","l","m","n","p","r","s","sh","t","w","y","z","zh"],
        "an":["an","b","c","ch","d","f","g","h","j","k","l","m","n","p","q","r","s","sh","t","w","x","y","z","zh"],
        "uai":["ch","g","h","k","sh","zh"],
        "ing":["b","d","j","l","m","n","p","q","t","x","y"],
        "uang":["ch","g","h","k","sh","zh"],
        "iang":["j","l","n","q","x"],
        "ou":["ch","c","d","f","g","h","k","l","m","n","ou","p","r","s","sh","t","y","zh","z"],
        "ua":["ch","g","h","k","sh","zh"],
        "ao":["ao","b","c","ch","d","g","h","k","l","m","n","p","r","s","sh","t","y","zh","z"],
        "ui":["ch","c","d","g","h","k","r","s","sh","t","z","zh"],
        "in":["b","j","l","m","n","p","q","x","y"],
        "iao":["b","d","j","l","m","n","p","q","t","x"],
        "ian":["b","d","j","l","m","n","p","q","t","x"],
        "iong":["j","q","x"],
        "ai":["ai","b","c","ch","d","g","h","k","l","m","n","p","sh","s","t","w","z","zh"],
        "en":["b","c","ch","d","en","f","g","h","k","m","n","p","r","s","sh","w","z","zh    `"],
        "ia":["j","d","l","q","x"]
}
nodeL=[]
edgeL=[]
LC=["uai","iong","ua"]
#LC=[]
for key,value in dictC.items():
    for key1,value1 in dictC.items():
        if key!=key1 and key not in LC and key1 not in LC:
            a = [x for x in value if x in value1] #两个列表表都存在
            if len(a)==0:
                if key not in nodeL:
                    nodeL.append(key)
                    nodeL.append(key1)
                if [key,key1] not in edgeL and [key1,key] not in edgeL:
                    edgeL.append([key,key1])
# print(edgeL)
# print(nodeL)
import networkx as nx
# 创建空的网格
G=nx.Graph()
# 添加节点
G.add_nodes_from(nodeL)

# 添加连线
G.add_edges_from(edgeL)
# 绘制网络图
nx.draw_networkx(G,pos=nx.circular_layout(G),with_labels=True,node_color='lightblue',
                 linewidths=4,
                 edge_color='black',style='-',
                 font_size=10,font_color='black',font_family='SimHei')
import matplotlib.pyplot as plt
plt.show()
