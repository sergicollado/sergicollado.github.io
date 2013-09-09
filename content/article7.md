Title: Javascript modular con RequireJs
Category: Javascript
date:  09-09-2013
Tags: Javascript, Front-End, RequireJs, Js, 
Slug: requireJs
Author: Sergi Collado
Summary: Empieza ha desarrollar javascript más modular con RequireJs


![RequireJs](|filename|/images/posts/requirejs.png)

[RequireJs](http://www.requirejs.org/){:target="_blank"} Es una librería Javascript que nos permite aislar modularmente los componentes de nuestra aplicación cliente.
Se gestiona a través de un punto único de entrada, ayudándonos a estructurar mejor nuestro código, en el que podremos definir las dependencias globales de nuestra aplicación, si es que son necesarias e incluso compilarlo todo en un único archivo.

Manos a la obra!  
Primero deberíamos descagar   [RequireJs](http://requirejs.org/docs/release/2.1.8/minified/require.js){:target="_blank"} de su web,
y organizar un poco la estructura de nuestra aplicación:

    :::shell
    /*
    root_app/
    ├── js
    │   ├── helpers
    │   │   └── utils.js
    │   ├── main.js
    │   ├── require.js
    │   └── vendor
    │       └── jquery-1.10.2.min.js
    └── index.html
    */

*root_app* es la raíz  donde vamos a trabajar, el archivo index.html es el que hará la llamada al scripts script principal de _requirejs_

    :::html
    <!DOCTYPE html>
    <html>
        <head>
            <title>My Project</title>
            <script data-main="js/main" src="js/require.js"></script>
        </head>
        <body>
            <h1>My  RequireJs Project</h1>
        </body>
    </html>

Como se puede observar en la etiqueta script enlazamos la librería _requirejs_ y en el atributo *data_main* enlazaremos nuestro script de entrada.

Vamos ahora a ir escribiendo nuestro script y viendo que todo ha ido como esperábamos.

    :::javascript
    require.config({
        baseUrl: 'js',
    });

En _baseUrl_ hemos configurado la ruta raíz de nuestra aplicación js, todos los archivos que añadamos a partir de aquí tendrán que ser relativos a la misma.
Yo normalmente uso jQuery, como podéis observar arriba, la he metido en la carpeta vendor, y ahora voy a añadirla a a require.config para poder usarla fácilmente:

    :::javascript
    require.config({
        baseUrl: 'js',
        paths: {
            jquery: 'vendor/jquery-1.10.2.min',
        }
    });

Ale, ya la tenemos a punto, simplemente la añadimos a paths, la clave es e nombre con el que queremos llamarla posteriormente,  *require* automáticamente le añade la teminación *.js* así que no debéis ponersela, acordáos de que la ruta debe partir de la que tengamos en *baseUrl*.

Ahora que ya tenemos un sencillo contexto configurado, vamos a crear un primer módulo y añadirlo a *main.js* debajo del config

    :::javascript
    requirejs(["helpers/utils"], function(Utils) {
        console.log(Utils.helloWorld);
    });

el método _requirejs_ admite como primer parámetro un array con las direcciones de los módulos que queramos utilizar dentro del mismo, como segundo parámetro tenemos una función que recibe como parámetros los mudulos descritos antes, es el momento de dar una buena semántica a los mismos. Así tenemos dentro de esta función un contexto único y aislado.

En el ejemplo de arriba yo le he pasado el módulo utils, que se encuentra dentro de la carpeta helpers, ahora  ya lo tenemos listo para usarse bajo el nombre Utils, en este caso es un simple objeto js clave valor, pero podría ser una función, una clase, etc ...

    :::javascript
    #helpers/utils
    define({
        helloWorld : 'hola'
    });

*utils.js* usa el modo más sencillo de crear un ḿodulo, como no depende de ningún otro módulo no necesitamos pasarlo como parámetro, es interesante que leáis en la documetación los distintos tipos de [módulos](http://requirejs.org/docs/api.html#funcmodule){:target="_blank"} que podéis hacer.

Por ejemplo, vamos a volver a *main.js* y usar jQuery en el módulo principal, quedaría así:

    :::javascript
    require.config({
        baseUrl: 'js',
        paths: {
            jquery: 'vendor/jquery-1.10.2.min',
        }
    });

    requirejs(['jquery', "helpers/utils"], function($, Util) {
        console.log(Util.helloWorls);
        console.log($);
    });

Como podéis ver, simplemente añadimos al array una cadena con el nombre que en *require.config* le hemos asignado como clave, luego lo ponemos como parámetro en la función anónima que ejecutará nuestro código. Ya tenemos disponible jQueryy lo podemos usar con el carácter $.

Ahora si vemos nuestro archivo *index.html* en un navegador, podremos observar como el console.log muestra 'hola' y la función de *jQuery*.

Si os habéis perdido, he subido los archivos a mi [git-hub](https://github.com/sergicollado/requirejs_tutorial){:target="_blank"} donde lé podréis echar un vistazo con más calma.

Esto es simplemente el comienzo, ahora solo os queda usar alguna librería de TDD como [Jasmine](http://pivotal.github.io/jasmine/){:target="_blank"} y no volver a hacer ese máldito código spaguetti que tanto cuesta de mantener, 

Y recordad que :
¡con javascript todo no vale!

Saludos!!


###Algunos enlaces interesantes:
* [RequireJs](http://www.requirejs.org/){:target="_blank"}



<a href="https://twitter.com/share" class="twitter-share-button" data-url="http://sergicollado.com/requireJs.html" data-via="circun4" data-lang="es">Twittear</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>



