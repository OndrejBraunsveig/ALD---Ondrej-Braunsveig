Na začátku programu si vytvořím hrací plochu, která je naplněná čísly -1. Poté začnu projíždět hrací plochu tak, že první projedu všechny sloupce řádku a pak se přesunu na další řádek. Při každém posunu kontroluju políčka na předchozím sloupci a řádku a ověřuji jestli se napojují na právě zvolené políčko (takže jestli se napojují zleva a ze shora). Podle toho zda-li se napojují či nikoliv vyřadím políčka, které nejsou kompatibilní s políčkem vlevo a nahoře (2 funkce, jedna kontroluje levého souseda a druhá horního souseda). Po kontrole mi zbydou všechna kompatibilní políčka, z nich následně jedno náhodně vyberu a dosadím ho do hrací plochy (každý druh políčka reprezentují čísla 0-12).

Jakmile je algoritmus dokončen, tak vygeneruji GUI s vizuálním zobrazením vygenerované hrací plochy. Políčka do GUI vkládám jako JPG.
Spuštěním programu se automaticky vygeneruje hrací plocha i GUI.


Solo práce - Ondřej Braunšveig
