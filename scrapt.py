#-*- coding: UTF-8 -*- 
import urllib
import urllib2
import re
import os

class Spider:

	def getHtml(self, url):
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		html = response.read()
		return html

	def getImg(self, html):
		reg = r'<img class="BDE_Image".*?src="(.*?)"'
		imgre = re.compile(reg) #把正则表达式reg编译成一个对象
		imglist = re.findall(imgre,html) #读取html中包含imgre的数据
		return imglist

	def saveImgs(self,imglist,md):
		x=0
		for imgurl in imglist:
			splitPath = imgurl.split('.')
			fTail = splitPath.pop()
			if len(fTail)>3:
				fTail = "jpg"
			fileName = md + "/" + str(x) + "." + fTail
			self.saveImg(imgurl,fileName)
			x+=1

	def saveImg(self,imageURL,fileName):
	    u = urllib.urlopen(imageURL)
	    data = u.read()
	    f = open(fileName, 'wb')
	    f.write(data)
	    print "正在悄悄保存图片",fileName
	    f.close()

	def mkdir(self,path):
		isExists=os.path.exists(path)
		if not isExists:
	            # 如果不存在则创建目录
	            print "偷偷新建了名字叫做",path,'的文件夹'
	            # 创建目录操作函数
	            os.makedirs(path)
	            return True
	        else:
	            # 如果目录存在则不创建，并提示目录已存在
	            print "名为",path,'的文件夹已经创建成功'
	            return False

spider = Spider()
html = spider.getHtml("http://tieba.baidu.com/p/4454914245")
imgs = spider.getImg(html)
md = "f:/bigbang/gd"
spider.mkdir(md)
spider.saveImgs(imgs,md)




