# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:07:43 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
x,y,z=mc.player.getTilePos()
mc.player.setTilePos(x,y,z)
time.sleep(5)

x=x+100
mc.player.setTilePos(x,y,z)
time.sleep(5)

x=x+100
mc.player.setTilePos(x,y,z)