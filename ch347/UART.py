import ctypes
from ctypes.wintypes import DWORD
from .util import LIBRARY
def CH347Uart_Open(iIndex:int=0)->bool:
    if LIBRARY.CH347Uart_Open(ctypes.c_ulong(iIndex)):
        return True
    else:
        return False
def CH347Uart_Close(iIndex:int=0)->bool:
    if LIBRARY.CH347Uart_Close(ctypes.c_ulong(iIndex)):
        return True
    else:
        return False
def CH347Uart_Init(iIndex:int=0,BaudRate:int=9600,ByteSize:int=8,Parity:int=0,StopBits:int=0,ByteTimeout:int=0)->bool:
    if LIBRARY.CH347Uart_Init(ctypes.c_ulong(iIndex),DWORD(BaudRate),ctypes.c_ubyte(ByteSize),ctypes.c_ubyte(Parity),ctypes.c_ubyte(StopBits),ctypes.c_ubyte(ByteTimeout)):
        return True
    else:
        return False
def CH347Uart_SetTimeout(iIndex:int=0,iWriteTimeout:int=0xffffffff,iReadTimeout:int=0xffffffff)->bool:
    if LIBRARY.CH347Uart_SetTimeout(ctypes.c_ulong(iIndex),ctypes.c_ulong(iWriteTimeout),ctypes.c_ulong(iReadTimeout)):
        return True
    else:
        return False
def CH347Uart_Read(iIndex:int=0,ioLength:int=0)->bytes:
    oBuffer=(ctypes.c_ubyte*ioLength)()
    realIoLength=ctypes.c_ulong(ioLength)
    if LIBRARY.CH347Uart_Read(ctypes.c_ulong(iIndex),ctypes.byref(oBuffer),ctypes.byref(realIoLength)):
        return bytes(oBuffer[0:realIoLength.value])
    else:
        return b""
def CH347Uart_Write(iIndex:int=0,iBuffer:bytes=b"")->int:
    ioLength=ctypes.c_ulong(len(iBuffer))
    if LIBRARY.CH347Uart_Write(ctypes.c_ulong(iIndex),ctypes.byref((ctypes.c_ubyte*len(iBuffer))(*iBuffer)),ctypes.byref(ioLength)):
        return ioLength.value
    else:
        return -1
def CH347Uart_QueryBufUpload(iIndex:int=0)->int:
    RemainBytes=ctypes.c_longlong()
    if LIBRARY.CH347Uart_QueryBufUpload(ctypes.c_ulong(iIndex),ctypes.byref(RemainBytes)):
        return RemainBytes.value
    else:
        return -1