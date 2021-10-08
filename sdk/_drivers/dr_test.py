#!coding:utf8
import json
import sys

sys.path.append("..")
from driver import *


class iotos_1(IOTOSDriverI):
    # 1、通信初始化
    def InitComm(self, attrs):
        self.online(True)
        self.setPauseCollect(False)
        self.setCollectingOneCircle(False)

    # 2、采集引擎回调，可也可以开启，也可以直接注释掉（对于主动上报，不存在遍历采集的情况）
    def Collecting(self, dataId):
        # self.setValue(u'车辆动态统计.车主电话', 12234437586)
        # self.setValue(u'车辆动态统计.车主姓名', " 张三")
        # self.setValue(u'车辆动态统计.当前车辆进出方向', "出")
        # self.setValue(u'车辆动态统计.车辆是否为黑名单车辆', False)
        # self.setValue(u'车辆动态统计.当前车身颜色', "黑色")
        # self.setValue(u'车辆动态统计.当前车辆车牌', "鄂A52602")
        # self.setValue(u'车辆动态统计.车辆出总数', 4452)
        # self.setValue(u'车辆动态统计.车辆进入总数', 2210)
        # self.setValue(u'车辆动态统计.车辆进出总数', 6662)
        # self.setValue(u'车辆动态统计.车辆类型', "小轿车")
        # self.setValue(u'人员动态统计.当前人员是否佩戴口罩', "yes")
        # self.setValue(u'人员动态统计.当前人员性别', "nan")
        # self.setValue(u'人员动态统计.当前人体温度', "30.2")
        # self.setValue(u'人员动态统计.门禁闸机打开状态', False)
        # self.setValue(u'人员动态统计.人员出数量', 74171)
        # self.setValue(u'人员动态统计.人员进入数量', 14141)
        # self.setValue(u'人员动态统计.总人数统计', 4452)

        return ()

    # 3、控制
    # 广播事件回调，其他操作访问
    def Event_customBroadcast(self, fromUuid, type, data):
        '''*************************************************
        TODO
        **************************************************'''
        return json.dumps({'code': 0, 'msg': '', 'data': ''})

    # 4、查询
    # 查询事件回调，数据点查询访问
    def Event_getData(self, dataId, condition):
        '''*************************************************
        TODO
        **************************************************'''
        return json.dumps({'code': 0, 'msg': '', 'data': ''})

    # 5、控制事件回调，数据点控制访问
    def Event_setData(self, dataId, value):
        '''*************************************************
        TODO
        **************************************************'''
        return json.dumps({'code': 0, 'msg': '', 'data': ''})

    # 6、本地事件回调，数据点操作访问
    def Event_syncPubMsg(self, point, value):
        '''*************************************************
        TODO
        **************************************************'''
        return json.dumps({'code': 0, 'msg': '', 'data': ''})
