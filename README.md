# City-Noise-Analysis--Hangzhou

## Tools
* Python
    * requests: connection
    * BeautifulSoup: for parsing
    * jieba: for parsing
    * pyecharts: for visualization using word_cloud and graph
* Source of data: http://www.info0571.com/hbjtdb/adv.html

## Intermediate Files
* wordcloud.txt
Generated from wordcloud_raw.txt, which is the result of running "cloud.py".
The keywords prefixed with "#" is "stop-words" manually tagged.


## User Manual

1. To get data containing keyword "噪音"(noise) between 2008-01-01 and 2020-01-01 from all newspapers, run the code below to write data into ./results.txt--the context we need.
```bash=
python payapa.py
```

2. To get the top-100 hotest keywords from all context, run:
```bash=
python cloud.py
```

3. To get the word-cloud like the picture below, please run the code below, and you'll get "Word_Cloud.html".
```bash=
python buildcloud.py
```
![](https://i.imgur.com/MjJsKai.png)

4. To get the relation-graph below, please run the code below, and you'll gt "graph.html".
```bash=
python network.py
```
![](https://i.imgur.com/NBVTN9F.png)
![](https://i.imgur.com/rJ6SEHH.png)
![](https://i.imgur.com/TCLcIQ9.png)
