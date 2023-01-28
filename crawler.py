#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://www.ptt.cc/bbs/Gossiping/index32944.html -> 2022.09.01 head
# https://www.ptt.cc/bbs/Gossiping/index33003.html -> 2022.09.02 head
# https://www.ptt.cc/bbs/Gossiping/index34775.html -> 2022.10.01 head
# https://www.ptt.cc/bbs/Gossiping/index36596.html -> 2022.11.01 head
# https://www.ptt.cc/bbs/Gossiping/index37701.html -> 2022.11.26 head
# https://www.ptt.cc/bbs/Gossiping/index37813.html -> 2022.11.26 tail
# https://www.ptt.cc/bbs/Gossiping/index38652.html -> 2022.12.01 head
import requests,  json
from bs4 import BeautifulSoup
from tqdm import tqdm
ptt = "https://www.ptt.cc/bbs/Gossiping/index"
pttcc = "https://www.ptt.cc"

def get_article(start,end):
    index = 1
    article_output, pushes_output = [], []
    for i in tqdm(range(start,end)):
        url = ptt + (str)(i) + '.html'
        r = requests.get(url,cookies={'over18':'1'})    
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.find_all('div',class_='title')
        # print(title)
        for t in tqdm(title):
            article_info = {}
            website = t.find('a')['href']
            site = pttcc + website
            res = requests.get(site,cookies={'over18':'1'})
            res.encoding = 'utf-8'
            art_soup = BeautifulSoup(res.text, 'html.parser')
            ### Get article info
            meta_data = art_soup.select('span.article-meta-value')
            # print(meta_data)
            if(len(meta_data) != 4):
                continue
            article_info['author'] = meta_data[0].text
            article_info['board'] = meta_data[1].text
            article_info['title'] = meta_data[2].text
            article_info['time'] = meta_data[3].text
            ### Get article content
            contain = art_soup.find(id = 'main-container')
            article_text = contain.text.split("--")[0]
            tmp = article_text.split("\n")[2:]
            # print(tmp)
            content = ""
            for i in tmp:
                if(len(i) < 4):
                    content += i + '\n'
                else:
                    if(i[:4] != 'http'):
                        content += i + '\n'
            article_info['content'] = content
            ### Get push
            pushes_info = []
            pushes = art_soup.find_all('div', class_="push")
            if (len(pushes) > 300):
                continue
            push_figure = {'推 ': 'like', '噓 ': 'dislike', '→ ': 'arrow'}
            for i in pushes:
                tmp = {}
                tmp['tag'] = push_figure[i.find('span',class_='push-tag').text]
                tmp['id'] = i.find('span',class_='push-userid').text
                tmp['content'] = i.find('span',class_='push-content').text
                s = (i.find('span',class_='push-ipdatetime').text).split(' ')
                for i in range(len(s)):
                    if(s[i] != ''):
                        tmp['ip'] = s[i] 
                        tmp['time'] = " ".join(s[i+1:])
                        tmp['time'] = tmp['time'][:-1]
                        break
                pushes_info.append(tmp)
            article_output.append(article_info)
            pushes_output.append(pushes_info)
    output = {}
    for i in range(len(article_output)):
        output[str(i)] = {}
        output[str(i)]['article'] = article_output[i]
        output[str(i)]['push'] = pushes_output[i]
    # print(output)
    with open('./data/2022_11_26_new.json','wb+') as pf:
    # with open('./data/test3.json','wb+') as pf:
        pf.write(json.dumps(output,indent=4,ensure_ascii=False).encode('utf-8'))

### Index may change day by day
get_article(37701,37813)
# get_article(37738,37739)

