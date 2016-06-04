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
		imgre = re.compile(reg) #��������ʽreg�����һ������
		imglist = re.findall(imgre,html) #��ȡhtml�а���imgre������
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
	    print "�������ı���ͼƬ",fileName
	    f.close()

	def mkdir(self,path):
		isExists=os.path.exists(path)
		if not isExists:
	            # ����������򴴽�Ŀ¼
	            print "͵͵�½������ֽ���",path,'���ļ���'
	            # ����Ŀ¼��������
	            os.makedirs(path)
	            return True
	        else:
	            # ���Ŀ¼�����򲻴���������ʾĿ¼�Ѵ���
	            print "��Ϊ",path,'���ļ����Ѿ������ɹ�'
	            return False

spider = Spider()
html = spider.getHtml("http://tieba.baidu.com/p/4454914245")
imgs = spider.getImg(html)
md = "f:/bigbang/gd"
spider.mkdir(md)
spider.saveImgs(imgs,md)




