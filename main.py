#!/usr/bin/env python

from direct.showbase.ShowBase import ShowBase
base = ShowBase()

from panda3d.core import NodePath, TextNode
from direct.gui.DirectGui import *
import sys

class World(object):
    def __init__(self):
        self.title = OnscreenText(  # Create the title
            text="Solar System",
            parent=base.a2dBottomRight, align=TextNode.A_right,
            style=1, fg=(1, 1, 1, 1), pos=(-0.1, 0.1), scale=.07)

        base.setBackgroundColor(0, 0, 0)
        base.disableMouse()
        camera.setPos(0, 0, 45)
        camera.setHpr(0, -90, 0) #(heading, pitch, roll) in degrees
        self.sizescale = 1.0
        self.loadPlanets()

    def loadPlanets(self):
        # load skybox
        self.sky = loader.loadModel("models/solar_sky_sphere")
        self.sky.reparentTo(render)
        self.sky.setScale(40)
        self.sky_tex = loader.loadTexture("models/stars_1k_tex.jpg")
        self.sky.setTexture(self.sky_tex, 1)

        # load sun
        self.sun = loader.loadModel("models/planet_sphere")
        self.sun.reparentTo(render)
        self.sun_tex = loader.loadTexture("models/sun_1k_tex.jpg")
        self.sun.setTexture(self.sun_tex, 1)
        self.sun.setScale(self.sizescale)

w = World()
base.run()
