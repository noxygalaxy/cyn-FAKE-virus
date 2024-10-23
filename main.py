import os
import subprocess
import time
import ctypes
from ctypes import wintypes
from colorama import Fore, Style, init
import win32gui
import win32con
import requests
from pydub import AudioSegment
from pydub.playback import play
import io
import simpleaudio as sa
import threading
import math

init()

SWP_NOSIZE = 0x0001
SWP_NOMOVE = 0x0002
HWND_TOPMOST = -1

def center_console():
    user32 = ctypes.windll.user32
    kernel32 = ctypes.windll.kernel32
    
    console_handle = kernel32.GetConsoleWindow()

    if console_handle == 0:
        print("Failed to get console window handle.")
        return

    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)

    console_rect = ctypes.wintypes.RECT()
    user32.GetWindowRect(console_handle, ctypes.byref(console_rect))
    console_width = console_rect.right - console_rect.left
    console_height = console_rect.bottom - console_rect.top

    x = (screen_width - console_width) // 2
    y = (screen_height - console_height) // 2

    user32.MoveWindow(console_handle, x, y, console_width, console_height, True)

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,200,200,0)

def play_audio_from_url(url, volume_percentage):
    response = requests.get(url)
    response.raise_for_status()

    audio_data = io.BytesIO(response.content)
    audio_segment = AudioSegment.from_file(audio_data)

    volume_dB = 20 * math.log10(volume_percentage / 100) if volume_percentage > 0 else -float('inf')

    audio_segment = audio_segment + volume_dB

    play(audio_segment)

def play_audio_in_thread(url, volume_percentage):
    audio_thread = threading.Thread(target=play_audio_from_url, args=(url, volume_percentage))
    audio_thread.start()

audio_url = "https://audio.jukehost.co.uk/jBFhuFOSppRM5il9ZWcNUWM9p8GVlJTH"
play_audio_in_thread(audio_url, volume_percentage=10)

os.system('mode 75, 35')
os.system('title .')
light_yellow = "\033[38;2;238;250;75m"
center_console()

print(light_yellow + """                                    ███                                    
                                    ███                                    
                                   █████                                   
                                  ███████                                  
                                 █████████                                 
                                 █████████                                 
                                ███████████                                
                               █████████████                               
                                ███████████                                
                                    ███                                    
                                    ███                                    
                                    ███                                    
                                    ███                                    
                                    ███                                    
                                    ████                                   
                                    ████                                   
                                   █████                                   
                                 ██     ██                                 
                              ███  █████  ███                              
                           ███   █████████   ███                           
                          ██  ███████████████  ██                          
                          ██ █████████████████ ██                          
                          ██ █████████████████ ██                          
                          ██ █████████████████ ██                          
                          ██ █████████████████ ██                          
                         ████ ████████████████ ███                         
                      ████████   █████████    ███████                      
                    █████████████   ███   █████████████                    
         ████    ██████          ███   ███          ██████    ████         
       █████████████                ███                █████████████       
      ███████████                                         ███████████      
     ████████████                                         ████████████     
   ██████████████                                         ██████████████   
  ██████████████                                           ██████████████  
 ███████                                                           ███████""")

def cmd1():
    cmd_process = subprocess.Popen(r'start cmd /c "title SCANNING C:\WINDOWS\SYSTEM32 DIRECTORY... && tree /f"', cwd=r'C:\Windows\System32', shell=True)

    def find_cmd_window():
        time.sleep(0.2)
        EnumWindows = ctypes.windll.user32.EnumWindows
        EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
        GetWindowText = ctypes.windll.user32.GetWindowTextW
        GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
        IsWindowVisible = ctypes.windll.user32.IsWindowVisible

        titles = []
        def foreach_window(hwnd, lParam):
            if IsWindowVisible(hwnd):
                length = GetWindowTextLength(hwnd)
                buff = ctypes.create_unicode_buffer(length + 1)
                GetWindowText(hwnd, buff, length + 1)
                titles.append((hwnd, buff.value))
            return True

        EnumWindows(EnumWindowsProc(foreach_window), 0)

        for handle, title in titles:
            if r"SCANNING C:\WINDOWS\SYSTEM32 DIRECTORY..." in title:
                return handle
        return None

    max_attempts = 999
    for attempt in range(max_attempts):
        cmd_handle = find_cmd_window()
        if cmd_handle:
            ctypes.windll.user32.MoveWindow(cmd_handle, 250, 170, 600, 400, True)
            break
        if attempt == max_attempts - 1:
            print("Could not find the CMD window.")

def cmd2():
    cmd_process = subprocess.Popen(r'start cmd /c "title SCANNING C:\WINDOWS DIRECTORY... && tree /f"', cwd=r'C:\Windows', shell=True)

    def find_cmd_window():
        time.sleep(0.2)
        EnumWindows = ctypes.windll.user32.EnumWindows
        EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
        GetWindowText = ctypes.windll.user32.GetWindowTextW
        GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
        IsWindowVisible = ctypes.windll.user32.IsWindowVisible

        titles = []
        def foreach_window(hwnd, lParam):
            if IsWindowVisible(hwnd):
                length = GetWindowTextLength(hwnd)
                buff = ctypes.create_unicode_buffer(length + 1)
                GetWindowText(hwnd, buff, length + 1)
                titles.append((hwnd, buff.value))
            return True

        EnumWindows(EnumWindowsProc(foreach_window), 0)

        for handle, title in titles:
            if r"SCANNING C:\WINDOWS DIRECTORY" in title:
                return handle
        return None

    max_attempts = 999
    for attempt in range(max_attempts):
        cmd_handle = find_cmd_window()
        if cmd_handle:
            ctypes.windll.user32.MoveWindow(cmd_handle, 1200, 250, 600, 400, True)
            break
        if attempt == max_attempts - 1:
            print("Could not find the CMD window.")

def cmd3():
    cmd_process = subprocess.Popen(r'start cmd /c "title SCANNING C:\PROGRAM FILES DIRECTORY... && tree /f"', cwd=r'C:\Program Files', shell=True)

    def find_cmd_window():
        time.sleep(0.2)
        EnumWindows = ctypes.windll.user32.EnumWindows
        EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
        GetWindowText = ctypes.windll.user32.GetWindowTextW
        GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
        IsWindowVisible = ctypes.windll.user32.IsWindowVisible

        titles = []
        def foreach_window(hwnd, lParam):
            if IsWindowVisible(hwnd):
                length = GetWindowTextLength(hwnd)
                buff = ctypes.create_unicode_buffer(length + 1)
                GetWindowText(hwnd, buff, length + 1)
                titles.append((hwnd, buff.value))
            return True

        EnumWindows(EnumWindowsProc(foreach_window), 0)

        for handle, title in titles:
            if r"SCANNING C:\PROGRAM FILES DIRECTORY..." in title:
                return handle
        return None

    max_attempts = 999
    for attempt in range(max_attempts):
        cmd_handle = find_cmd_window()
        if cmd_handle:
            ctypes.windll.user32.MoveWindow(cmd_handle, 250, 666, 600, 400, True)
            break
        if attempt == max_attempts - 1:
            print("Could not find the CMD window.")

def cmd4():
    cmd_process = subprocess.Popen(r'start cmd /c "title SCANNING C:\WINDOWS\SYSWOW64... && tree /f"', cwd=r'C:\Windows\SysWOW64', shell=True)

    def find_cmd_window():
        time.sleep(0.2)
        EnumWindows = ctypes.windll.user32.EnumWindows
        EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
        GetWindowText = ctypes.windll.user32.GetWindowTextW
        GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
        IsWindowVisible = ctypes.windll.user32.IsWindowVisible

        titles = []
        def foreach_window(hwnd, lParam):
            if IsWindowVisible(hwnd):
                length = GetWindowTextLength(hwnd)
                buff = ctypes.create_unicode_buffer(length + 1)
                GetWindowText(hwnd, buff, length + 1)
                titles.append((hwnd, buff.value))
            return True

        EnumWindows(EnumWindowsProc(foreach_window), 0)

        for handle, title in titles:
            if r"SCANNING C:\WINDOWS\SYSWOW64..." in title:
                return handle
        return None

    max_attempts = 999
    for attempt in range(max_attempts):
        cmd_handle = find_cmd_window()
        if cmd_handle:
            ctypes.windll.user32.MoveWindow(cmd_handle, 1200, 682, 600, 400, True)
            break
        if attempt == max_attempts - 1:
            print("Could not find the CMD window.")

cmd2()

while True:
    cmd1()
    time.sleep(0.5)
    cmd3()
    time.sleep(10)
    cmd1()
    time.sleep(0.5)
    cmd4()
    time.sleep(10)
    cmd1()
    time.sleep(0.5)
    cmd3()
    time.sleep(10)
    cmd1()
    time.sleep(0.5)
    cmd4()
    time.sleep(10)
    cmd1()
    time.sleep(0.5)
    cmd3()
    time.sleep(10)
    cmd1()
    time.sleep(0.5)
    cmd4()
    time.sleep(10)
    cmd1()
    time.sleep(0.5)
    cmd3()
    time.sleep(10)
    cmd1()
    time.sleep(0.5)
    cmd4()
    time.sleep(10)
    cmd1()
    time.sleep(0.5)
    cmd3()
    time.sleep(10)
    cmd1()
    time.sleep(0.5)
    cmd4()
    time.sleep(10)
    cmd2()
    time.sleep(0.5)
