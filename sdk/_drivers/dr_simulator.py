#!coding:utf8
import json
# import winsound
import sys

sys.path.append("..")

from driver import *
import threading
import time
import random
import math
import datetime

def indexOf(strList,strItem):
    itmp = -1
    for item in strList:
        if item == strItem:
            itmp = strList.index(item)
            return itmp
    return itmp

class Simulator(IOTOSDriverI):
    datetimes = datetime.datetime.now()
    times=datetime.datetime.strftime(datetimes,'%H:%M:%S')
    dataId2Timer = {}

    def timerProcess(self,param,dataId):
        typetmp = param['pointType']
        changetmp = param['changeOption']

        # valtmp = self.value(self.name(dataId))
        valtmp = self.value(self.name(dataId),source='platform')

        self.warn(self.name(dataId) + ' : ' + str(valtmp))
        if typetmp == 'BOOL':
            if changetmp == 'Ascending' or changetmp == 'Descending':
                if valtmp == '' or valtmp == None:
                    valtmp = False
                valtmp = bool(1- valtmp)
            elif changetmp == 'Constant':
                pass
            elif changetmp == 'Random':
                valtmp = bool(random.randint(0,1))
            valtmp = bool(valtmp)
        elif typetmp == "INT":
            if valtmp == '' or valtmp == None:
                valtmp = 0
            if changetmp == 'Ascending' or changetmp == 'Descending':
                if changetmp == 'Ascending':
                    valtmp = int(valtmp) + 1
                else:
                    valtmp = int(valtmp) - 1
                if valtmp > param['valueRange'][1]:
                    valtmp = param['valueRange'][0]
                if valtmp < param['valueRange'][0]:
                    valtmp = param['valueRange'][1]
            elif changetmp == 'Random':
                valtmp = random.randint(param['valueRange'][0],param['valueRange'][1])
            elif changetmp == 'Constant':
                pass
        elif typetmp == "FLOAT":
            if valtmp == '' or valtmp == None:
                valtmp = 0.0
            if changetmp == 'Ascending':
                valtmp = random.uniform(valtmp,param['valueRange'][1])
            elif changetmp == 'Descending':
                valtmp = random.uniform(param['valueRange'][0],valtmp)
            elif changetmp == 'Random':
                valtmp = random.uniform(param['valueRange'][0], param['valueRange'][1])
            elif changetmp == 'Constant':
                pass
            if valtmp >= param['valueRange'][1]:
                valtmp = param['valueRange'][0]
            elif valtmp <= param['valueRange'][0]:
                valtmp = param['valueRange'][1]
            valtmp = round(valtmp,3)
        elif typetmp == "STRING":
            strlisttmp = param['stringContents'].split(' ')
            itmp = indexOf(strlisttmp,valtmp)
            if itmp == -1:
                itmp = 0
            elif changetmp == 'Ascending' or changetmp == 'Descending':
                if changetmp == 'Ascending':
                    itmp += 1
                else:
                    itmp -= 1
                if itmp == len(strlisttmp):
                    itmp = 0
                elif itmp == -1:
                    itmp = len(strlisttmp) - 1
            elif changetmp == 'Random':
                itmp = random.randint(0,len(strlisttmp) - 1)
            elif changetmp == 'Constant':
                pass
            else:
                assert 0
            valtmp = str(strlisttmp[itmp])
        else:
            assert 0

        self.setValue(self.name(dataId), valtmp)

        #??????????????????
        if param['timeChoose'] == 0:    #????????????
            time.sleep(param['timeDefault']/1000.000)
        else:                           #????????????
            time.sleep(random.randint(param['timeRange'][0],param['timeRange'][1])/1000.0000)

        #???????????????????????????
        timertmp = threading.Timer(5, self.timerProcess, (param, dataId))
        self.dataId2Timer[dataId] = timertmp
        #python???timer????????????????????????????????????
        timertmp.start()


    # 1??????????????????
    def InitComm(self, attrs):
        self.online(True)
        self.collectingOneCircle = True                                 #???????????????Collecting?????????????????????????????????????????????
        self.pauseCollect = True

    # 2?????????
    def Collecting(self, dataId):
        cfgtmp = self.data2attrs[dataId]['config']['param']
        changeChooseTmp = cfgtmp['change']['choose']
        pointType = self.data2attrs[dataId]['valuetype']
        timeOption = cfgtmp['time']['option'][1]['random']
        valueOption = cfgtmp['value']['range']

        #???????????????????????????????????????????????????????????????????????????????????????
        timeChoose = cfgtmp['time']['choose']
        timeDefault = cfgtmp['time']['option'][0]['default']            #??????????????????
        timeRange = (timeOption['min'],timeOption['max'])               #????????????????????????
        changeOption = cfgtmp['change']['option'][changeChooseTmp]      #????????????
        valueRange = (valueOption['min'],valueOption['max'])            #?????????????????????
        stringContents = cfgtmp['value'].get("string", '')                      #??????????????????
        paramtmp = {
            'pointType':pointType,
            'timeChoose':timeChoose,
            'timeDefault':timeDefault,
            'timeRange':timeRange,
            'changeOption':changeOption,
            'valueRange':valueRange,
            'stringContents':stringContents
        }
        # ???????????????????????????????????????
        timertmp = threading.Timer(5, self.timerProcess, (paramtmp, dataId))
        self.dataId2Timer[dataId] = timertmp
        #python???timer????????????????????????????????????
        timertmp.start()
        return ()

    # 3?????????
    # ???????????????????????????????????????
    def Event_customBroadcast(self, fromUuid, type, data):
        '''*************************************************

		TODO
		**************************************************'''
        return json.dumps({'code': 0, 'msg': '', 'data': ''})

    # 3?????????
    # ??????????????????????????????????????????
    def Event_getData(self, dataId, condition):
        data = None
        return json.dumps({'code': 0, 'msg': '', 'data': {'time':0,'value':data}})

    # ??????????????????????????????????????????
    def Event_setData(self, dataId, value):
        # winsound.Beep(500,100)
        self.info("**********************")
        return json.dumps({'code': 0, 'msg': '', 'data': ''})

    # ??????????????????????????????????????????
    def Event_syncPubMsg(self, point, value):
        return json.dumps({'code': 0, 'msg': '', 'data': ''})
