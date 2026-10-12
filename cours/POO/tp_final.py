"""
Vous modélisez un service de location urbaine “CityBike” avec des stations réparties en ville, des vélos (mécaniques et électriques), des usagers (standard et premium), des trajets enregistrés, et un gestionnaire du réseau.

Un vélo peut être verrouillé, déverrouillé, il peut parcourir des kilomètres, il est disponible ou indisponible
Nous avons plusieurs types de vélo: classique et électrique qui a une autonomie, un niveau de batterie, et nécessite des recharges (1%/km consommé)

Une station a un code, un nom et une capacité de vélos, il peut avoir un dépôt ou un retrait de vélo, un inventaire, un taux d’occupation, et des statistiques sur les types de vélo disponibles.

Un usager a un identifiant, un nom, est actif ou non, a un historique de trajets. Il peut être standard (2 trajets actifs maximum, ou premium trajet illimité

Un trajet a un identifiant, un vélo, un utilisateur, une station de départ et d’arrivée ainsi qu’une distance. Il peut démarrer, ce qui déverrouille le vélo et marque comme indisponible + utilisateur actif. Il peut se terminer à une station d’arrivée et la distance parcourue (maj de batterie, verrouille, etc.).

Mon gestionnaire de réseau permet l’ajout d’une station, d’un vélo ou d’un utilisateur, gère la création d’un trajet et la fin d’un trajet, gère des données de statistique avec des moyennes de saturation toutes stations confondues, trajets par utilisateurs, trajets par vélo, nombre de vélos disponibles (possible par station), total km parcourus par type de vélo et l’utilisateur avec le plus de kilomètres.
"""

