# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:33:28 2020

@author: user
"""


mc=Min
from mcpi.minecraft import Minecraftecraft.create()
import time

x,y,z = mc.player.getTilePos()

y = y + 100
mc.player.setTilePos(x,y,z)
time.set(10)

y = y + 100
mc.player.setTilePos(x,y,z)
time.set(10) 

y = y + 100
mc.player.setTilePos(x,y,z)
                                    