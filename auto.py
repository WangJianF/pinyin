# -*- coding: utf-8 -*-

import pinyin, os, shutil
from pinyin._compat import u

# 在此添加需要屏蔽的图片
unCopy = ("选择场次界面","选择场次界面-注释","登录界面","登录界面-加载","个人信息界面","个人信息界面-注释","底分数集","加载界面","弹窗标注","弹窗效果图","主界面", "主界面-注释","金币钻石数值")

assetsDir = "assets"
targetDir = "target"

plistDir = "plistDir"
packPngCmdStr = "TexturePacker --format cocos2d --size-constraints NPOT --opt RGBA8888 --data %s.plist --sheet %s.png %s"

def shouldCopy(names):
	if names[1] == '.txt':
		return False
	else:
		for x in unCopy:
			if x == names[0].decode('gb2312').encode('utf-8'):
				return False
	return names

def travelDir(srcDir, dscDir):
	for oName in os.listdir(srcDir):
		srcName = os.path.join(srcDir, oName)
		if os.path.isdir(srcName):
			pName = pinyin.get(oName.decode('gb2312').encode('utf-8') , format="strip")
			tName = os.path.join(dscDir, pName)
			os.mkdir(tName)
			travelDir(srcName, tName)
		elif os.path.isfile(srcName):
			names = os.path.splitext(oName)
			if shouldCopy(names):
				pName = pinyin.get(names[0].decode('gb2312').encode('utf-8'), format="strip")
				s = srcDir.replace(assetsDir, '')
				s = s.replace('\\', '_')
				s = pinyin.get_initial(s.decode('gb2312').encode('utf-8')).replace(' ', '')
				pName = pName + s + names[1]
				tName = os.path.join(dscDir, pName)
				shutil.copy(srcName, tName)

if os.path.exists(targetDir):
	shutil.rmtree(targetDir)
if os.path.exists(plistDir):
	shutil.rmtree(plistDir)
os.mkdir(targetDir)
os.mkdir(plistDir)

travelDir(assetsDir, targetDir)

for x in os.listdir(targetDir):
	fileName = os.path.join(targetDir, x)
	dirName = os.path.join(plistDir, x)
	pngName = os.path.join(dirName, x)
	os.system(packPngCmdStr %(pngName, pngName, fileName))

