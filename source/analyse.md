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
 * `Topo` s'occupe du relief. Les données qu'il récolte se trouvent dans le dossier `alti_data` sous forme d'une multitude de fichier. Chacun de ses fichiers correspond à une tuile du relief suisse d'1 km{sup}`2`. Chaque linge du fichier correspond une coordonnée x, une coordonnée y, et une altitude.


Ensuite, on instancie une `Camera` (de `camera.py`) qui s'occupe de placer la caméra dans l'espace et d'actualiser ses mouvements.
Dès lors que tout est chargé, on rentre dans la boucle principale qui 
 1. Contrôle les nouveaux événements (entrées au clavier, mouvement de curseur)
 2. Met à jour la caméra, les différents affichages et la résolution du terrain.
 3. Crée le rendu final de la frame. Cependant, si l'utilisateur n'a pas bougé on ne fait rien. En effet il ne sert à rien de créer un rendu parfaitement identique au précédent.
 4. Retarde le programme pour se limiter à 60 fps.

## Analyse poussée d'un bout de code
Analysons dans cette section ce que fait la class `Topo` de `model.py`.

Mais d'abord quelques remarques préliminaires. _OpenGL_ est une bibliothèque graphique 3D disponible en _Python_. Les fonctionnalités que nous utiliserons pour nos éléments graphiques sont principalement les outils de "dessin", notamment le processus `GL_TRIANGLES`, et les changements de couleur. Pour mieux comprendre prenons le code suivant :

```{code} python
a_lot_of_spacial_coordinates = [(1, 1, 1), (0.2, 2, 1.1), ...]
nb_triangles = len(a_lot_of_spacial_coordinates) // 3

glBegin(GL_TRIANGLES)

for i in range(nb_triangles):
    idx = 3 * i
    glColor3fv([1.,0,0])
    glVertex3fv(a_lot_of_spacial_coordinates[idx])
    glVertex3fv(a_lot_of_spacial_coordinates[idx + 1])
    glVertex3fv(a_lot_of_spacial_coordinates[idx + 2])

glEnd()
```

Ici on commence par se mettre en mode _dessin successif de triangles_(`GL_TRIANGLES`). Puis à chaque itération de la boucle `for`, _OpenGL_ crée un nouveau triangle de couleur rouge qui relie trois **Vertex**. C'est sur ce principe qu'on dessinera notre terrain, une succession de triangles mais de couleur calculée à partir du positionnement du triangle par rapport à la lumière.


Ainsi arrive le moment où l'on crée une instance `Topo` en passant en paramètre une liste de tuiles (càd dans quels fichiers d'`alti_data` il faudra aller regarder). 

**Pour chaque tuile**: L'instance commence par enregistrer tous les points de la tuile sous cette forme:
```{code} python
data_of_tileXX = [[(x1, y1, z11), (x2, y1, z21), ..., (xn, y1, zn1)],
                  [(x1, y2, z12), (x2, y2, z22), ..., (xn, y2, zn2)],
                                        ...
                  [(x1, yn, z1n), (x2, yn, z2n), ..., (xn, yn, znn)]]
```
Rappelons-nous qu'il nous faut dessiner des triangles. Pour l'instant nous n'avons qu'un tableau de points. L'astuce est de se faire une liste d'index qui pointeront savamment sur les bons éléments du tableau. Voici un exemple simplifié:

```{code} python
data_of_tile01 = [[a, b],
                  [c, d]] # avec a-d des points de l'espace

#triangles souhaités (a, b, d) (a, c, d)

idx_triangles = [[(0,0), (0,1), (1,1)], #pour (a, b, d)
                 [(0,0), (1,0), (1,1)]] #pour (a, c, d)
```
