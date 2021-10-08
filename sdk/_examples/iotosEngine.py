#!coding:utf8



import json
import sys
sys.path.append("..")
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass
import time
from iotos import *
from routelib.jlib import *
from utils import logger
import argparse
parser = argparse.ArgumentParser(description='')

parser.add_argument('--u', type=str, default = None)    

parser.add_argument('--p', type=str, default = None)    

parser.add_argument('--i', type=str, default = None)


parser.add_argument('--s', type=str, default = None)

try:
    parser.add_argument('--h', type=str, default = HTTP_HOST)
except:
    parser.add_argument('--h', type=str, default='http://sys.iotos.net.cn')
args = parser.parse_args()


username = args.u
password = args.p
uuid = args.i
host = args.h
s_name = args.s

zm = IOTOSys()
zm.http_host = host
try:
    login = zm.Login(username,password,uuid,True,s_name)
    logging.debug(login)
    dataRet = json.loads(login)
except Exception as e:
    traceback.print_exc()
    logger.error("启动异常")
    import signal
    while True:
        try:
            os.kill(os.getpid(), signal.SIGKILL)
            break
        except:
            traceback.print_exc()

if dataRet['code'] != 0:
    zm.Logout()
    if dataRet['msg'] == 'AccountNotRegister':
        time.sleep(99999999999)
    elif dataRet['msg'] == 'IONodeNotExist':
        time.sleep(60 * 60)
    else:
        time.sleep(10)
        zm.exit_to_reboot()
else:
    zm.engineRun()




# logout = zm.Logout()
# print logout,222222222

# valtmp = {dataId : 998}
# sendmsg = zm.SendMsg(uuid,json.dumps(valtmp))
# print 'sendmsg ======>>>>> ',sendmsg


# DevOnline = zm.DevOnline([uuid + '.' + devId])
# JLib().debug(DevOnline)


# DevOffine = zm.DevOffine(points)
# print DevOffine,5555555555


# GetPlatformData = zm.GetPlatformData(point)
# JLib().debug(GetPlatformData)


# GetDeviceData = zm.GetDeviceData(point)
# print "GetDeviceData ===========>>>",GetDeviceData


# SubMsg = zm.SubMsg(['7832cbf0-466e-11e7-9107-000c2977d5f6.7a502a16.b0e3e7e2'])
#pirnt SubMsg


# PubMsg = zm.PubMsg(point, True)
# JLib().debug(PubMsg)


# import pty
# import os
# import select
#
# def mkpty():
#     master1, slave = pty.openpty()
#     slaveName1 = os.ttyname(slave)
#
#     master2, slave = pty.openpty()
#     slaveName2 = os.ttyname(slave)
#
#     print '\nslavedevice names: ', slaveName1, slaveName2
#     return master1, master2
#
# if __name__ == "__main__":
#
#     master1, master2 = mkpty()
#     while True:
#         rl, wl, el = select.select([master1,master2], [], [], 1)
#         for master in rl:
#             data = os.read(master, 128)
#             print "read %d data." % len(data)
#             if master==master1:
#                 os.write(master2, data)
#             else:
#                 os.write(master1, data)



# PubMsgs = zm.PubMsgs(points)
# print PubMsgs


# text = json.dumps(text)

# # engineInit = zm.engineInit(text)

# zm.engineRun()
# time.sleep(3)
# sendmsg = zm.SendMsg('377ee948-7b59-11e7-bc9f-000c2977d5f6','aaa')

# count = zm.count()
# print count,2222222222222

# print zm.m_devlist
# [u'377ee948-7b59-11e7-bc9f-000c2977d5f6.d9c05ecb', u'377ee948-7b59-11e7-bc9f-000c2977d5f6.8ee79805']

# print zm.m_dev2attrs
# {u'377ee948-7b59-11e7-bc9f-000c2977d5f6.d9c05ecb': {u'timestamp': 1502437422.321, u'config': {u'type': u'serialport', u'param': {u'parity': u'N', u'baudrate': u'9600', u'byteSize': 8, u'xonxoff': 0, u'stopbits': 1, u'port': u'COM1'}, u'parentId': u''}, u'description': u'', u'name': u'agv_01'}, u'377ee948-7b59-11e7-bc9f-000c2977d5f6.8ee79805': {u'timestamp': 1502437422.214, u'config': {'param': {u'parity': u'N', u'baudrate': u'9600', u'byteSize': 8, u'xonxoff': 0, u'stopbits': 1, u'port': u'COM1'}, u'parentId': u'd9c05ecb'}, u'description': u'', u'name': u'agv_02'}}

# print zm.m_dev2points
# {u'377ee948-7b59-11e7-bc9f-000c2977d5f6.d9c05ecb': [u'377ee948-7b59-11e7-bc9f-000c2977d5f6.d9c05ecb.e513dee0', u'377ee948-7b59-11e7-bc9f-000c2977d5f6.d9c05ecb.e5132311', u'377ee948-7b59-11e7-bc9f-000c2977d5f6.d9c05ecb.8637dec2', u'377ee948-7b59-11e7-bc9f-000c2977d5f6.d9c05ecb.8637dec3'], u'377ee948-7b59-11e7-bc9f-000c2977d5f6.8ee79805': [u'377ee948-7b59-11e7-bc9f-000c2977d5f6.8ee79805.55f37d1e']}


# print zm.m_point2attrs
# {u'377ee948-7b59-11e7-bc9f-000c2977d5f6.d9c05ecb.e5132311': {u'description': u'\u53c2\u6570\u63cf\u8ff0', u'readwrite': u'0', u'timestamp': 1502438647.763, u'defaultvalue': u'', u'maxvalue': u'', u'minvalue': u'', u'refreshcycle': 10, u'regexp': u'', u'sensibility': u'', u'config': {u'type': u'modbus_rtu', u'param': {u'regad2': 8, u'devid12': 2, u'funid23': 3}, u'parentId': u''}, u'valuetype': u'BOOL', u'unit': u'', u'name': u'params'}, u'377ee948-7b59-11e7-bc9f-000c2977d5f6.d9c05ecb.8637dec3': {u'description': u'', u'readwrite': u'1', u'timestamp': 1502438647.763, u'defaultvalue': u'', u'maxvalue': u'', u'minvalue': u'', u'refreshcycle': 1000, u'regexp': u'', u'sensibility': u'', u'config': {u'param': {u'regad2': 8912, u'devid12': 2, u'funid': 3, u'devid': 2, u'regad': 900, u'funid23': 3, u'test': 10010}, u'parentId': u'8637dec2'}, u'valuetype': u'BOOL', u'unit': u'', u'name': u'params2'}, u'377ee948-7b59-11e7-bc9f-000c2977d5f6.d9c05ecb.8637dec2': {u'description': u'', u'readwrite': u'1', u'timestamp': 1502438647.763, u'defaultvalue': u'', u'maxvalue': u'', u'minvalue': u'', u'refreshcycle': 1000, u'regexp': u'', u'sensibility': u'', u'config': {u'param': {u'regad2': 8, u'devid12': 2, u'funid': 3, u'devid': 2, u'regad': 9, u'funid23': 3}, u'parentId': u'e513dee0'}, u'valuetype': u'BOOL', u'unit': u'', u'name': u'params2'}, u'377ee948-7b59-11e7-bc9f-000c2977d5f6.8ee79805.55f37d1e': {u'description': u'\u63cf\u8ff0xxx', u'readwrite': u'2', u'timestamp': 1502438647.763, u'defaultvalue': u'', u'maxvalue': u'', u'minvalue': u'', u'refreshcycle': 300, u'regexp': u'', u'sensibility': u'', u'config': {u'type': u'modbus_rtu', u'param': {u'regad': 0, u'funid': 2, u'devid': 1}, u'parentId': u''}, u'valuetype': u'INT', u'unit': u'', u'name': u'params'}, u'377ee948-7b59-11e7-bc9f-000c2977d5f6.d9c05ecb.e513dee0': {u'description': u'\u53c2\u6570\u63cf\u8ff0', u'readwrite': u'0', u'timestamp': 1502438647.763, u'defaultvalue': u'', u'maxvalue': u'', u'minvalue': u'', u'refreshcycle': 10, u'regexp': u'', u'sensibility': u'', u'config': {u'type': u'modbus_rtu', u'param': {u'regad2': 8, u'devid12': 2, u'funid': 3, u'devid': 2, u'regad': 4, u'funid23': 3}, u'parentId': u'e5132311'}, u'valuetype': u'BOOL', u'unit': u'', u'name': u'params'}}


# print zm.RunCollecting()




# import OpenOPC
#
# opc_server = 'DSxPOpcSimulator.TSxOpcSimulator.1'
# opc_host='127.0.0.1'
#
# opc = OpenOPC.client()
# print opc.servers()
# # [u'DSxPOpcSimulator.TSxOpcSimulator.1']
# opc.connect(opc_server)
# print opc.write(('Simulation Items.String.Str_03','hello world!'))
# while True:
# 	print opc.read('Simulation Items.String.Str_03', sync=True)
# 	time.sleep(1)




# import time
# import modbus_tk
# import modbus_tk.defines as cst
# import modbus_tk.modbus as modbus
# import modbus_tk.modbus_rtu as modbus_rtu
# import serial
#
# serial = serial.Serial(port='COM4', baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
# master = modbus_rtu.RtuMaster(serial)
# master.set_timeout(10.0)
# master.set_verbose(True)
#
# rtu_ret = master.execute(4, cst.READ_HOLDING_REGISTERS, 32, 16)
# print 'rtu_ret', len(rtu_ret), rtu_ret
