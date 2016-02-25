Title: Comandos útiles git
Category: Dev
date:  03-05-2013
Tags: git, deploy
Slug: git-interesting
Author: Sergi Collado
Summary: Algunos pequeños e útiles comandos de git
email:sergicollado@gmail.com

Algunos pequeños e útiles comandos de git que te hacen la vida más sencilla:

    #!bash
    #delete all removed files
    git rm $(git ls-files --deleted)

    #delete untracked files
    git clean -f
    #if you want to also remove directories, run
    git clean -f -d

    #ignore mode changes chmod
    git config core.filemode false
    # or global:
    git config --global core.filemode false







###Algunos enlaces interesantes sobre git:
* [deploying](http://wildlyinaccurate.com/deploying-a-git-repository-to-a-remote-server){:target="_blank"}


<a href="https://twitter.com/share" class="twitter-share-button" data-url="http://sergicollado.com/git-interesting.html" data-via="sergi_py" data-lang="es">Twittear</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>

![Hola](|filename|/images/posts/git.png)
