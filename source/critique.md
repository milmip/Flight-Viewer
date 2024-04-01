(regard-critique)=

# Regard critique et améliorations


Ayant dû imposer une fin au projet, la version 1.0 de Flight Viewer possède encore bien des pistes d'améliorations. Ce chapitre en répertorie quelques unes.

## Interface utilisateur

En ce qui concerne l'interface de l'application, je vois plusieurs évolutions possibles:

La plus importante serait de crée une interface utilisateur pour que ce dernier puisse choisir ses vols depuis le logiciel et non qu'il doive lui-même le mettre dans un dossier. Cette UI se composerait d'un pseudo explorateur de fichier qui permettrait directement d'aller chercher le fichier trace là où il se trouve. 

Il devrait aussi y avoir une partie de l'UI qui s'occupe de la capture d'écran, et de l'enregistrer.


Un gros soucis qui réside dans la version 1.0 est qu'il n'y a pas de message d'extension de carte. C'est dire que Flight Viewer possède des données uniquement pour une partie de la Gruyère et qu'il ne prévient pas quand il n'a pas les données d'un autre site. Bien qu'il soit aisé d'étendre les données topographique à la main, en allant les chercher sur [swissALTI3D](https://www.swisstopo.admin.ch/fr/modele-altimetrique-swissalti3d), Flight Viewer devrait pouvoir le faire automatiquement dans ses versions futures. 

Le même problème se présente avec la minimap.


## Code

J'apporterai aussi sur le code quelques améliorations notamment sur le parthing des tuiles de la topographie dans `alti_data/`. Tout est regroupé dans un script, peu optimisé et moins modulé. Comme je considérais qu'il ne faisait pas à proprement parler parti du logiciel, j'ai laissé ceci un peu de côté.

