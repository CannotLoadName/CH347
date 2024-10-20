import ctypes
from typing import Tuple
from .util import LIBRARY
def CH347GPIO_Get(iIndex:int=0)->Tuple[int,int]:
    iDir=ctypes.c_ubyte()
    iData=ctypes.c_ubyte()
    if LIBRARY.CH347GPIO_Get(ctypes.c_ulong(iIndex),ctypes.byref(iDir),ctypes.byref(iData)):
        return iDir.value,iData.value
    else:
        return -1,-1
def CH347GPIO_Set(iIndex:int=0,iEnable:int=0xff,iSetDirOut:int=0,iSetDataOut:int=0)->bool:
    if LIBRARY.CH347GPIO_Set(ctypes.c_ulong(iIndex),ctypes.c_ubyte(iEnable),ctypes.c_ubyte(iSetDirOut),ctypes.c_ubyte(iSetDataOut)):
        return True
    else:
        return False