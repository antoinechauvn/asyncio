# asyncio
Approche sur la librairie de haut niveau Asyncio

## Différence entre parallélisme et concurrence

>Le parallélisme consiste à effectuer plusieurs opérations en même temps. Le multitraitement est un moyen d'effectuer le parallélisme et il implique la répartition des tâches sur les unités centrales de traitement (CPU ou cœurs) d'un ordinateur. Le multitraitement est bien adapté aux tâches liées au processeur : les boucles for étant étroitement liées et les calculs mathématiques entrent généralement dans cette catégorie.

>La concurrence est un terme légèrement plus large que le parallélisme. Cela suggère que plusieurs tâches ont la capacité de s'exécuter de manière chevauchante. (Il y a un dicton qui dit que la simultanéité n'implique pas le parallélisme.)

>Le threading est un modèle d'exécution simultanée dans lequel plusieurs threads exécutent des tâches à tour de rôle. Un processus peut contenir plusieurs threads. Python a une relation compliquée avec le threading grâce à son GIL , mais cela dépasse le cadre de cet article.

>Ce qu'il est important de savoir sur le threading, c'est qu'il est préférable pour les tâches liées aux E/S. Alors qu'une tâche liée au processeur est caractérisée par le fait que les cœurs de l'ordinateur travaillent continuellement du début à la fin, une tâche liée aux E/S est dominée par beaucoup d'attente sur les entrées/sorties pour se terminer.

>Pour récapituler ce qui précède, la simultanéité englobe à la fois le multitraitement (idéal pour les tâches liées au processeur) et le threading (adapté aux tâches liées aux E/S). Le multitraitement est une forme de parallélisme, le parallélisme étant un type (sous-ensemble) spécifique de concurrence. La bibliothèque standard Python offre depuis longtemps une prise en charge de ces deux éléments via ses packages multiprocessing, threading, et concurrent.futures.
