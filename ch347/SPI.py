import ctypes
from .util import LIBRARY
class SPI_CONFIG(ctypes.Structure):
    _fields_=[
        ("iMode",ctypes.c_ubyte),
        ("iClock",ctypes.c_ubyte),
        ("iByteOrder",ctypes.c_ubyte),
        ("iSpiWriteReadInterval",ctypes.c_ushort),
        ("iSpiOutDefaultData",ctypes.c_ubyte),
        ("iChipSelect",ctypes.c_ulong),
        ("CS1Polarity",ctypes.c_ubyte),
        ("CS2Polarity",ctypes.c_ubyte),
        ("iIsAutoDeativeCS",ctypes.c_ushort),
        ("iActiveDelay",ctypes.c_ushort),
        ("iDelayDeactive",ctypes.c_ulong)
    ]
def CH347SPI_Init(iIndex:int=0,iMode:int=3,iClock:int=1,iByteOrder:bool=False,iSpiWriteReadInterval:int=65280,iSpiOutDefaultData:int=0,iChipSelect:int=0,CS1Polarity:bool=False,CS2Polarity:bool=False,iIsAutoDeativeCS:int=0,iActiveDelay:int=0,iDelayDeactive:int=0)->bool:
    if LIBRARY.CH347SPI_Init(ctypes.c_ulong(iIndex),ctypes.byref(SPI_CONFIG(iMode,iClock,1 if iByteOrder else 0,iSpiWriteReadInterval,iSpiOutDefaultData,iChipSelect,1 if CS1Polarity else 0,1 if CS2Polarity else 0,iIsAutoDeativeCS,iActiveDelay,iDelayDeactive))):
        return True
    else:
        return False
def CH347SPI_SetDataBits(iIndex:int=0,iDataBits:bool=False)->bool:
    if LIBRARY.CH347SPI_SetDataBits(ctypes.c_ulong(iIndex),ctypes.c_ubyte(1 if iDataBits else 0)):
        return True
    else:
        return False
def CH347SPI_GetCfg(iIndex:int=0)->dict:
    SpiCfg=SPI_CONFIG()
    if LIBRARY.CH347SPI_GetCfg(ctypes.c_ulong(iIndex),ctypes.byref(SpiCfg)):
        return {
            "iMode":SpiCfg.iMode,
            "iClock":SpiCfg.iClock,
            "iByteOrder":True if SpiCfg.iByteOrder else False,
            "iSpiWriteReadInterval":SpiCfg.iSpiWriteReadInterval,
            "iSpiOutDefaultData":SpiCfg.iSpiOutDefaultData,
            "iChipSelect":SpiCfg.iChipSelect,
            "CS1Polarity":True if SpiCfg.CS1Polarity else False,
            "CS2Polarity":True if SpiCfg.CS2Polarity else False,
            "iIsAutoDeativeCS":SpiCfg.iIsAutoDeativeCS,
            "iActiveDelay":SpiCfg.iActiveDelay,
            "iDelayDeactive":SpiCfg.iDelayDeactive
        }
    else:
        return {}
def CH347SPI_ChangeCS(iIndex:int=0,iStatus:bool=False)->bool:
    if LIBRARY.CH347SPI_ChangeCS(ctypes.c_ulong(iIndex),ctypes.c_ubyte(1 if iStatus else 0)):
        return True
    else:
        return False
def CH347SPI_SetChipSelect(iIndex:int=0,iEnableSelect:int=0,iChipSelect:int=0,iIsAutoDeativeCS:int=0,iActiveDelay:int=0,iDelayDeactive:int=0)->bool:
    if LIBRARY.CH347SPI_SetChipSelect(ctypes.c_ulong(iIndex),ctypes.c_ushort(iEnableSelect),ctypes.c_ushort(iChipSelect),ctypes.c_ulong(iIsAutoDeativeCS),ctypes.c_ulong(iActiveDelay),ctypes.c_ulong(iDelayDeactive)):
        return True
    else:
        return False
def CH347SPI_Write(iIndex:int=0,iChipSelect:int=0,iWriteStep:int=1,ioBuffer:bytes=b"")->bool:
    if LIBRARY.CH347SPI_Write(ctypes.c_ulong(iIndex),ctypes.c_ulong(iChipSelect),ctypes.c_ulong(len(ioBuffer)),ctypes.c_ulong(iWriteStep),ctypes.byref((ctypes.c_ubyte*len(ioBuffer))(*ioBuffer))):
        return True
    else:
        return False
def CH347SPI_Read(iIndex:int=0,iChipSelect:int=0,iLength:int=0,ioBuffer:bytes=b"")->bytes:
    realIoBuffer=(ctypes.c_ubyte*max(iLength,len(ioBuffer)))(*ioBuffer)
    if LIBRARY.CH347SPI_Read(ctypes.c_ulong(iIndex),ctypes.c_ulong(iChipSelect),ctypes.c_ulong(len(ioBuffer)),ctypes.byref(ctypes.c_ulong(iLength)),ctypes.byref(realIoBuffer)):
        return bytes(realIoBuffer[0:iLength])
    else:
        return b""
def CH347SPI_WriteRead(iIndex:int=0,iChipSelect:int=0,ioBuffer:bytes=b"")->bytes:
    realIoBuffer=(ctypes.c_ubyte*len(ioBuffer))(*ioBuffer)
    if LIBRARY.CH347SPI_WriteRead(ctypes.c_ulong(iIndex),ctypes.c_ulong(iChipSelect),ctypes.c_ulong(len(ioBuffer)),ctypes.byref(realIoBuffer)):
        return bytes(realIoBuffer)
    else:
        return b""
def CH347StreamSPI4(iIndex:int=0,iChipSelect:int=0,ioBuffer:bytes=b"")->bytes:
    realIoBuffer=(ctypes.c_ubyte*len(ioBuffer))(*ioBuffer)
    if LIBRARY.CH347StreamSPI4(ctypes.c_ulong(iIndex),ctypes.c_ulong(iChipSelect),ctypes.c_ulong(len(ioBuffer)),ctypes.byref(realIoBuffer)):
        return bytes(realIoBuffer)
    else:
        return b""