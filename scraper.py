# -*- coding utf-8 -*-
"""

Created by gsiadak @ 12:13 PM 3/30/16

"""
import time
from lxml import html as LH
import requests
import pandas as pd


def main():
    page = requests.get('http://pimpmykeyboard.com/key-status/')
    tree = LH.fromstring(page.content)
    list = ([td.text_content() for td in tree.xpath('//td')])

    newlist=[]
    i = 0
    while i <= len(list):
        if i >= len(list):
            break
        templist=[]
        templist.append(list[i])
        templist.append(list[i+1])
        templist.append(list[i+2])
        newlist.append(templist)
        i += 3

    df = pd.DataFrame(newlist)
    df.to_csv('out.csv', index=False, header=False)




# COMPUTATIONALTIMING #
start_time = time.time()
main()
end_time = time.time()
print("Computation Time: %g seconds" % round((end_time - start_time), 3))
