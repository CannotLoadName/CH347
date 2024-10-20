import ctypes
from enum import Enum
from typing import Tuple
from .util import LIBRARY
class EEPROM_TYPE(Enum):
    ID_24C01=ctypes.c_int(0)
    ID_24C02=ctypes.c_int(1)
    ID_24C04=ctypes.c_int(2)
    ID_24C08=ctypes.c_int(3)
    ID_24C16=ctypes.c_int(4)
    ID_24C32=ctypes.c_int(5)
    ID_24C64=ctypes.c_int(6)
    ID_24C128=ctypes.c_int(7)
    ID_24C256=ctypes.c_int(8)
    ID_24C512=ctypes.c_int(9)
    ID_24C1024=ctypes.c_int(10)
    ID_24C2048=ctypes.c_int(11)
    ID_24C4096=ctypes.c_int(12)
def CH347I2C_Set(iIndex:int=0,iMode:int=1)->bool:
    if LIBRARY.CH347I2C_Set(ctypes.c_ulong(iIndex),ctypes.c_ulong(iMode)):
        return True
    else:
        return False
def CH347I2C_SetStretch(iIndex:int=0,iEnable:bool=True)->bool:
    if LIBRARY.CH347I2C_SetStretch(ctypes.c_ulong(iIndex),ctypes.c_bool(iEnable)):
        return True
    else:
        return False
def CH347I2C_SetDelaymS(iIndex:int=0,iDelay:int=0)->bool:
    if LIBRARY.CH347I2C_SetDelaymS(ctypes.c_ulong(iIndex),ctypes.c_ulong(iDelay)):
        return True
    else:
        return False
def CH347StreamI2C(iIndex:int=0,iWriteBuffer:bytes=b"",iReadLength:int=0)->bytes:
    oReadBuffer=(ctypes.c_ubyte*iReadLength)()
    if LIBRARY.CH347StreamI2C(ctypes.c_ulong(iIndex),ctypes.c_ulong(len(iWriteBuffer)),ctypes.byref((ctypes.c_ubyte*len(iWriteBuffer))(*iWriteBuffer)),ctypes.c_ulong(iReadLength),ctypes.byref(oReadBuffer)):
        return bytes(oReadBuffer)
    else:
        return b""
def CH347StreamI2C_RetACK(iIndex:int=0,iWriteBuffer:bytes=b"",iReadLength:int=0)->Tuple[bytes,int]:
    oReadBuffer=(ctypes.c_ubyte*iReadLength)()
    rAckCount=ctypes.c_ulong()
    if LIBRARY.CH347StreamI2C_RetACK(ctypes.c_ulong(iIndex),ctypes.c_ulong(len(iWriteBuffer)),ctypes.byref((ctypes.c_ubyte*len(iWriteBuffer))(*iWriteBuffer)),ctypes.c_ulong(iReadLength),ctypes.byref(oReadBuffer),ctypes.byref(rAckCount)):
        return bytes(oReadBuffer),rAckCount.value
    else:
        return b"",-1
def CH347ReadEEPROM(iIndex:int=0,iEepromID:EEPROM_TYPE=EEPROM_TYPE.ID_24C01,iAddr:int=0,iLength:int=0)->bytes:
    iBuffer=(ctypes.c_ubyte*iLength)()
    if LIBRARY.CH347ReadEEPROM(ctypes.c_ulong(iIndex),iEepromID.value,ctypes.c_ulong(iAddr),ctypes.c_ulong(iLength),ctypes.byref(iBuffer)):
        return bytes(iBuffer)
    else:
        return b""
def CH347WriteEEPROM(iIndex:int=0,iEepromID:EEPROM_TYPE=EEPROM_TYPE.ID_24C01,iAddr:int=0,iBuffer:bytes=b"")->bool:
    if LIBRARY.CH347WriteEEPROM(ctypes.c_ulong(iIndex),iEepromID.value,ctypes.c_ulong(iAddr),ctypes.c_ulong(len(iBuffer)),ctypes.byref((ctypes.c_ubyte*len(iBuffer))(*iBuffer))):
        return True
    else:
        return False