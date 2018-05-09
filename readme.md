说明：1.自动将中文名的图片转为拼音,驼峰名+下划线+目录名首字母
	    如：登陆目录下的登陆背景.jpg->dengLuBeiJing_bj.jpg
	    所有文件将拷贝到target目录下
	  2.自动打包为plist文件，保存在plistDir下

1.安装texture packer安装目录下的bin目录添加到path中去
2.将图片放入assets（目前只支持一级目录）
3.在auto.py中添加需要屏蔽的图片
4.执行auto.py