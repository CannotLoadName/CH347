#-*-coding:utf-8;-*-
from ctypes import byref,c_ubyte,c_ulong
from .core import LIBRARY,SPI_CONFIG
def CH347SPI_Init(iIndex:int,iMode:int,iClock:int,iByteOrder:int,iSpiWriteReadInterval:int,iSpiOutDefaultData:int,iChipSelect:int,CS1Polarity:int,CS2Polarity:int,iIsAutoDeativeCS:int,iActiveDelay:int,iDelayDeactive:int)->bool:
    SpiCfg=SPI_CONFIG(iMode,iClock,iByteOrder,iSpiWriteReadInterval,iSpiOutDefaultData,iChipSelect,CS1Polarity,CS2Polarity,iIsAutoDeativeCS,iActiveDelay,iDelayDeactive)
    return LIBRARY.CH347SPI_Init(iIndex,byref(SpiCfg))
CH347SPI_SetFrequency=LIBRARY.CH347SPI_SetFrequency
CH347SPI_SetDataBits=LIBRARY.CH347SPI_SetDataBits
def CH347SPI_GetCfg(iIndex:int)->dict:
    SpiCfg=SPI_CONFIG()
    if LIBRARY.CH347SPI_GetCfg(iIndex,byref(SpiCfg)):
        return {
            "iMode":SpiCfg.iMode,
            "iClock":SpiCfg.iClock,
            "iByteOrder":SpiCfg.iByteOrder,
            "iSpiWriteReadInterval":SpiCfg.iSpiWriteReadInterval,
            "iSpiOutDefaultData":SpiCfg.iSpiOutDefaultData,
            "iChipSelect":SpiCfg.iChipSelect,
            "CS1Polarity":SpiCfg.CS1Polarity,
            "CS2Polarity":SpiCfg.CS2Polarity,
            "iIsAutoDeativeCS":SpiCfg.iIsAutoDeativeCS,
            "iActiveDelay":SpiCfg.iActiveDelay,
            "iDelayDeactive":SpiCfg.iDelayDeactive
        }
    else:
        return {}
CH347SPI_ChangeCS=LIBRARY.CH347SPI_ChangeCS
CH347SPI_SetChipSelect=LIBRARY.CH347SPI_SetChipSelect
def CH347SPI_Write(iIndex:int,iChipSelect:int,iWriteStep:int,ioBuffer:bytes)->bool:
    return LIBRARY.CH347SPI_Write(iIndex,iChipSelect,len(ioBuffer),iWriteStep,byref((c_ubyte*len(ioBuffer))(*ioBuffer)))
def CH347SPI_Read(iIndex:int,iChipSelect:int,iLength:int,ioBuffer:bytes)->bytes:
    realIoBuffer=(c_ubyte*max(iLength,len(ioBuffer)))(*ioBuffer)
    if LIBRARY.CH347SPI_Read(iIndex,iChipSelect,len(ioBuffer),byref(c_ulong(iLength)),byref(realIoBuffer)):
        return bytes(realIoBuffer[:iLength])
    else:
        return b""
def CH347SPI_WriteRead(iIndex:int,iChipSelect:int,ioBuffer:bytes)->bytes:
    realIoBuffer=(c_ubyte*len(ioBuffer))(*ioBuffer)
    if LIBRARY.CH347SPI_WriteRead(iIndex,iChipSelect,len(ioBuffer),byref(realIoBuffer)):
        return bytes(realIoBuffer[:])
    else:
        return b""
def CH347StreamSPI4(iIndex:int,iChipSelect:int,ioBuffer:bytes)->bytes:
    realIoBuffer=(c_ubyte*len(ioBuffer))(*ioBuffer)
    if LIBRARY.CH347StreamSPI4(iIndex,iChipSelect,len(ioBuffer),byref(realIoBuffer)):
        return bytes(realIoBuffer[:])
    else:
        return b""