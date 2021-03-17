import sys
import os
import subprocess

version = 1.0

def winver():
    os.system('winver')
    global banner
    print(banner+"\nНажмите ENTER для выхода в главное меню")
    input()

def panelcontrol():
    os.system('control')
    global banner
    print(banner+"\nНажмите ENTER для выхода в главное меню")
    input()

def settingInet():
    global banner
    menu = input(banner+'\n1 - Открыть "Панель управления" (NEW)\n2 - Открыть "Панель управления" (OLD)\n\n0 - Выход\n')
    if menu == "0": return()
    if menu == "1": PanelNEW()
    if menu == "2": PanelOLD()

def PanelNEW():
    os.system('explorer.exe ms-settings:network')
    global banner
    print(banner+"\nНажмите ENTER для выхода в главное меню")
    input()

def PanelOLD():
    os.system('explorer.exe shell:::{992CFFA0-F557-101A-88EC-00DD010CCC48}')
    global banner
    print(banner+"\nНажмите ENTER для выхода в главное меню")
    input()

def systeminf():
    subprocess.call('start /wait python systeminf.py', shell=True)
    global banner
    print(banner+"\nНажмите ENTER для выхода в главное меню")
    input()

def progrmandcomp():
    os.system('appwiz.cpl')
    global banner
    print(banner+"\nНажмите ENTER для выхода в главное меню")
    input()

def ipinfo():
    subprocess.call('start /wait python ipinfo.py', shell=True)
    global banner
    print(banner+"\nНажмите ENTER для выхода в главное меню")
    input()

def opappdata():
    os.system('explorer.exe %APPDATA%')
    global banner
    print(banner+"\nНажмите ENTER для выхода в главное меню")
    input()

def resexplorer():
    os.system('taskkill /f /IM explorer.exe')
    os.system('start explorer.exe')
    global banner
    print(banner+"\nНажмите ENTER для выхода в главное меню")
    input()

def regeditopen():
    os.system('regedit')
    global banner
    print(banner+"\nНажмите ENTER для выхода в главное меню")
    input()

def getmac():
    subprocess.call('start /wait python getmac.py', shell=True)
    global banner
    print(banner+"\nНажмите ENTER для выхода в главное меню")
    input()

def defender_start():
    os.system('C:\Windows\System32\SecurityHealthSystray.exe -explorer.exe')
    global banner
    print(banner+'\n"Windows Defender" был успешно запущен и перемещён в трей.\n\nНажмите ENTER для выхода в главное меню')
    input()

def info():
    global banner, version
    print(banner+"\nВерсия "+str(version)+"\n\nЗа все действия с программой отвечаете только вы!\n\nСоздатель Telegram - @avencores\n\nНажмите ENTER чтобы выйти")
    input()

while True:
    banner = ("\n" * 100)+ """
__        _____ _   _     ____            _             _
\ \      / /_ _| \ | |   / ___|___  _ __ | |_ _ __ ___ | |
 \ \ /\ / / | ||  \| |  | |   / _ \| '_ \| __| '__/ _ \| |
  \ V  V /  | || |\  |  | |__| (_) | | | | |_| | | (_) | |
   \_/\_/  |___|_| \_|   \____\___/|_| |_|\__|_|  \___/|_|

Telegram Channel: t.me/hzfnews
VK: vk.com/hzforum1
    """

    print(banner)
    menu = input('1 - Посмотреть версию Windows (WinVer)\n2 - Запустить "Панель управления"\n3 - Запустить "Настройки сети"\n4 - Запустить "Программы и компоненты"\n5 - Информация о системе\n6 - Узнать своё ip\n7 - Открыть папку AppData\n8 - Перезапустить explorer.exe\n9 - Запустить regedit.exe\n10 - Узнать mac адрес устройств совместимых со стандартами IEEE 802\n11 - Запустить "Windows Defender"\n\n12 - Важная информация!\n\n0 - Выход\n')
    if menu == "0": exit()
    if menu == "1": winver()
    if menu == "2": panelcontrol()
    if menu == "3": settingInet()
    if menu == "4": progrmandcomp()
    if menu == "5": systeminf()
    if menu == "6": ipinfo()
    if menu == "7": opappdata()
    if menu == "8": resexplorer()
    if menu == "9": regeditopen()
    if menu == "10": getmac()
    if menu == "11": defender_start()
    if menu == "12": info()
