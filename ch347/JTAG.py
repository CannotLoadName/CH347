import ctypes
from .util import LIBRARY
def CH347Jtag_INIT(iIndex:int=0,iClockRate:int=0)->bool:
    if LIBRARY.CH347Jtag_INIT(ctypes.c_ulong(iIndex),ctypes.c_ubyte(iClockRate)):
        return True
    else:
        return False
def CH347Jtag_TmsChange(iIndex:int=0,tmsValue:bytes=b"",Skip:int=0)->bool:
    if LIBRARY.CH347Jtag_TmsChange(ctypes.c_ulong(iIndex),ctypes.byref((ctypes.c_ubyte*len(tmsValue))(*tmsValue)),ctypes.c_ulong(len(tmsValue)),ctypes.c_ulong(Skip)):
        return True
    else:
        return False
def CH347Jtag_IoScan(iIndex:int=0,DataBits:bytes=b"",IsRead:bool=False)->bool:
    if LIBRARY.CH347Jtag_IoScan(ctypes.c_ulong(iIndex),ctypes.byref((ctypes.c_ubyte*len(DataBits))(*DataBits)),ctypes.c_ulong(len(DataBits)),ctypes.c_bool(IsRead)):
        return True
    else:
        return False
def CH347Jtag_IoScanT(iIndex:int=0,DataBits:bytes=b"",IsRead:bool=False,IsLastPkt:bool=False)->bool:
    if LIBRARY.CH347Jtag_IoScanT(ctypes.c_ulong(iIndex),ctypes.byref((ctypes.c_ubyte*len(DataBits))(*DataBits)),ctypes.c_ulong(len(DataBits)),ctypes.c_bool(IsRead),ctypes.c_bool(IsLastPkt)):
        return True
    else:
        return False
def CH347Jtag_WriteRead(iIndex:int=0,IsDR:bool=False,iWriteBitBuffer:bytes=b"",oReadBitLength:int=0)->bytes:
    realOReadBitLength=ctypes.c_ulong(oReadBitLength)
    oReadBitBuffer=(ctypes.c_ubyte*oReadBitLength)()
    if LIBRARY.CH347Jtag_WriteRead(ctypes.c_ulong(iIndex),ctypes.c_bool(IsDR),ctypes.c_ulong(len(iWriteBitBuffer)),ctypes.byref((ctypes.c_ubyte*len(iWriteBitBuffer))(*iWriteBitBuffer)),ctypes.byref(realOReadBitLength),ctypes.byref(oReadBitBuffer)):
        return bytes(oReadBitBuffer[0:realOReadBitLength.value])
    else:
        return b""
def CH347Jtag_WriteRead_Fast(iIndex:int=0,IsDR:bool=False,iWriteBitBuffer:bytes=b"",oReadBitLength:int=0)->bytes:
    realOReadBitLength=ctypes.c_ulong(oReadBitLength)
    oReadBitBuffer=(ctypes.c_ubyte*oReadBitLength)()
    if LIBRARY.CH347Jtag_WriteRead_Fast(ctypes.c_ulong(iIndex),ctypes.c_bool(IsDR),ctypes.c_ulong(len(iWriteBitBuffer)),ctypes.byref((ctypes.c_ubyte*len(iWriteBitBuffer))(*iWriteBitBuffer)),ctypes.byref(realOReadBitLength),ctypes.byref(oReadBitBuffer)):
        return bytes(oReadBitBuffer[0:realOReadBitLength.value])
    else:
        return b""
def CH347Jtag_SwitchTapState(TapState:int=0)->bool:
    if LIBRARY.CH347Jtag_SwitchTapState(ctypes.c_ubyte(TapState)):
        return True
    else:
        return False
def CH347Jtag_ByteWriteDR(iIndex:int=0,iWriteBuffer:bytes=b"")->bool:
    if LIBRARY.CH347Jtag_ByteWriteDR(ctypes.c_ulong(iIndex),ctypes.c_ulong(len(iWriteBuffer)),ctypes.byref((ctypes.c_ubyte*len(iWriteBuffer))(*iWriteBuffer))):
        return True
    else:
        return False
def CH347Jtag_ByteReadDR(iIndex:int=0,oReadLength:int=0)->bytes:
    oReadBuffer=(ctypes.c_ubyte*oReadLength)()
    if LIBRARY.CH347Jtag_ByteReadDR(ctypes.c_ulong(iIndex),ctypes.byref(ctypes.c_ulong(oReadLength)),ctypes.byref(oReadBuffer)):
        return bytes(oReadBuffer)
    else:
        return b""
def CH347Jtag_ByteWriteIR(iIndex:int=0,iWriteBuffer:bytes=b"")->bool:
    if LIBRARY.CH347Jtag_ByteWriteIR(ctypes.c_ulong(iIndex),ctypes.c_ulong(len(iWriteBuffer)),ctypes.byref((ctypes.c_ubyte*len(iWriteBuffer))(*iWriteBuffer))):
        return True
    else:
        return False
def CH347Jtag_ByteReadIR(iIndex:int=0,oReadLength:int=0)->bytes:
    oReadBuffer=(ctypes.c_ubyte*oReadLength)()
    if LIBRARY.CH347Jtag_ByteReadIR(ctypes.c_ulong(iIndex),ctypes.byref(ctypes.c_ulong(oReadLength)),ctypes.byref(oReadBuffer)):
        return bytes(oReadBuffer)
    else:
        return b""
def CH347Jtag_BitWriteDR(iIndex:int=0,iWriteBuffer:bytes=b"")->bool:
    if LIBRARY.CH347Jtag_BitWriteDR(ctypes.c_ulong(iIndex),ctypes.c_ulong(len(iWriteBuffer)),ctypes.byref((ctypes.c_ubyte*len(iWriteBuffer))(*iWriteBuffer))):
        return True
    else:
        return False
def CH347Jtag_BitWriteIR(iIndex:int=0,iWriteBuffer:bytes=b"")->bool:
    if LIBRARY.CH347Jtag_BitWriteIR(ctypes.c_ulong(iIndex),ctypes.c_ulong(len(iWriteBuffer)),ctypes.byref((ctypes.c_ubyte*len(iWriteBuffer))(*iWriteBuffer))):
        return True
    else:
        return False
def CH347Jtag_BitReadIR(iIndex:int=0,oReadLength:int=0)->bytes:
    oReadBuffer=(ctypes.c_ubyte*oReadLength)()
    if LIBRARY.CH347Jtag_BitReadIR(ctypes.c_ulong(iIndex),ctypes.byref(ctypes.c_ulong(oReadLength)),ctypes.byref(oReadBuffer)):
        return bytes(oReadBuffer)
    else:
        return b""
def CH347Jtag_BitReadDR(iIndex:int=0,oReadLength:int=0)->bytes:
    oReadBuffer=(ctypes.c_ubyte*oReadLength)()
    if LIBRARY.CH347Jtag_BitReadDR(ctypes.c_ulong(iIndex),ctypes.byref(ctypes.c_ulong(oReadLength)),ctypes.byref(oReadBuffer)):
        return bytes(oReadBuffer)
    else:
        return b""