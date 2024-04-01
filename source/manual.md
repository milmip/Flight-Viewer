(manual)=

# Manuel d'utilisation
## Avant de lancer Flight Viewer
Evidemment, l'utilisateur doit impérativement enregistrer son vol. Sur le site de décollage, il allumera son variomètre avec altimètre intégré et le couplera avec son téléphone via l'application _XCTrack_ par expemple. L'application utilisée importe peu, tant que le vol est enregistré au format `.igc`. Après son vol, l'utilisateur exporte le fichier de son téléphone vers son ordinateur. Il dépose finalement son vol dans le dossier `my_flights/` pour le traiter dans Flight Viewer.

Dans le dossier parent de l'application, `FlightViewer_1.0/`, l'utilisateur dispose de trois choses utiles: 
  1. Le dossier `my_flights/` pour qu'il y dispose les vols `.igc` qu'il souhaite voir. Il doit y figurer au moins un vol pour que l'application se lance. Maximum 20 vols !
  2. L'utilisateur pourra jouer avec certains paramètres du logiciel via le fichier `config.toml`.
  3. Finalement l'utilisateur lance le programme en exécutant le script `launch.sh`, dans un terminal ou avec un _clic droit_, _Exécuter comme un programme_. **Attention à bien rendre le fichier exécutable**.

```{figure} figure/Capture1.png
---
width: 50%
```
Avant de continuer, l'utilisateur aura pris le soin de télécharger les modules requis à **Flight Viewer** grâce à la commande suivante exécutée dans un terminal: 
```{code} bash
pip install PyOpenGL, numpy, pygame
```

## Flight Viewer
Une fois qu'on a placé le fichier qu'on désire au bon endroit, on lance le programme d'une des manière exposé plus haut. (Les utilisateurs qui possèdent encore un OS dont le terminal ne travail pas avec _bash_ trouveront le moyen de lancer le fichier `FlightViewer_1.0/app/main.py` avec `python3`.)

Le logiciel se met à charger, une fenêtre journalière de terminal s'ouvre.

L'utilisateur accède au panneau de commandes en tapant {kbd}`h`. Voici un résumé ici:
  * pour se mouvoir dans le plan, taper {kbd}`a`{kbd}`s`{kbd}`d`{kbd}`w`.
  * pour monter/descendre, taper {kbd}`space`{kbd}`alt`.
  * pour orienter la caméra, bouger la souris.
  * pour zoomer/dézoomer la minimap, taper {kbd}`q`{kbd}`e`.
  * pour cacher/montrer la minimap, taper {kbd}`c`.
  * pour montrer/cacher le relief étandu, taper {kbd}`v`. (Par soucis de fluidité, il est conseillé de se mouvoir en affichant le minimum de relief.)
  * pour quitter, taper {kbd}`alt` + {kbd}`f4`.
