# -*- coding: utf-8 -*-
import platform

def type_system():
    # 判断操作系统，并将结果赋值于info
    info = platform.platform()
    # Windows操作系统返回结果为0
    if 'indows' in info:
        return 0
    # Ubuntu操作系统返回结果为1
    elif 'buntu' in info:
        return 1
    # Centos操作系统返回结果为2
    elif 'entos' in info:
        return 2
    # 其他类型操作系统返回结果为3
    else:
        return 3

if __name__ == "__main__":
    type_system()
