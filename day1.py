# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:36:14 2020

@author: user
"""

from mcpi.minecraft import Minecraft

mc=Minecraft.create()
print(mc.player.getTilePos())