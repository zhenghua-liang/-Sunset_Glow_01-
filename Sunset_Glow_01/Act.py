import win32api
import win32con
import time
import win32gui

# 进入游戏窗口
hwnd = win32gui.FindWindow(None, u'PPSSPP v0.9.9.1-1505-gcf577e9 - ULJM05082 : STREET FIGHTER ZERO3 DOUBLE UPPER')
win32gui.SetForegroundWindow(hwnd)

key_map = {
    "W": 87, "S": 83, "A": 65, "D": 68,  # W S A D分别对应↑ ↓ ← →
    "J": 74, "K": 75, "L": 76,  # J K L 分别对应轻拳 中拳 重拳
    "U": 85, "I": 73, "O": 79,  # U I O 分别对应轻腿 中腿 重腿
}
interval = 0.2


def key_down(key):  # 按下键盘上的按键
    key = key.upper()
    vk_code = key_map[key]
    win32api.keybd_event(vk_code, win32api.MapVirtualKey(vk_code, 0), 0, 0)


def key_up(key):  # 松开键盘上的按键
    key = key.upper()
    vk_code = key_map[key]
    win32api.keybd_event(vk_code, win32api.MapVirtualKey(vk_code, 0), win32con.KEYEVENTF_KEYUP, 0)


def key_press(key, interval):  # 按下按键的间隔时间
    key_down(key)
    time.sleep(interval)
    key_up(key)


def key_one(key, interval):
    key_down(key)
    time.sleep(interval)
    key_up(key)


def key_two(key1, key2, interval1, interval2):
    key_down(key1)
    time.sleep(interval1)
    key_down(key2)
    time.sleep(interval2)
    key_up(key1)
    key_up(key2)


# 我道拳（左）
def wodaoquan_left(uio):
    key_down('S')
    time.sleep(interval * 0.08)
    key_down('D')
    key_up('S')
    time.sleep(interval * 0.08)
    key_up('D')
    key_one(uio, interval)


# 我道拳（右）
def wodaoquan_right(uio):
    key_down('S')
    time.sleep(interval * 0.08)
    key_down('A')
    key_up('S')
    time.sleep(interval * 0.08)
    key_up('A')
    key_one(uio, interval)


# 晃龙拳（左）
def huanglongquan_left(uio):
    key_one('D', interval * 0.08)
    key_down('S')
    time.sleep(interval * 0.06)
    key_down('D')
    time.sleep(interval * 0.06)
    key_one(uio, interval)
    time.sleep(interval * 0.06)
    key_up('S')
    key_up('D')


# 晃龙拳（右）
def huanglongquan_right(uio):
    key_one('A', interval * 0.08)
    key_down('S')
    time.sleep(interval * 0.06)
    key_down('A')
    time.sleep(interval * 0.06)
    key_one(uio, interval)
    time.sleep(interval * 0.06)
    key_up('A')
    key_up('A')


# 断空脚（左）
def duankongjiao_left(jkl):
    key_down('S')
    time.sleep(interval * 0.09)
    key_down('A')
    key_up('S')
    time.sleep(interval * 0.09)
    key_up('A')
    key_one(jkl, interval)


# 断空脚（右）
def duankongjiao_right(jkl):
    key_down('S')
    time.sleep(interval * 0.09)
    key_down('D')
    key_up('S')
    time.sleep(interval * 0.09)
    key_up('D')
    key_one(jkl, interval)


# 超杀 晃龙烈火（左）
def sc_huanglong_left(jkl):
    key_down('S')
    time.sleep(interval * 0.08)
    key_down('D')
    key_up('S')
    time.sleep(interval * 0.08)
    key_up('D')
    key_down('S')
    time.sleep(interval * 0.08)
    key_down('D')
    key_up('S')
    time.sleep(interval * 0.08)
    key_up('D')
    key_one(jkl, interval)


# 超杀 晃龙烈火（右）
def sc_huanglong_right(jkl):
    key_down('S')
    time.sleep(interval * 0.08)
    key_down('A')
    key_up('S')
    time.sleep(interval * 0.08)
    key_up('A')
    key_down('S')
    time.sleep(interval * 0.08)
    key_down('A')
    key_up('S')
    time.sleep(interval * 0.08)
    key_up('A')
    key_one(jkl, interval)


# 超杀 震空我道（左）
def sc_wodao_left(uio):
    key_down('S')
    time.sleep(interval * 0.08)
    key_down('D')
    key_up('S')
    time.sleep(interval * 0.08)
    key_up('D')
    key_down('S')
    time.sleep(interval * 0.08)
    key_down('D')
    key_up('S')
    time.sleep(interval * 0.08)
    key_up('D')
    key_one(uio, interval)


# 超杀 震空我道（右）
def sc_wodao_right(uio):
    key_down('S')
    time.sleep(interval * 0.08)
    key_down('A')
    key_up('S')
    time.sleep(interval * 0.08)
    key_up('A')
    key_down('S')
    time.sleep(interval * 0.08)
    key_down('A')
    key_up('S')
    time.sleep(interval * 0.08)
    key_up('A')
    key_one(uio, interval)


# 超杀 必胜无赖拳（左）
def sc_bisheng_left(jkl):
    key_down('S')
    time.sleep(interval * 0.08)
    key_down('A')
    key_up('S')
    time.sleep(interval * 0.08)
    key_up('A')
    key_down('S')
    time.sleep(interval * 0.08)
    key_down('A')
    key_up('S')
    time.sleep(interval * 0.08)
    key_up('A')
    key_one(jkl, interval)


# 超杀 必胜无赖拳（右）
def sc_bisheng_righe(jkl):
    key_down('S')
    time.sleep(interval * 0.08)
    key_down('D')
    key_up('S')
    time.sleep(interval * 0.08)
    key_up('D')
    key_down('S')
    time.sleep(interval * 0.08)
    key_down('D')
    key_up('S')
    time.sleep(interval * 0.08)
    key_up('D')
    key_one(jkl, interval)


# 保持移动（单一方向）
def move_onekey_away(key):
    key_down(key)


# 终止移动（单一方向）
def move_onekey_put(key):
    key_up(key)


# 保持移动（双方向）
def move_twokey_away(key1, key2):
    key_down(key1)
    key_down(key2)


# 终止移动（双方向）
def move_twokey_put(key1, key2):
    key_up(key1)
    key_up(key2)


# 拳脚攻击
def attack(key):
    key_press(key)

