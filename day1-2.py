# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:01:53 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x=900
y=900
z=900
mc.player.setTilePos(x,y,z)