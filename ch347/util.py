import ctypes
from ctypes.wintypes import HANDLE,MAX_PATH
from typing import Tuple
try:
    LIBRARY=ctypes.WinDLL("CH347DLLA64.DLL")
except FileNotFoundError:
    try:
        LIBRARY=ctypes.WinDLL("CH347DLL.DLL")
    except FileNotFoundError:
        raise ImportError("You have not installed the driver for CH347.")
class DEV_INFOR(ctypes.Structure):
    _fields_=[
        ("iIndex",ctypes.c_ubyte),
        ("DevicePath",ctypes.c_ubyte*MAX_PATH),
        ("UsbClass",ctypes.c_ubyte),
        ("FuncType",ctypes.c_ubyte),
        ("DeviceID",ctypes.c_char*64),
        ("ChipMode",ctypes.c_ubyte),
        ("DevHandle",HANDLE),
        ("BulkOutEndpMaxSize",ctypes.c_ushort),
        ("BulkInEndpMaxSize",ctypes.c_ushort),
        ("UsbSpeedType",ctypes.c_ubyte),
        ("CH347IfNum",ctypes.c_ubyte),
        ("DataUpEndp",ctypes.c_ubyte),
        ("DataDnEndp",ctypes.c_ubyte),
        ("ProductString",ctypes.c_char*64),
        ("ManufacturerString",ctypes.c_char*64),
        ("WriteTimeout",ctypes.c_ulong),
        ("ReadTimeout",ctypes.c_ulong),
        ("FuncDescStr",ctypes.c_char*64),
        ("FirewareVer",ctypes.c_ubyte)
    ]
def CH347OpenDevice(DevI:int=0)->int:
    return LIBRARY.CH347OpenDevice(ctypes.c_ulong(DevI))
def CH347CloseDevice(iIndex:int=0)->bool:
    if LIBRARY.CH347CloseDevice(ctypes.c_ulong(iIndex)):
        return True
    else:
        return False
def CH347GetDeviceInfor(iIndex:int=0)->dict:
    DevInformation=DEV_INFOR()
    if LIBRARY.CH347GetDeviceInfor(ctypes.c_ulong(iIndex),ctypes.byref(DevInformation)):
        return {
            "iIndex":DevInformation.iIndex,
            "DevicePath":ctypes.string_at(DevInformation.DevicePath),
            "UsbClass":DevInformation.UsbClass,
            "FuncType":DevInformation.FuncType,
            "DeviceID":DevInformation.DeviceID,
            "ChipMode":DevInformation.ChipMode,
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
def CH347GetVersion(iIndex:int=0)->Tuple[int,int,int,int]:
    iDriverVer=ctypes.c_ubyte()
    iDLLVer=ctypes.c_ubyte()
    ibcdDevice=ctypes.c_ubyte()
    iChipType=ctypes.c_ubyte()
    if LIBRARY.CH347GetVersion(ctypes.c_ulong(iIndex),ctypes.byref(iDriverVer),ctypes.byref(iDLLVer),ctypes.byref(ibcdDevice),ctypes.byref(iChipType)):
        return iDriverVer.value,iDLLVer.value,ibcdDevice.value,iChipType.value
    else:
        return -1,-1,-1,-1
def CH347SetTimeout(iIndex:int=0,iWriteTimeout:int=0xffffffff,iReadTimeout:int=0xffffffff)->bool:
    if LIBRARY.CH347SetTimeout(ctypes.c_ulong(iIndex),ctypes.c_ulong(iWriteTimeout),ctypes.c_ulong(iReadTimeout)):
        return True
    else:
        return False