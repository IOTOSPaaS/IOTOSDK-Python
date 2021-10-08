#!coding:utf8
import json
# import winsound
import sys
sys.path.append("..")

from driver import *
import threading
import time

class Demo(IOTOSDriverI):
	p1val = 0
	c1val = 0
	f1val = 0
	ctime = 0
	flag = True

	def func(self):
		if self.flag == False:
			self.flag = True
		else:
			self.flag = False
		self.setValue(u'demo_device.回水电磁阀1控制', self.flag)
		self.timer = threading.Timer(1, self.func)
		self.timer.start()

	#1、通信初始化
	def InitComm(self,attrs):
		self.timer = threading.Timer(1, self.func)
		self.timer.start()
		self.online(True)

		self.setValue(u'demo_device.热水供水泵控制', True)


	#2、采集
	def Collecting(self, dataId):
		time.sleep(0xfffff)
		'''*************************************************

		TODO

		**************************************************'''
		return 0


	#3、控制
	#事件回调接口，其他操作访问
	def Event_customBroadcast(self, fromUuid, type, data):
		'''*************************************************

		TODO 

		**************************************************'''
		return json.dumps({'code':0, 'msg':'', 'data':''})

	# 3、查询
	# 事件回调接口，监测点操作访问
	def Event_getData(self, dataId, condition):
		'''*************************************************

		TODO 

		**************************************************'''
		data=None
		return json.dumps({'code':0, 'msg':'', 'data':data})


	# 事件回调接口，监测点操作访问
	def Event_setData(self, dataId, value):

		# winsound.Beep(500,100)


		return json.dumps({'code':0, 'msg':'', 'data':''})


	# 事件回调接口，监测点操作访问
	def Event_syncPubMsg(self, point, value):

		return json.dumps({'code':0, 'msg':'', 'data':''})