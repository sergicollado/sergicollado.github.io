Title: Test más semánticos en Python con Sure
Category: Dev
date:  08-05-2013
Tags: tdd, python, sure
Slug: sure
Author: Sergi Collado
Summary: Test más semánticos en Python con Sure
email:sergicollado@gmail.com


El módulo que incorpora python para hacer test unitarios es unittest,
con este, se puede empezar a hacer tdd fácilmente.
Personalmente prefiero la semántica de [repec](http://rspec.info/){:target="_blank"} que la de los asserts de xUnit,
La solución que yo he encontrado, es utilizar la librería [Sure](http://falcao.it/sure/){:target="_blank"}, inspirada en should.js.

Para instalarla es muy sencillo,

    :::bash
    user@machine:~$ [sudo] pip install sure

Es recomendable usar virtualenv para la instalación.


Una vez instalado podemos usarla  facilmente:

    :::python
    import sure

    (4).should.be.equal(2 + 2)
    (3).shouldnt.be.equal(5)

    #con colleciones
    {'foo': 'bar'}.should.equal({'foo': 'bar'})
    [].should.be.empty;
    "g".should.be.within("gabriel")

Lo mejor es leerse la documentación que está en la página del proyecto, pero como podéis leer es muy intuitivo.

Para usarlo en nuestros tests podemos  sustituir los asserts típicos de unittest por los de Sure:

    :::python
    import unittest
    import sure
    from map import *

    class TesTing(unittest.TestCase):

        def setUp(self):
            self.mapa = Map("textMap.tmx")

        def test_entorno(self):
            (4).should.be.equal(2 + 2)
            (5).should.be.greater_than(4)

        def test_intialitation_map(self):
            (self.mapa).should.be.an('map.Map')
            (self.mapa).should_not.be.empty()

    if __name__ == '__main__' :
        unittest.main(verbosity=2)


Si ponéis verbosity = 2 como argumento al arrancar unnittest.main veremos más datos al ejecutar los tests:

    :::bash
    test_entorno (__main__.TesTing) ... ok
    test_intialitation_map (__main__.TesTing) ... ok

    ----------------------------------------------------------------------
    Ran 2 tests in 0.201s

    OK





###Algunos enlaces interesantes sobre sure:
* [repec](http://rspec.info/){:target="_blank"}
* [Sure](http://falcao.it/sure/){:target="_blank"}
* [Tdd en python](http://css.dzone.com/articles/tdd-python-5-minutes){:target="_blank"}



<a href="https://twitter.com/share" class="twitter-share-button" data-url="http://sergicollado.com/sure.html" data-via="sergi_py" data-lang="es">Twittear</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>


![Hola](|filename|/images/posts/sure.png)
