Title: Extendiendo Model CActiveRecord
Category: Dev
date:  08-05-2013
Tags: php, Yii, ActiveRecord, extends
Slug: YiiExtendsModel
Author: Sergi Collado
Summary: Extendiendo Modelo CActiveRecord en Yii Framework
email:sergicollado@gmail.com


La mayoría de Frameworks para crear webs, nos sirven de gran ayuda a la hora de estructurar nuestro código y ayudarnos con miles de funcionalidades.
A veces estas ventajas se transforman en desventajas, dificultando la versatilidad de la toma de decisiones, haciéndonos perder más tiempo del que debíeramos.

Últimamente he usado el Framework Yii, en un par de proyectos.
En Yii se pueden crear módulos, widgets y componentes, así puedes descargar la lógica de los controladores, consiguiendo un código más legible.

Puedes encontrar el código en [MiGitHub](https://github.com/sergicollado/blog-examples/blob/master/CModelWithFile.php){:target="_blank"}

Cómo ejemplo me voy a centrar en una clase que he hecho estos días:

    :::php
    <?php
    //A field named 'file' is required'
    class CModelWithFile extends CActiveRecord{

        public $file_uploaded;

        public function saveWithImage($post){
            $this->attributes=$post;
            if(!$this->validate())
                return false;

            $this->saveFile();

            return $this->save();
        }

        private function saveFile(){
            $this->file_uploaded   =   CUploadedFile::getInstance($this,'file_uploaded');
            if(!$this->file_uploaded)
                return false;

            $this->file = '';
            $location_image = $this->getFileLocation();
            $this->file =  $this->moveFile($location_image,$this->file_uploaded);
        }

        private function moveFile($folder,$file_uploaded){
            $image_name= md5($file_uploaded.'algoparacodificar').$file_uploaded;
            $image_name = strtolower($image_name);

            $this->createDirectory();
            $file_uploaded->saveAs($folder.$image_name);
            return $image_name;
        }

        private function getFileUrl(){
            return Yii::app()->getBaseUrl(true).'/images/'.get_class($this).'/';
        }
        private function getFileLocation(){
            return Yii::getPathOfAlias('webroot').'/images/'.get_class($this).'/';
        }

        public function showImageFile(){
            if($this->file): ?>
            <li class="span3">
                <a href="#" class="thumbnail" rel="tooltip" data-title="Imagen">
                <?php $root = $this->getFileUrl().$this->file; ?>
                    <img src="<?php echo $root;?>" />
                </a>
            </li>
            <?php endif;
        }

        private function createDirectory(){
            $directory = rtrim($this->getFileLocation(),'/');
            if (is_dir($directory))
                return true;

            mkdir($directory);

        }

    }


Un gran número de entidades tienen la necesidad de subir algún tipo de archivo.
Además Yii te ofrece una manera fácil de validar atributos que llegan de un post.
Si toda la lógica necesaria para ambas cosas las dejamos en un método del controlador, el resultado es un montón de código repetido.

Para que funcione esta clase, tendríamos que tener una columna de tipoo string llamada 'file';
El modo de uso es muy sencillo :

    :::php
    <?php
    if(isset($_POST['Project']))
    {
        if($model->saveWithImage($_POST['Project']))
            $this->redirect(array('view','id'=>$model->id));
    }

Podríamos sobreescribir los métodos getFileLocation y getFileUrl para modificar la carpeta dónde se guardará la imagen.

Me he permitido añadir la función createDirectory, que  detectaría automáticamente si existe la carpeta donde deseamos guardar los archivos y la crearía, por defecto la carpeta images/NombreDelModelo... eso sí, debería estar creada la carpeta images en la raíz.

También he incluido el método showImageFile, que nos serviría de manera sencilla para renderizar en html la imagen, cuando esta se encuentre disponible, por ejemplo en el formulario de actualización. Este método debería estar en un widget o similar, dada su funcionalidad.


###Algunos enlaces interesantes sobre Yii:
* [Yii](http://www.yiiframework.com/doc/guide/1.1/en/extension.create){:target="_blank"}



<a href="https://twitter.com/share" class="twitter-share-button" data-url="http://sergicollado.com/YiiExtendsModel.html" data-via="sergi_py" data-lang="es">Twittear</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>

![YiiLogo](|filename|/images/posts/yii.png)
