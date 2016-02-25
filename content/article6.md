Title: Haystack, ElasticSearch en Django
Category: Dev
date:  23-08-2013
Tags: Django, python, elasticsearch, haystack
Slug: haystack
Author: Sergi Collado
Summary: Usar elasticksearch desde un proyecto web Django
email:sergicollado@gmail.com



![elasticsearch](|filename|/images/posts/elasticsearch.png)

[Elasticsearch](http://www.elasticsearch.org/){:target="_blank"} es una herramienta open source flexible y poderosa, un motor de búsquedas y analíticas real-time distribuido, cuyo corazón es el famoso proyecto Java Lucene.

En esta entrada no pretendo hacer un manual extenso sobre este magnífico proyecto open source, si no describir los pasos básicos que se deben seguir para usarlo en nuestras aplicaciones web Django, a través de [Haystack](http://haystacksearch.org/){:target="_blank"}

[Haystack](http://haystacksearch.org/) es una librería para Django que nos sirve para usar motores de búsqueda a través  de su API, se integra pefectamente con el workflow del Framework y nos permite usar varios motores como [Solr](http://lucene.apache.org/solr/){:target="_blank"},[whoosh](https://bitbucket.org/mchaput/whoosh/wiki/Home){:target="_blank"},etc...

Primero deberíamos instalar ElastickSearch, para ello vamos a su página de [descargas](http://www.elasticsearch.org/download/){:target=":_blank"} , allí bajamos la versión que nos interese, en mi caso como uso Ubuntu el .deb, y lo instalo en mi máquina.

Ahora tenemos que iniciarlo como servicio:

    :::shell
        sudo service elasticsearch start

        [sudo] password for sergi:
         * Starting ElasticSearch Server
           ...done.


Después necesitamos instalar unas pyelasticsearch y haystack en el virtualenv de nuestro proyecto:

    :::shell
        pip install pyelasticsearch
        pip install django-haystack

Añadimos Haystack a nuestro archivo de configuración de Django:

    :::python
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',

            # added
            'haystack',
        ]

Añadimos la configuración de elacticsearch también a nuestro settings.py

    :::python
        HAYSTACK_CONNECTIONS = {
            'default': {
                'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
                'URL': 'http://127.0.0.1:9200/',
                'INDEX_NAME': 'haystack',
            },
        }


Lo siguiente es indexar los modelos que queremos que aparezcan el las busquedas.
Para ello añadimos el archivo search_indexes.py en una de nuestras apps:

    :::python
        import datetime
        from haystack import indexes
        from .models import News


        class NewsIndex(indexes.SearchIndex, indexes.Indexable):
            text = indexes.CharField(document=True, use_template=True)

            #model fields
            caption = indexes.CharField(model_attr='caption')
            author = indexes.CharField(model_attr='author')
            created_at = indexes.DateTimeField(model_attr='created_at')

            def get_model(self):
                return News

            def index_queryset(self, using=None):
                """Used when the entire index for model is updated."""
                return self.get_model().objects.filter(created_at__lte=datetime.datetime.now())

En este caso en concreto estamos indexando el modelo news, el objeto SearchIndex es el modo en que Haystack determina que datos tendrá el índice.

Sólo puede haber un field con con el argumento document=True y es obligatorio, es el primer campo donde buscará.

Como añadido le podemos pasar el parámetro use_template=True, si lo hacemos tendremos que crear en el directorio dónde tengamos nuestras templates esta estructura de carpetas search/indexes/myapp/news_text.txt donde news_text.txt será el template  que use para guardar los datos indexados del modelo.

    :::python
        {{ object.caption }}
        {{ object.user.get_full_name }}
        {{ object.body }}

También, como en el ejemplo anterior, se pueden usar fields adicionales para añadir filtros adicionales.

Ahora sólo nos queda, añadir la url a nuestro URLconf

    :::python
        url(r'^search/', include('haystack.urls'))

La template que representará las búsquedas, en templates/search/search.html, que yo formateo con bootstrap jejeje:

    :::hmtl
        {% extends 'main.html' %}
        {% block main_content %}

        <div class='row'>
            <form method="get" action=".">
                <table>
                    {{ form.as_table }}
                    <tr>
                        <td>&nbsp;</td>
                        <td>
                            <input type="submit" value="Search">
                        </td>
                    </tr>
                </table>
            </form>
        </div>
        <div class="row">
            <div class="col-lg-12">
                    <h3>
                        Search Results
                    </h3>
                    {% for result in page.object_list %}
                    <ul>
                        <li>{{ result.object.caption }}
                            <img class="tumbnail" style="width:200px" src="{{ result.object.file.url }}">
                        </li>
                    </ul>
                    {% empty %}
                    <span>No results found.</span>
                    {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>

        {% endblock %}

Como podéis observar page.object_list es una lista de los objetos devueltos en la busqueda.
Ya sólo resta crear los indices nuevos desde manage.py:

    :::python
        ./manage.py rebuild_index

Una vez funcionando todo, podemos actualizar los índices, con el comando:

    :::python
        ./manage.py update_index


Y creo que no me dejo nada más, a mi me ha funcionado, ahora ya tienes la potencia de indexación de lucene en tu projecto web.

Saludos!!


###Algunos enlaces interesantes:
* [Elasticsearch](http://www.elasticsearch.org/download/){:target="_blank"}
* [Haystack](http://haystacksearch.org/){:target="_blank"}



<a href="https://twitter.com/share" class="twitter-share-button" data-url="http://sergicollado.com/haystack.html" data-via="sergi_py" data-lang="es">Twittear</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>



