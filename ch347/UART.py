#-*-coding:utf-8;-*-
from ctypes import byref,c_longlong,c_ubyte,c_ulong,string_at
from typing import Callable,Tuple,Union
from .core import LIBRARY,DEV_INFOR,mPCH347_NOTIFY_ROUTINE
CH347Uart_Open=LIBRARY.CH347Uart_Open
CH347Uart_Close=LIBRARY.CH347Uart_Close
def CH347Uart_SetDeviceNotify(iIndex:int,iDeviceID:bytes)->Callable[[Union[Callable[[int],None],None]],Union[mPCH347_NOTIFY_ROUTINE,None]]:
    def realCH347Uart_SetDeviceNotify(iNotifyRoutine:Union[Callable[[int],None],None])->Union[mPCH347_NOTIFY_ROUTINE,None]:
        if iNotifyRoutine is None:
            realINotifyRoutine=mPCH347_NOTIFY_ROUTINE()
        else:
            realINotifyRoutine=mPCH347_NOTIFY_ROUTINE(iNotifyRoutine)
        if LIBRARY.CH347Uart_SetDeviceNotify(iIndex,iDeviceID,realINotifyRoutine):
            return realINotifyRoutine
    return realCH347Uart_SetDeviceNotify
def CH347Uart_GetCfg(iIndex:int)->Tuple[int,int,int,int,int]:
    BaudRate=c_ulong()
    ByteSize=c_ubyte()
    Parity=c_ubyte()
    StopBits=c_ubyte()
    ByteTimeout=c_ubyte()
    if LIBRARY.CH347Uart_GetCfg(iIndex,byref(BaudRate),byref(ByteSize),byref(Parity),byref(StopBits),byref(ByteTimeout)):
        return BaudRate.value,ByteSize.value,Parity.value,StopBits.value,ByteTimeout.value
    else:
        return -1,-1,-1,-1,-1
CH347Uart_Init=LIBRARY.CH347Uart_Init
CH347Uart_SetTimeout=LIBRARY.CH347Uart_SetTimeout
def CH347Uart_Read(iIndex:int,ioLength:int)->bytes:
    oBuffer=(c_ubyte*ioLength)()
    realIoLength=c_ulong(ioLength)
    if LIBRARY.CH347Uart_Read(iIndex,byref(oBuffer),byref(realIoLength)):
        return bytes(oBuffer[:realIoLength.value])
    else:
        return b""
def CH347Uart_Write(iIndex:int,iBuffer:bytes)->int:
    ioLength=c_ulong(len(iBuffer))
    if LIBRARY.CH347Uart_Write(iIndex,byref((c_ubyte*len(iBuffer))(*iBuffer)),byref(ioLength)):
        return ioLength.value
    else:
        return -1
def CH347Uart_QueryBufUpload(iIndex:int)->int:
    RemainBytes=c_longlong()
    if LIBRARY.CH347Uart_QueryBufUpload(iIndex,byref(RemainBytes)):
        return RemainBytes.value
    else:
        return -1
def CH347Uart_GetDeviceInfor(iIndex:int)->dict:
    DevInformation=DEV_INFOR()
    if LIBRARY.CH347Uart_GetDeviceInfor(iIndex,byref(DevInformation)):
        return {
            "iIndex":DevInformation.iIndex,
            "DevicePath":string_at(DevInformation.DevicePath),
            "UsbClass":DevInformation.UsbClass,
            "FuncType":DevInformation.FuncType,
            "DeviceID":DevInformation.DeviceID,
            "ChipMode":DevInformation.ChipMode,
            "DevHandle":DevInformation.DevHandle,
            "BulkOutEndpMaxSize":DevInformation.BulkOutEndpMaxSize,
            "BulkInEndpMaxSize":DevInformation.BulkInEndpMaxSize,
            "UsbSpeedType":DevInformation.UsbSpeedType,
            "CH347IfNum":DevInformation.CH347IfNum,
            "DataUpEndp":DevInformation.DataUpEndp,
            "DataDnEndp":DevInformation.DataDnEndp,
            "ProductString":DevInformation.ProductString,
            "ManufacturerString":DevInformation.ManufacturerString,
            "WriteTimeout":DevInformation.WriteTimeout,
            "ReadTimeout":DevInformation.ReadTimeout,
            "FuncDescStr":DevInformation.FuncDescStr,
            "FirewareVer":DevInformation.FirewareVer
        }
    else:
        return {}