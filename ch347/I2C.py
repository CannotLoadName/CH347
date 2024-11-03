#-*-coding:utf-8;-*-
from ctypes import byref,cast,c_ubyte,c_ulong,POINTER
from typing import Tuple
from .core import LIBRARY
from .const import EEPROM_TYPE
CH347I2C_Set=LIBRARY.CH347I2C_Set
CH347I2C_SetStretch=LIBRARY.CH347I2C_SetStretch
CH347I2C_SetDelaymS=LIBRARY.CH347I2C_SetDelaymS
def CH347StreamI2C(iIndex:int,iWriteBuffer:bytes,iReadLength:int)->bytes:
    oReadBuffer=(c_ubyte*iReadLength)()
    if LIBRARY.CH347StreamI2C(iIndex,len(iWriteBuffer),byref((c_ubyte*len(iWriteBuffer))(*iWriteBuffer)),iReadLength,byref(oReadBuffer)):
        return bytes(oReadBuffer[:])
    else:
        return b""
def CH347StreamI2C_RetACK(iIndex:int,iWriteBuffer:bytes,iReadLength:int)->Tuple[bytes,int]:
    oReadBuffer=(c_ubyte*iReadLength)()
    rAckCount=c_ulong()
    if LIBRARY.CH347StreamI2C_RetACK(iIndex,len(iWriteBuffer),byref((c_ubyte*len(iWriteBuffer))(*iWriteBuffer)),iReadLength,byref(oReadBuffer),byref(rAckCount)):
        return bytes(oReadBuffer[:]),rAckCount.value
    else:
        return b"",-1
def CH347ReadEEPROM(iIndex:int,iEepromID:EEPROM_TYPE,iAddr:int,iLength:int)->bytes:
    oBuffer=(c_ubyte*iLength)()
    if LIBRARY.CH347ReadEEPROM(iIndex,iEepromID.value,iAddr,iLength,cast(oBuffer,POINTER(c_ubyte))):
        return bytes(oBuffer[:])
    else:
        return b""
def CH347WriteEEPROM(iIndex:int,iEepromID:EEPROM_TYPE,iAddr:int,iBuffer:bytes)->bool:
    return LIBRARY.CH347WriteEEPROM(iIndex,iEepromID.value,iAddr,len(iBuffer),cast((c_ubyte*len(iBuffer))(*iBuffer),POINTER(c_ubyte)))