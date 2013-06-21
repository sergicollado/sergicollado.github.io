Title: Librería tmxScene python-sfml python
Category: Dev
date:  20-06-2013
Tags: tmx, python, sfml, tmxScene, tiled
Slug: tmxscene
Author: Sergi Collado
Summary: Primeros pasos para renderizar entornos de tiles creados por Tiled


![sfml](|filename|/images/posts/sfml-logo.png)

Últimamente me he propuesto hacer juego en python y de paso probar [Python-sfml](http://www.python-sfml.org/index.html){:target="_blank"} que me parece muy interesante.

El primer paso ha consistedo en crear una librería para poder usar el maravilloso software [tiled](http://www.mapeditor.org/){:target="_blank"} y así editar los niveles del juego con toda la potencia que te da esta herramienta.

Su utilización es bastante sencilla, hasta que la empaquete y se pueda instalar mediante pip, simplemente debemos clonar el [repositorio](https://github.com/sergicollado/sceneTmx){:target="_blank"} el múdulo en cuestión se corresponde con la carpeta scene.

tmxScene tiene como dependecia el módulo tmxlib y lo he desarrollado en Python 2.7, se puede instalar fácilmente desde Pip:

    :::shell
        pip install tmxlib

El repositorio es en sí mismo un ejemplo de como se puede utilizar, puedes echar un vistazo al script de entrada main.py 

    :::python
        import sfml as sf
        from config import *
        import scene
        import character
        from scene.renderer import drawables

        width = 1280
        height = 820
        window = sf.RenderWindow(sf.VideoMode(width, height), "pySFML Window")
        window.framerate_limit = 60
        window.vertical_synchronization = True

        clock = sf.Clock()


        try:
            texture = sf.Texture.from_file(IMAGES_PATH+"twilight-tiles.png")
            
            sprites = drawables.Sprites()
            scene = scene.Scene(MAPS_PATH+"textMap.tmx", width, height, sprites)
            scene.set_images_path(IMAGES_PATH)
            layers = [
                {'name':'c2' , 'distance': 0.8},
                {'name':'c1' , 'distance': 1},
            ]
            scene.set_visible_layers(layers)

            
            player = character.Character(IMAGES_PATH+"mikeypebalz.png", 57,101, sprites)
            player.set_velocity(10)
        except IOError: 
            print IOError
            exit(1)

        while window.is_open:
            for event in window.events:

                if type(event) is sf.CloseEvent or sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
                    window.close()

                if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT):
                    scene.cam.panning_right()
                    player.horizontal_aceleration()

                if sf.Keyboard.is_key_pressed(sf.Keyboard.LEFT):
                    scene.cam.panning_left()
                    player.horizontal_deceleration() e

                if sf.Keyboard.is_key_pressed(sf.Keyboard.UP):
                    scene.cam.panning_top()

                if sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN):
                    scene.cam.panning_down()

            time  = clock.restart().seconds*10
            window.clear() 
            scene.update(time)
            scene.render(window)
            player.update(time)
            player.render(window)
            window.display() 
    
###Algunos enlaces interesantes:
* [tiled](http://www.mapeditor.org/){:target="_blank"}
* [repositorio](https://github.com/sergicollado/sceneTmx){:target="_blank"}
* [Python-sfml](http://www.python-sfml.org/index.html){:target="_blank"}



<a href="https://twitter.com/share" class="twitter-share-button" data-url="http://sergicollado.com/tmxscene.html" data-via="circun4" data-lang="es">Twittear</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>



