import pyglet


def GifRoxy():
    # pick an animated gif file you have in the working directory
    ag_file = "Personal Voice Assistant.gif"
    animation = pyglet.resource.animation(ag_file)
    sprite = pyglet.sprite.Sprite(animation)

    # create a window and set it to the image size
    win = pyglet.window.Window(width=sprite.width, height=sprite.height, caption="Virtual Assistance Roxy")

    @win.event
    def on_draw():
        win.clear()
        sprite.draw()
    pyglet.app.run()


GifRoxy()
