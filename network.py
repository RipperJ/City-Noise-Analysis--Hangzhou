import random
from itertools import combinations as cbn
from pyecharts import options as opts
from pyecharts.charts import Graph

# read 57 keywords
f = open("wordcloud.txt", "r", encoding="utf-8")
n = []
size = []
ls = {}
l = f.readlines()
for i in l:
    if i.startswith("#") == True:
        continue
    n.append(i.split()[0])
    size.append(i.split()[1])
for i in cbn(n, 2):
    ls[i] = 0
# now ls has all the pairs, it's a dict of len: 57 * 56 / 2
f.close()

f = open("results.txt", "r", encoding="utf-8")
l = f.readlines()
count = 0
for i in l:
    # every paragraph in the whole context
    for j in cbn(n, 2):
        if j[0] in i and j[1] in i:
            ls[j] += 1
    if count % 1000 == 0:
        print("count: ", str(count))
    count += 1
# print(sorted(ls.items(), key=lambda x:x[1], reverse=True))
# ls = sorted(ls.items(), key=lambda x:x[1], reverse=True)

# start to draw
nodes = []
for i in range(len(n)):
    nodes.append({
        "name": n[i],
        "symbolSize": int(size[i]) / 100,
        "itemStyle": {"normal": {"color": "#"+str(hex(random.randint(0x6, 0xA)))[2:]+str(hex(random.randint(0x6, 0xA)))[2:]+str(hex(random.randint(0x6, 0xA)))[2:]}}
        })
print(len(nodes))
links = []
# for i in nodes:
#     for j in nodes:
#         links.append({"source": i.get("name"), "target": j.get("name")})
for i in ls.items():
    if i[1] >= 200:
        links.append({
            "source": i[0][0],
            "target": i[0][1],
            # "itemStyle": {"normal": {"color": "#FFF"}}
            })

c = (
    Graph()
    .add("",
        nodes,
        links,
        repulsion = 8000,
        # layout="circular",
        linestyle_opts=opts.LineStyleOpts(width=0.5, opacity=0.5),
        is_draggable=True,
        )
    .set_global_opts(title_opts=opts.TitleOpts(title="Internal_Relation--Noise Context"))
    .render("graph.html")
)
