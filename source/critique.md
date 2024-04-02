(regard-critique)=

# Regard critique et améliorations


Ayant dû imposer une fin au projet, la version 1.0 de Flight Viewer possède encore bien des pistes d'améliorations. Ce chapitre en répertorie quelques-unes.

## Interface utilisateur

En ce qui concerne l'interface de l'application, je vois plusieurs évolutions possibles:

La plus importante serait de créer une interface utilisateur pour que ce dernier puisse choisir ses vols depuis le logiciel et non qu'il doive lui-même le mettre dans un dossier. Cette UI se composerait d'un pseudo-explorateur de fichier qui permettrait directement d'aller chercher le fichier trace là où il se trouve. 

Il devrait aussi y avoir une partie de l'UI qui s'occupe de la capture d'écran, et de l'enregistrer.


Un gros souci qui réside dans la version 1.0 est qu'il n'y a pas de message d'extension de carte. C'est dire que Flight Viewer possède des données uniquement pour une partie de la Gruyère et qu'il ne prévient pas quand il n'a pas les données d'un autre site. Bien qu'il soit aisé d'étendre les données topographiques à la main, en allant les chercher sur [swissALTI3D](https://www.swisstopo.admin.ch/fr/modele-altimetrique-swissalti3d), Flight Viewer devrait pouvoir le faire automatiquement dans ses versions futures. 

Le même problème se présente avec la minimap.


## Code

J'apporterai aussi sur le code quelques améliorations notamment sur le parthing des tuiles de la topographie dans `alti_data/`. Tout est regroupé dans un script, peu optimisé et moins modulé. Comme je considérais qu'il ne faisait pas à proprement parler parti du logiciel, j'ai laissé ceci un peu de côté.

## Conclusion

Durant la réalisation de ce projet, j'ai appris plusieurs choses. La principale est le perfectionnement dans la programmation orientée objet. Même au-delà de Python, ce bagage acquis me sera utile pour d'autres langages qui suivront dans mes études. 

En ce qui concerne le projet en lui-même, il reste certes de bonnes améliorations à apporter, mais la version 1.0 de **Flight Viewer** correspond à ce que j'avais en tête au début. Je n'avais même pas imaginé pouvoir faire une minimap et un panneau de commandes, ce qui montre que ce projet a même dépassé un peu mes attentes. Le rendu me plaît; j'apprécie la texture unie du relief en bref que cela ne soit pas le rendu d'une image satellite, on admire son vol avec un autre point de vue.
