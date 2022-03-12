import cv2
import pyautogui
import numpy as np
import win32gui
from PyQt5.QtWidgets import QApplication
import sys
import win32con
import Act

# 进入游戏窗口
hwnd = win32gui.FindWindow(None, u'PPSSPP v0.9.9.1-1505-gcf577e9 - ULJM05082 : STREET FIGHTER ZERO3 DOUBLE UPPER')
win32gui.SetForegroundWindow(hwnd)


# 截取游戏画面
def cut_picture():
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    # img.save('screenshow.jpg')
    return img


# 判断游戏画面
def judge_picture(img):  # 自己
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # cv2.imshow('hsv',hsv)
    # cv2.waitKey(0)
    purple_low = np.array([125, 43, 46])
    purple_high = np.array([155, 255, 255])
    img = cv2.inRange(hsv, purple_low, purple_high)

    img = cv2.GaussianBlur(img, (39, 39), 0)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(img)
    circle_done = img.copy()
    cv2.circle(circle_done, maxLoc, 59, (255, 0, 0), 2)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    return circle_done


def judge_picture_enemy(img):  # 敌人
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # cv2.imshow('hsv',hsv)
    # cv2.waitKey(0)
    red_low = np.array([0, 43, 46])
    red_high = np.array([10, 255, 255])
    img = cv2.inRange(hsv, red_low, red_high)

    img = cv2.GaussianBlur(img, (39, 39), 0)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(img)
    circle_done = img.copy()
    cv2.circle(circle_done, maxLoc, 59, (255, 0, 0), 2)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    return cv2.bitwise_not(circle_done)


# 逐帧分析
def cut_all_pictures():
    i = 0
    while win32gui.GetWindowText(
            hwnd) == u'PPSSPP v0.9.9.1-1505-gcf577e9 - ULJM05082 : STREET FIGHTER ZERO3 DOUBLE UPPER':
        imgs = cut_picture()
        imgs.save(f'G:\Pycharm_project\Sunset_Glow_01\imgs\imgs{i}.jpg')
        img0 = cv2.imread(f'G:\Pycharm_project\Sunset_Glow_01\imgs\imgs{i}.jpg')
        hsv_done = judge_picture(img0)
        cv2.imwrite(f'G:\Pycharm_project\Sunset_Glow_01\hsv_done\hsv_done{i}.jpg', hsv_done)
        hsv_done_enemy = judge_picture_enemy(img0)
        cv2.imwrite(f'G:\Pycharm_project\Sunset_Glow_01\hsv_done_enemy\hsv_done_enemy{i}.jpg', hsv_done_enemy)

        # hsv_done:自身状态   hsv_done_enemy:对手状态

        i += 1
        if i >= 200:
            break


cut_all_pictures()
