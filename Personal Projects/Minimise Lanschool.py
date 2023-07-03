import ctypes
from ctypes import wintypes
from collections import namedtuple

user32 = ctypes.WinDLL('user32', use_last_error=True)

def check_zero(result, func, args):    
    if not result:
        err = ctypes.get_last_error()
        if err:
            raise ctypes.WinError(err)
    return args

if not hasattr(wintypes, 'LPDWORD'): # PY2
    wintypes.LPDWORD = ctypes.POINTER(wintypes.DWORD)

WindowInfo = namedtuple('WindowInfo', 'pid title')

WNDENUMPROC = ctypes.WINFUNCTYPE(
    wintypes.BOOL,
    wintypes.HWND,    # _In_ hWnd
    wintypes.LPARAM,) # _In_ lParam

user32.EnumWindows.errcheck = check_zero
user32.EnumWindows.argtypes = (
   WNDENUMPROC,      # _In_ lpEnumFunc
   wintypes.LPARAM,) # _In_ lParam

user32.IsWindowVisible.argtypes = (
    wintypes.HWND,) # _In_ hWnd

user32.GetWindowThreadProcessId.restype = wintypes.DWORD
user32.GetWindowThreadProcessId.argtypes = (
  wintypes.HWND,     # _In_      hWnd
  wintypes.LPDWORD,) # _Out_opt_ lpdwProcessId

user32.GetWindowTextLengthW.errcheck = check_zero
user32.GetWindowTextLengthW.argtypes = (
   wintypes.HWND,) # _In_ hWnd

user32.GetWindowTextW.errcheck = check_zero
user32.GetWindowTextW.argtypes = (
    wintypes.HWND,   # _In_  hWnd
    wintypes.LPWSTR, # _Out_ lpString
    ctypes.c_int,)   # _In_  nMaxCount



def list_windows():
    '''Return a sorted list of visible windows.'''
    result = []
    @WNDENUMPROC
    def enum_proc(hWnd, lParam):
        #if user32.IsWindowVisible(hWnd):
        pid = wintypes.DWORD()
        tid = user32.GetWindowThreadProcessId(
                    hWnd, ctypes.byref(pid))
        length = user32.GetWindowTextLengthW(hWnd) + 1
        title = ctypes.create_unicode_buffer(length)
        user32.GetWindowTextW(hWnd, title, length)
        result.append(WindowInfo(pid.value, title.value))
        return True
    user32.EnumWindows(enum_proc, 0)
    return sorted(result)

psapi = ctypes.WinDLL('psapi', use_last_error=True)

psapi.EnumProcesses.errcheck = check_zero
psapi.EnumProcesses.argtypes = (
   wintypes.LPDWORD,  # _Out_ pProcessIds
   wintypes.DWORD,    # _In_  cb
   wintypes.LPDWORD,) # _Out_ pBytesReturned

def list_pids():
    '''Return sorted list of process IDs.'''
    length = 4096
    PID_SIZE = ctypes.sizeof(wintypes.DWORD)
    while True:
        pids = (wintypes.DWORD * length)()
        cb = ctypes.sizeof(pids)
        cbret = wintypes.DWORD()
        psapi.EnumProcesses(pids, cb, ctypes.byref(cbret))
        if cbret.value < cb:
            length = cbret.value // PID_SIZE
            return sorted(pids[:length])
        length *= 2


import time

#Get Active  #https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-getactivewindow
#Set win     #https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-setwindowpos

#SetWindowPos FUNCTION
SetWindowPos = ctypes.windll.user32.SetWindowPos
SetWindowPos.restype = wintypes.BOOL
SetWindowPos.argtypes = [
    wintypes.HWND, #hWnd
    wintypes.HWND, #hWndInsertAfter
    ctypes.c_int,  #X #pos
    ctypes.c_int,  #Y #pos
    ctypes.c_int,  #cx #new width
    ctypes.c_int,  #cy #new height
    ctypes.c_uint, #uFlags
]
#

#FLAGS
SWP_HIDEWINDOW = 0x80 #HIDE 
SWP_SHOWWINDOW = 0x40 #SHOW
SWP_NOMOVE     = 0x0002 #NO MOVE
SWP_NOSIZE     = 0x0001 #NO SIZE


time.sleep(3)

def GetPIDsByTitle(title):
    windows = list_windows()
    pids = []
    for window in windows:
        pid, _title = list(window)

        if _title == title:
            pids.append(pid)

# HANDLE

windows = list_windows()
print(windows)

print("Minimising")

pids = GetPIDsByTitle("Lanschool Student")

def minimise(pids):
    for pid in pids:
        SetWindowPos(pid, 0, 0, 0, 100, 100, 0)

print("Minimised")


#EXAMPLE ON TOP -> because -> -1
#SetWindowPos(Active_W, -1, 0, 0, 0, 0,SWP_NOMOVE|SWP_NOSIZE )

#EXAMPLE ON TOP CANCEL -> because -> -2
#SetWindowPos(Active_W, -2, 0, 0, 0, 0,SWP_NOMOVE|SWP_NOSIZE )

#EXEMPLE DEPLACE     
#SetWindowPos(Active_W, 0, 2550, 0, 0, 0, SWP_NOSIZE )

#EXEMPLE RESIZE #column size
#SetWindowPos(Active_W, 0, 0, 0, 100, 1000, SWP_NOMOVE)
