# -*- coding: utf-8 -*-
import urllib
import urllib2
import re

class QSBK:
	def __init__(self):
		self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		self.headers = { 'User-Agent' : self.user_agent }
		self.page = 1
		self.stories = []
		self.enable = False

	def getPage(self,page):
		try:
			url = "http://www.qiushibaike.com/hot/page/" + str(page)
			request = urllib2.Request(url,headers = self.headers)
			respond = urllib2.urlopen(request)
			pageCode = respond.read().decode('utf-8')
			return pageCode
			
		except urllib2.URLError, e:
			if hasattr(e,"code"):
				print e.code
				return None
			if hasattr(e,"reason"):
				print e.reason
				return None

	def getPageItems(self,page):
		pageCode = self.getPage(page)
		if not pageCode:
			print"页面加载失败"
			return None
		
		pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?<h2>(.*?)</h2>.*?<div.*?class'+
						'="content".*?>(.*?)</div>.*?<div.*?class="stats.*?class="number">(.*?)</i>',re.S)
		items = re.findall(pattern,pageCode)
		pageStories = []
		for item in items:
			pageStories.append([item[0].strip(),item[1].strip(),item[2].strip()])
		return pageStories

	def loadPage(self):
		if self.enable:
			if len(self.stories) < 2:
				pageStories = self.getPageItems(self.page)
				if pageStories:
					self.stories.append(pageStories)
					self.page += 1
	
	def getOneStory(self,page,pageStories):
		for story in pageStories:
			Input = raw_input()
			self.loadPage()
			if Input == "Q":
				self.enable = False
				return 
			print u"第%d页\t发布人:%s\t\n%s\n赞:%s\n" % (page,story[0],story[1],story[2])

	def start(self):
		print u"正在读取糗事百科,按回车查看新段子，Q退出"
		self.enable = True
		self.loadPage()
		nowPage = 0
		while self.enable:
			if len(self.stories)>0:
				pageStories = self.stories[0]
				nowPage += 1
				del self.stories[0]
				self.getOneStory(nowPage,pageStories)

spider = QSBK()
spider.start()
  