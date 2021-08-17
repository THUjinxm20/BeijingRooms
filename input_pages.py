
import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd
from multiprocessing.pool import ThreadPool
from datetime import datetime
import random
import time
import os.path
import threading

def print_process_info(big_district, middle_district, page):
    # Use a breakpoint in the code line below to debug your script.
    timestr = datetime.now().strftime('%Y%m%d%H%M')
    print(f'...............[{timestr}][{big_district}][{middle_district}][{page}] processing ...............')

def check_site_blocked() :
    timestr = datetime.now().strftime('%Y%m%d%H%M')
    print('Time[' + timestr +']. Url is blocked. Verify the site. ')
    delay_time = random.uniform(5, 10)
    delay_time = round(delay_time, 2)
    time.sleep(delay_time)

# get 17 big district name and url
def get_big_district ():
    big_district_list = pd.DataFrame({'district':[]})
    while 1:
        url_base = "https://bj.ke.com/ershoufang/dongcheng"
        url = requests.get(url_base)
        html = url.content
        soup = BeautifulSoup(html, "html.parser")

        idx = 0
        big_url_list = [] #big district url
        big_name = [] #big district name

        for distLink in soup.find_all('a', "CLICKDATA"):
            href = distLink.get('href')
            text = distLink.get_text('href')
            big_name.append(text)
            big_url_list.append('https://bj.ke.com' + href)
            idx += 1
            # new_df = pd.DataFrame([[1, href]], columns=['idx', 'district'])
            # df_big_district_list.append(new_df)

        df_big_district_url_list = pd.DataFrame(big_url_list, columns=['big_district_url'])
        df_big_district_url_list = df_big_district_url_list[0:17]
        df_big_name = pd.DataFrame(big_name,columns = ['big_district_name'])
        df_big_name= df_big_name[0:17]

        df_big_name_pinyin = pd.DataFrame(df_big_name,columns = ['big_district_pinyin'])

        for i in range(0,17,1):
            df_big_name_pinyin.iloc[i] = (df_big_district_url_list['big_district_url'].iloc[i][29:-1])

        #df_big_name_pinyin = pd.DataFrame(columns = ['big_district_pinyin'])
        #df_big_name_pinyin = df_big_district_url_list['big_district_url'][29:-1]


        #df_big = pd.concat([df_big_name,df_big_district_url_list],axis = 1)
        # print(df_big_district_list)

        return df_big_name, df_big_district_url_list,df_big_name_pinyin


df_big_name, df_big_district_url_list,df_big_name_pinyin = get_big_district()
print(df_big_name)
print(df_big_district_url_list)
print(df_big_name_pinyin)
#print(df_big_district_url_list['big_district_url'].iloc[1][29:-1])

#middle = get_middle_district(df_big_district_url_list)
#print(middle)

url_base = "https://bj.ke.com/ershoufang/dongcheng"
url = requests.get(url_base)
html = url.content
soup = BeautifulSoup(html, "html.parser")

atags = soup.select("#beike > div.sellListPage > div.m-filter > div.position > dl > dd > div > div ")[1].select('a')

middle_href = pd.DataFrame(columns=['middle_href'])
middle_text = pd.DataFrame(columns=['middle_text'])

count = int(0)
for an in atags:
    href = an['href']
    text = an.get_text()
    middle_href.loc[count] = [href]
    middle_text.loc[count] = [text]
    print(href)
    print(text)
    count+=1

print(middle_href)
print(middle_text)

