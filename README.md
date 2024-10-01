
# PXML Reader

PXML Reader est un module python qui permet de lire un fichier .pxml. Basé sur le PXML de Progress Group, j'ai suivi le manifeste en provenance de Progress afin d'établir un reader automatique et simple qui fonctionne dans tout les cas.
[[Spécification PXML]](https://www.pxml.eu/PXML-Specification-1.3-EN.pdf)




## Authors

- [@faressofiane -- Sofiane Fares](https://github.com/FaresSofiane)
- [@Brisoz77 -- François BRIDONNEAU](https://github.com/Bridoz77)


## Usage/Examples

```python

from PXML_Reader import *


// lire un fichier
x = "//path/de/votre/fichier"
pxml_obj = pxml(x)
 
// pour modifier un fichier
pxml_obj.DocInfo.Comment = "test" // voir dans la documentation de PXML, la position de la valeur à changé

e = elementinfo.ElementInfo("test", True, "test", "test", "test", "test", 1, 1.0, 1.0, "test", "test", [])
e.ElementInfoVal.append(eleminfoval.ElemInfoVal(Type="test", V="test"))
pxml_obj.Order[0].Product[0].ElementInfo.append(e)

// Pour enregistrer le fichier

with open(x, 'w', encoding='UTF-8') as file:
        file.write(pxml_obj.__xml__())
```

