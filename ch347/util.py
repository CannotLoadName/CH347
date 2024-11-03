#-*-coding:utf-8;-*-
from ctypes import byref,c_ubyte,c_ulong,string_at
from typing import Callable,Tuple,Union
from .core import LIBRARY,DEV_INFOR,mPCH347_NOTIFY_ROUTINE
CH347OpenDevice=LIBRARY.CH347OpenDevice
CH347CloseDevice=LIBRARY.CH347CloseDevice
def CH347GetDeviceInfor(iIndex:int)->dict:
    DevInformation=DEV_INFOR()
    if LIBRARY.CH347GetDeviceInfor(iIndex,byref(DevInformation)):
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
CH347GetChipType=LIBRARY.CH347GetChipType
def CH347GetVersion(iIndex:int)->Tuple[int,int,int,int]:
    iDriverVer=c_ubyte()
    iDLLVer=c_ubyte()
    ibcdDevice=c_ubyte()
    iChipType=c_ubyte()
    if LIBRARY.CH347GetVersion(iIndex,byref(iDriverVer),byref(iDLLVer),byref(ibcdDevice),byref(iChipType)):
        return iDriverVer.value,iDLLVer.value,ibcdDevice.value,iChipType.value
    else:
        return -1,-1,-1,-1
def CH347SetDeviceNotify(iIndex:int,iDeviceID:bytes)->Callable[[Union[Callable[[int],None],None]],Union[mPCH347_NOTIFY_ROUTINE,None]]:
    def realCH347SetDeviceNotify(iNotifyRoutine:Union[Callable[[int],None],None])->Union[mPCH347_NOTIFY_ROUTINE,None]:
        if iNotifyRoutine is None:
            realINotifyRoutine=mPCH347_NOTIFY_ROUTINE()
        else:
            realINotifyRoutine=mPCH347_NOTIFY_ROUTINE(iNotifyRoutine)
        if LIBRARY.CH347SetDeviceNotify(iIndex,iDeviceID,realINotifyRoutine):
            return realINotifyRoutine
    return realCH347SetDeviceNotify
def CH347ReadData(iIndex:int,ioLength:int)->bytes:
    oBuffer=(c_ubyte*ioLength)()
    realIoLength=c_ulong(ioLength)
    if LIBRARY.CH347ReadData(iIndex,byref(oBuffer),byref(realIoLength)):
        return bytes(oBuffer[:realIoLength.value])
    else:
        return b""
def CH347WriteData(iIndex:int,iBuffer:bytes)->int:
    ioLength=c_ulong(len(iBuffer))
    if LIBRARY.CH347WriteData(iIndex,byref((c_ubyte*len(iBuffer))(*iBuffer)),byref(ioLength)):
        return ioLength.value
    else:
        return -1
CH347SetTimeout=LIBRARY.CH347SetTimeout