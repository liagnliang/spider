#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
__title__=""
__author__="Administrator"
__mtime_="2018/9/12"
Fail until you fail again,this is how you succeed.

"""
import threading
import time
import os
from contextlib import closing

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_vedio_url_list():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    locator_result = (By.XPATH, '//ul[contains(@class,"video-list")]/li/a')
    driver = webdriver.Chrome(executable_path="E:\webdrivers\chromedriver_win32\chromedriver.exe",
                              chrome_options=chrome_options)
    driver.get(URL)
    directory_title = driver.find_element_by_tag_name("h1").text
    if os.path.exists(BASE_DIRECTORY+directory_title)==False:
        os.mkdir(BASE_DIRECTORY+directory_title)
    links = driver.find_elements(*locator_result)
    for link in links:
        video_url_list.append(link.get_attribute('href'))
        video_title_list.append(link.find_element_by_class_name('title').text)
        print(link.get_attribute('href')+"-----"+link.find_element_by_class_name('title').text)
    print("获取所有视频地址列表")
    return directory_title
    driver.quit()


def download_vedio(vedio_dir,vedio_url, vedio_title):
    headers = {
        'client': 'web',
        'Referer': vedio_url,
        'User_Agent': 'Mozilla/5.0(Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
    }
    first_request_url = vedio_url.replace('play', 'video/play/url')
    r = requests.get(first_request_url, headers=headers)
    reality_vedio_url = r.json().get('data')
    r.close()
    store_directory = BASE_DIRECTORY + vedio_dir + "\\"
    print(vedio_title+" 开始下载,请稍后......")
    with closing(requests.get(reality_vedio_url)) as resp:
        with open(store_directory+vedio_title +'.mp4', 'wb') as f:
            f.write(resp.content)
    print("当前视频 " + vedio_title + " 下载完成！")


if __name__ == "__main__":
    URL = "http://www.icoolxue.com/album/show/360"
    BASE_DIRECTORY="e:\\vedio\\"
    video_url_list = []
    video_title_list = []
    list_locator=0
    thread_num=3 # 设置线程数量
    directory_title = get_vedio_url_list()
    if len(video_url_list)!=len(video_title_list):
        exit()
    while (list_locator < len(video_url_list)):
        thread_list = []
        for i in range(0,thread_num): # 每次创建三个线程
            if (list_locator+i) < len(video_url_list):
                # 创建线程th
                th = threading.Thread(target=download_vedio,
                                      args=(directory_title, video_url_list[list_locator], video_title_list[list_locator]))
                thread_list.append(th)
                list_locator = list_locator + 1
        for th in theard_list:
            th.setDaemon(True)
            th.start()
		for th in theard_list:
            th.join()

    print("所有视频下载完成！！！")
