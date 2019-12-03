# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 14:19:56 2019
QQ群：476842922(欢迎加群讨论学习)
@author: Administrator
"""
import sys, os
from pynput.keyboard import Controller, Key, Listener


# 监听按压
def on_press(key):
    try:
        print("正在按压:", format(key.char))
    except AttributeError:
        print("正在按压:", format(key))


# 监听释放
def on_release(key):
    print("已经释放:", format(key))

    if key == Key.esc:
        # 停止监听
        return False


# 开始监听
def start_listen():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    # 实例化键盘
    kb = Controller()

    # 使用键盘输入一个字母
    kb.press('a')
    kb.release('a')

    # 使用键盘输入字符串,注意当前键盘调成英文
    kb.type("hello world")

    # 使用Key.xxx输入
    kb.press(Key.space)

    # 开始监听,按esc退出监听
    start_listen()
