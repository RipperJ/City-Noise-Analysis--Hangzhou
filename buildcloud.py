from pyecharts import WordCloud

f = open("wordcloud.txt", "r", encoding="utf-8")
l = f.readlines()
name = []
value = []
for i in l:
    if i.startswith("#") == True:
        continue
    name.append(i.split()[0])
    value.append(i.split()[1])
# myWordCloud = WordCloud("Word Cloud", width = 1000, height = 640)
# myWordCloud.add("", name, value, word_size_range=[20, 100])
# print(myWordCloud)

def wordcloud_build() -> WordCloud:
    c = (
        WordCloud("Word Cloud", width = 1000, height = 640)
        .add("", name, value, word_size_range=[20, 100])
        # .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-基本示例"))
        .render('./Word_Cloud.html')
    )
    return c

wordcloud_build()
