# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:05:11 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat("你現在在X:"+str(x)+"y:"+str(y)+"z:"+str(z))
    time.sleep(1)


