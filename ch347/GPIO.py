#-*-coding:utf-8;-*-
from ctypes import byref,cast,c_ubyte,POINTER
from typing import Callable,Tuple,Union
from .core import LIBRARY,mPCH347_INT_ROUTINE
def CH347GPIO_Get(iIndex:int)->Tuple[int,int]:
    iDir=c_ubyte()
    iData=c_ubyte()
    if LIBRARY.CH347GPIO_Get(iIndex,byref(iDir),byref(iData)):
        return iDir.value,iData.value
    else:
        return -1,-1
CH347GPIO_Set=LIBRARY.CH347GPIO_Set
def CH347SetIntRoutine(iIndex:int,Int0PinN:int,Int0TripMode:int,Int1PinN:int,Int1TripMode:int)->Callable[[Union[Callable[[bytes],None],None]],Union[mPCH347_INT_ROUTINE,None]]:
    def realCH347SetIntRoutine(iIntRoutine:Union[Callable[[bytes],None],None])->Union[mPCH347_INT_ROUTINE,None]:
        if iIntRoutine is None:
            realIIntRoutine=mPCH347_INT_ROUTINE()
        else:
            realIIntRoutine=mPCH347_INT_ROUTINE(lambda iStatus:iIntRoutine(bytes(iStatus[:8])))
        if LIBRARY.CH347SetIntRoutine(iIndex,Int0PinN,Int0TripMode,Int1PinN,Int1TripMode,realIIntRoutine):
            return realIIntRoutine
    return realCH347SetIntRoutine
def CH347ReadInter(iIndex:int)->bytes:
    iStatus=(c_ubyte*8)()
    if LIBRARY.CH347ReadInter(iIndex,cast(iStatus,POINTER(c_ubyte))):
        return bytes(iStatus[:])
    else:
        return b""
CH347AbortInter=LIBRARY.CH347AbortInter
CH347StartIapFwUpate=LIBRARY.CH347StartIapFwUpate