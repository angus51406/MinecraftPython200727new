# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:08:42 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x = 50.5
y = 50.5
z = 50.5
mc.player.setPos(x,y,z)