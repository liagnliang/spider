#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
__title__=""
__author__="Administrator"
__mtime_="2018/5/18"
Fail until you fail again,this is how you succeed.

"""
import codecs

class DataOutput(object):

	def __init__(self):
		self.datas=[]

	def store_data(self,data):
		if data is None:
			return
		self.datas.append(data)

	def output_html(self):
		fout=codecs.open('baike.html','w',encoding='utf-8')
		fout.write("<html>")
		fout.write("<body>")
		fout.write("<table>")
		for data in self.datas:
			fout.write("<tr>")
			fout.write("<td>%s</td>"%data['url'])
			fout.write("<td>%s</td>"%data['title'])
			fout.write("<td>%s</td>"%data['summary'])
			fout.write("</tr>")
			self.datas.remove(data)
		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")
		fout.close()