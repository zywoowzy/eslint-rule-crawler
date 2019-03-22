# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from lxml import etree
import re

if __name__ == '__main__':
    req = Request('https://eslint.org/docs/rules/', headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    bf = BeautifulSoup(html, features='html.parser')
    et = etree.HTML(html)
    rules = []
    elems = et.xpath('//table[@class="rule-list table table-striped"]/tbody'
    '/tr/td[1]/span[@title="recommended"]/../../td[3]/p/a')
    fixs = et.xpath('//table[@class="rule-list table table-striped"]/tbody'
    '/tr/td[1]/span[@title="recommended"]/../../td[2]')
    infos = et.xpath('//table[@class="rule-list table table-striped"]/tbody'
    '/tr/td[1]/span[@title="recommended"]/../../td[4]/p')
    print('total num: ', len(elems))
    for each in elems:
        rule = each.text
        rules.append(rule)
        print('"' + rule + '": 1,')
    print()
    for i in range(len(elems)):
        rule = elems[i].text
        info = infos[i].text
        print(rule + ': ' + info)

    # print(rules)