#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
__title__=""
__author__="Administrator"
__mtime_="2018/5/16"
Fail until you fail again,this is how you succeed.

"""
import re
import urlparse
from bs4 import BeautifulSoup

class HtmlParser(object):
	def parser(self,page_url,html_cont):
		if page_url is None or html_cont is None:
			return
		soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
		new_urls=self._get_new_urls(page_url,soup)
		new_data=self._get_new_data(page_url,soup)
		return new_urls,new_data

	def _get_new_urls(self,page_url,soup):
		new_urls=set()
		links=soup.find_all('a',href=re.compile(r'/item/.*'))
		for link in links:
			new_url=link['href']
			#拼接成完整网址
			new_full_url=urlparse.urljoin(page_url,new_url)
			new_urls.add(new_full_url)
		return new_urls

	def _get_new_data(self,page_url,soup):
		data={}
		data['url']=page_url
		title=soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
		data['title']=title.get_text()
		summary=soup.find('div',class_='lemma-summary')
		data['summary']=summary.get_text()
		return data