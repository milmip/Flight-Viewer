(analyse)=

# Fonctionnement du code

## Arborescence du projet et résumé du fonctionnement
L'arborescence du projet se présente de la manière suivante:

```{code}
app
 ├── camera.py
 ├── main.py
 ├── model.py
 ├── parth.py
 ├── scene.py
 |
 ├── alti_data
 ├── img
 ├── map
 └── track
```

Expliquons dans les grandes lignes ce que fais notre programme. Tout commence dans `main.py`. On charge les paramètres de configuration avec _toml_. On initialise _pygame_ pour l'interaction avec l'utilisateur, et le moteur graphique _OpenGL_. On crée une instance `Scene` (implémentation dans `scene.py`) qui regroupera tous les éléments graphiques. Cette scène possède pour attribut les instances `Minimap`, `Help`, `Track`, `Topo`; ceci sont tous les éléments graphiques du programme (dans `model.py`).
 * `Minimap` s'occupe de la mini-carte, dont l'image brute se trouve dans le dossier `map`.
 * `Help` s'occupe de l'affichage de l'aide, dont l'image brute se trouve dans le dossier `img`.
 * `Track` s'occupe du tracé des vols. Dans les grandes lignes, il prend un fichier qu'on a disposé dans `my_flights`, s'il n'est déjà pas _parthed_ on le _parth_ et on l'enregistre dans le dossier `track`. Ensuite on charge le fichier _parthed_.
 * `Topo` s'occupe du relief. Les données qu'il récolte se trouvent dans le dossier `alti_data`.


Ensuite, on instancie une `Camera` (de `camera.py`) qui s'occupe de placer la caméra dans l'espace et d'actualiser ses mouvements.
Dès lors que tout est chargé, on rentre dans la boucle principale qui 
 1. Contrôle les nouveaux événements (entrées au clavier, mouvement de curseur)
 2. Met à jour la caméra, les différents affichages et la résolution du terrain.
 3. Crée le rendu final de la frame. Cependant, si l'utilisateur n'a pas bougé on ne fait rien. En effet il ne sert à rien de créer un rendu parfaitement identique au précédent.
 4. Retarde le programme pour se limiter à 60 fps.


