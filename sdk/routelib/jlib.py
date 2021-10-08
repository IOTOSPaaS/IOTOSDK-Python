# coding=utf-8


import time
import struct
import sys
import json
import traceback

import logging
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler

import re
from utils import logger
# 心跳维持
class JLib:
    def __init__(self):
        self.logger = logger

        self.debug = self.logger.debug
        self.info = self.logger.info
        self.warn = self.logger.warn
        self.error = self.logger.error
        self.critical = self.logger.critical
        self.exception = self.logger.exception

    def str2hex(self,s):
        return ' '.join([hex(ord(c)).replace('0x', '') for c in s])

    def hex2str(self,s):
        return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])

    def str2bin(self,s):
        return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

    def bin2str(self,s):
        return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])

    def pack(self,expression,data):
        return struct.pack(expression,data)[0]

    def unpack(self,expression,data):
        if type(data) is int:
            data = data.to_bytes(length=1, byteorder='big')
        return struct.unpack(expression,data)[0]

    def unpackByte(self,bt):
        return struct.unpack('B',bt)[0]

    def errlog(self,dt):
        try:
            jsobj = json.loads(dt)
            if jsobj and jsobj['code'] != 0:
                traceback.print_exc(jsobj['msg'])
        except Exception as e:
            pass

    def print_hex(self,out):
        print(out.hex())

    def flags_extract(self,data,beginFlag,endFlag):
        ex = self.FlagsExtract()
        return ex.extract(data,beginFlag,endFlag)

    class FlagsExtract():
        def __init__(self):
            self.__beforeLeft = bytearray()
            self.__nextLeft = bytearray()
            self.__packagelist = []
            self.__data = None
            self.__flagBegin = None,
            self.__flagEnd = None

        def extract(self,data,flagBegin,flagEnd):
            self.__data = data
            self.__flagBegin = flagBegin
            self.__flagEnd = flagEnd
            self.__parser(data,flagBegin,flagEnd)
            return (self.__beforeLeft,self.__packagelist,self.__nextLeft)

        def __append_and_check(self,data):
            innerdatatmp = data[1:len(data) - 1]
            assert innerdatatmp.find(self.__flagBegin) == -1 and innerdatatmp.find(self.__flagEnd) == -1
            self.__packagelist.append(data)

        def __parser(self,data,flagBegin,flagEnd):
            beginIndex = data.find(flagBegin)
            endIndex = data.find(flagEnd)

            if beginIndex == -1 and endIndex == -1:
                self.__beforeLeft = data
                return

            if beginIndex == -1:
                assert endIndex == len(data) - 1
                self.__beforeLeft = data
                return
            if endIndex == -1:
                assert beginIndex == 0
                self.__nextLeft = data
                return


            realEndIndex = 0
            if beginIndex == 0:
                self.__append_and_check(data[beginIndex:endIndex + 1])
                realEndIndex = endIndex
            else:
                self.__beforeLeft = data[:beginIndex]
                if data.count(flagEnd) == 1:
                    assert data[beginIndex -1] == flagEnd
                    self.__nextLeft = data[beginIndex:]
                    return
                else:
                    itmp = data.find(flagEnd)
                    assert itmp == beginIndex -1
                    itmp2 = data[itmp + 1:].find(flagEnd)
                    realEndIndex = itmp + itmp2 + 1
                    assert realEndIndex > beginIndex
                    self.__append_and_check(data[beginIndex:realEndIndex + 1])
            if realEndIndex != len(data) - 1:
                assert data[realEndIndex + 1] == flagBegin
                self.__parser(data[realEndIndex + 1:],flagBegin,flagEnd)


if __name__ == '__main__':
    dt = bytearray([0x31,0x32,0x44,0x41,0x41,0x45,0x43,0x41,0x51,0x59,0x41])
    j = JLib()
    rt = j.flags_extract(dt,0x02,0x03)
    print(rt)
