#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
__title__=""
__author__="Administrator"
__mtime_="2018/5/16"
Fail until you fail again,this is how you succeed.

"""
import requests
class HtmlDownloader(object):

	def download(self,url):
		if url is None:
			return None
		headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
				   'Accept-Encoding': 'gzip, deflate, sdch, br',
				   'Accept-Language': 'zh-CN,zh;q=0.8',
				   'Cache-Control': 'max-age=0',
				   'Connection': 'keep-alive',
				   'Cookie': 'BAIDUID=15939B8CC064BCF11CC51522F62B020C:FG=1; BIDUPSID=15939B8CC064BCF11CC5152                  2F62B020C; PSTM=1526891357; PSINO=3; H_PS_PSSID=1422_21087_26432_22159; BDORZ=FFFB88E999                  055A3F8A630C64834BD6D0; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1526891380; Hm_lpvt_55b5                  74651fcae74b0a9f1cf9c8d7c93a=1526894344',
				   'Host': 'baike.baidu.com',
				   'Referer': 'https://baike.baidu.com/item/%E4%BA%9A%E6%88%90%E9%B8%9F',
				   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)                   Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400',
				   'X-Requested-With': 'XMLHttpRequest'}
		r=requests.get(url,headers=headers)
		if r.status_code==200:
			r.encoding='utf-8'
			return r.text
		return None