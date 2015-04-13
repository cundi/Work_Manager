# -*- coding: utf-8 -*-

from datetime import datetime


# return delta time
def get_delta_time(time_in):
    time_delta = datetime.today() - time_in
    day = time_delta.days
    sec = time_delta.seconds
    if day > 0:
        if day / 365 > 0:
            return '%d 年前' % (day/365)
        else:
            return '%d 天前' % (day%365)
    else:
        if sec < 60:
            return '1 分钟前'
        elif sec < 3600:
            return '%d 分钟前' % (sec/60)
        else:
            return '%d 小时 %d 分钟前' % (sec/3600, (sec%3600)/60)