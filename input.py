#!/usr/bin/env python3

#################################
#
# Trying to learn to read input from a controller.
#
#
#################################


import sdl2.ext
import sys

RESOURCES = sdl2.ext.Resources('E:\Python34\Lib\site-packages\sdl2')

sdl2.ext.init()

window = sdl2.ext.Window("Hello World!", size=(640, 480))
window.show()

factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
sprite = factory.from_image(RESOURCES.get_path("hello.bmp"))

spriterenderer = factory.create_sprite_render_system(window)
spriterenderer.render(sprite)

processor = sdl2.ext.TestEventProcessor()
processor.run(window)

sdl2.ext.quit()



