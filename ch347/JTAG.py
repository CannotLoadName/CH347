#-*-coding:utf-8;-*-
from ctypes import byref,cast,c_ubyte,c_ulong,POINTER
from math import ceil
from .core import LIBRARY
CH347Jtag_INIT=LIBRARY.CH347Jtag_INIT
def CH347Jtag_GetCfg(iIndex:int)->int:
    ClockRate=c_ubyte()
    if LIBRARY.CH347Jtag_GetCfg(iIndex,byref(ClockRate)):
        return ClockRate.value
    else:
        return -1
def CH347Jtag_TmsChange(iIndex:int,tmsValue:bytes,Step:int,Skip:int)->bool:
    realStep=ceil(Step/8)
    return LIBRARY.CH347Jtag_TmsChange(iIndex,cast((c_ubyte*realStep)(*tmsValue[:min(len(tmsValue),realStep)]),POINTER(c_ubyte)),Step,Skip)
def CH347Jtag_IoScan(iIndex:int,DataBits:bytes,DataBitsNb:int,IsRead:bool)->bytes:
    realDataBitsNb=ceil(DataBitsNb/8)
    realDataBits=(c_ubyte*realDataBitsNb)(*DataBits[:min(len(DataBits),realDataBitsNb)])
    if LIBRARY.CH347Jtag_IoScan(iIndex,cast(realDataBits,POINTER(c_ubyte)),DataBitsNb,IsRead):
        return bytes(realDataBits[:])
    else:
        return b""
def CH347Jtag_IoScanT(iIndex:int,DataBits:bytes,DataBitsNb:int,IsRead:bool,IsLastPkt:bool)->bytes:
    realDataBitsNb=ceil(DataBitsNb/8)
    realDataBits=(c_ubyte*realDataBitsNb)(*DataBits[:min(len(DataBits),realDataBitsNb)])
    if LIBRARY.CH347Jtag_IoScanT(iIndex,cast(realDataBits,POINTER(c_ubyte)),DataBitsNb,IsRead,IsLastPkt):
        return bytes(realDataBits[:])
    else:
        return b""
CH347Jtag_Reset=LIBRARY.CH347Jtag_Reset
CH347Jtag_ResetTrst=LIBRARY.CH347Jtag_ResetTrst
def CH347Jtag_WriteRead(iIndex:int,IsDR:bool,iWriteBitLength:int,iWriteBitBuffer:bytes,oReadBitLength:int)->bytes:
    realIWriteBitLength=ceil(iWriteBitLength/8)
    realOReadBitLength=c_ulong(oReadBitLength)
    oReadBitBuffer=(c_ubyte*ceil(oReadBitLength/8))()
    if LIBRARY.CH347Jtag_WriteRead(iIndex,IsDR,iWriteBitLength,byref((c_ubyte*realIWriteBitLength)(*iWriteBitBuffer[:min(len(iWriteBitBuffer),realIWriteBitLength)])),byref(realOReadBitLength),byref(oReadBitBuffer)):
        return bytes(oReadBitBuffer[:ceil(realOReadBitLength.value/8)])
    else:
        return b""
def CH347Jtag_WriteRead_Fast(iIndex:int,IsDR:bool,iWriteBitBuffer:bytes,oReadBitLength:int)->bytes:
    realOReadBitLength=c_ulong(oReadBitLength)
    oReadBitBuffer=(c_ubyte*oReadBitLength)()
    if LIBRARY.CH347Jtag_WriteRead_Fast(iIndex,IsDR,len(iWriteBitBuffer),byref((c_ubyte*len(iWriteBitBuffer))(*iWriteBitBuffer)),byref(realOReadBitLength),byref(oReadBitBuffer)):
        return bytes(oReadBitBuffer[:realOReadBitLength.value])
    else:
        return b""
CH347Jtag_SwitchTapState=LIBRARY.CH347Jtag_SwitchTapState
def CH347Jtag_ByteWriteDR(iIndex:int,iWriteBuffer:bytes)->bool:
    return LIBRARY.CH347Jtag_ByteWriteDR(iIndex,len(iWriteBuffer),byref((c_ubyte*len(iWriteBuffer))(*iWriteBuffer)))
def CH347Jtag_ByteReadDR(iIndex:int,oReadLength:int)->bytes:
    realOReadLength=c_ulong(oReadLength)
    oReadBuffer=(c_ubyte*oReadLength)()
    if LIBRARY.CH347Jtag_ByteReadDR(iIndex,byref(realOReadLength),byref(oReadBuffer)):
        return bytes(oReadBuffer[:realOReadLength.value])
    else:
        return b""
def CH347Jtag_ByteWriteIR(iIndex:int,iWriteBuffer:bytes)->bool:
    return LIBRARY.CH347Jtag_ByteWriteIR(iIndex,len(iWriteBuffer),byref((c_ubyte*len(iWriteBuffer))(*iWriteBuffer)))
def CH347Jtag_ByteReadIR(iIndex:int,oReadLength:int)->bytes:
    realOReadLength=c_ulong(oReadLength)
    oReadBuffer=(c_ubyte*oReadLength)()
    if LIBRARY.CH347Jtag_ByteReadIR(iIndex,byref(realOReadLength),byref(oReadBuffer)):
        return bytes(oReadBuffer[:realOReadLength.value])
    else:
        return b""
def CH347Jtag_BitWriteDR(iIndex:int,iWriteBitLength:int,iWriteBitBuffer:bytes)->bool:
    realIWriteBitLength=ceil(iWriteBitLength/8)
    return LIBRARY.CH347Jtag_BitWriteDR(iIndex,iWriteBitLength,byref((c_ubyte*realIWriteBitLength)(*iWriteBitBuffer[:min(len(iWriteBitBuffer),realIWriteBitLength)])))
def CH347Jtag_BitWriteIR(iIndex:int,iWriteBitLength:int,iWriteBitBuffer:bytes)->bool:
    realIWriteBitLength=ceil(iWriteBitLength/8)
    return LIBRARY.CH347Jtag_BitWriteIR(iIndex,iWriteBitLength,byref((c_ubyte*realIWriteBitLength)(*iWriteBitBuffer[:min(len(iWriteBitBuffer),realIWriteBitLength)])))
def CH347Jtag_BitReadIR(iIndex:int,oReadBitLength:int)->bytes:
    realOReadBitLength=c_ulong(oReadBitLength)
    oReadBitBuffer=(c_ubyte*ceil(oReadBitLength/8))()
    if LIBRARY.CH347Jtag_BitReadIR(iIndex,byref(realOReadBitLength),byref(oReadBitBuffer)):
        return bytes(oReadBitBuffer[:ceil(realOReadBitLength.value/8)])
    else:
        return b""
def CH347Jtag_BitReadDR(iIndex:int,oReadBitLength:int)->bytes:
    realOReadBitLength=c_ulong(oReadBitLength)
    oReadBitBuffer=(c_ubyte*ceil(oReadBitLength/8))()
    if LIBRARY.CH347Jtag_BitReadDR(iIndex,byref(realOReadBitLength),byref(oReadBitBuffer)):
        return bytes(oReadBitBuffer[:ceil(realOReadBitLength.value/8)])
    else:
        return b""