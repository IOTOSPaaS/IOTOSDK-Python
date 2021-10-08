#!coding:utf8
from driver import IOTOSDriverI
import json, time, random, threading


# 继承官方驱动类（ZMIotDriverI）
from exception import DataNotExistError


class HelloWorldDriver(IOTOSDriverI):

    # 1、通信初始化
    def InitComm(self, attrs):
        self.online(True)
        self.critical("deviceId=" + self.sysId)
        self.debug("deviceId=" + self.sysId)
        self.pauseCollect = False

        try:
            # 通过数据点名称，设置单个值
            self.setValue('上电时间', time.time())

            # 通过数据点名称，设置多个值
            s = self.id(u'设备网络状态')
            retJson = self.setValues([
                dict(id=self.pointId(self.id(u'网关网络状态')), value=1),
                dict(id=self.pointId(self.id(u'设备网络状态')), value=1),
            ])
            self.info(retJson)
        except DataNotExistError as e:
            self.warn(e)

    # 2、采集
    def Collecting(self, dataId):
        '''*************************************************
        TODO
        **************************************************'''
        time.sleep(1)
        try:
            # 通过数据点ID获取数据点属性字典
            data_attr = self.data2attrs[dataId]
            value_type = data_attr["valuetype"]
            s = self.name(dataId)
            if self.name(dataId) == u'上电时间':
                return None
            if value_type == u'BOOL':
                new_value = random.randint(0, 1)
            elif value_type == u'FLOAT':
                new_value = random.uniform(0, 1000)
            else:
                new_value = time.time()
            return (new_value, )
        except DataNotExistError as e:
            self.error(e)
            return None

    # 3、控制
    # 事件回调接口，其他操作访问
    def Event_customBroadcast(self, fromUuid, type, data):
        '''*************************************************

        TODO
        **************************************************'''
        return json.dumps({'code': 0, 'msg': '', 'data': ''})

    # 3、查询
    # 事件回调接口，监测点操作访问
    def Event_getData(self, dataId, condition):
        '''*************************************************
        TODO
        **************************************************'''
        return json.dumps({'code': 0, 'msg': '', 'data': ''})

    # 事件回调接口，监测点操作访问
    def Event_setData(self, dataId, value):
        '''*************************************************
        TODO
        **************************************************'''
        return json.dumps({'code': 0, 'msg': '', 'data': ''})

    # 事件回调接口，监测点操作访问
    def Event_syncPubMsg(self, point, value):
        '''*************************************************
        TODO
        **************************************************'''
        return json.dumps({'code': 0, 'msg': '', 'data': ''})