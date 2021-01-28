# TLN-MIAGE-IA2-3

Voir rapport.pdf pour toutes les informations liées au projet.


# A result example : 

```
------------
Request : disease AND severe AND pneumonia

['diseas', 'and', 'sever', 'and', 'pneumonia']
[[0, 1, 2, 3, 4, 5, 6, 8, 9], 'and', [0, 1, 2, 3, 4, 5, 6, 8, 9], 'and', [0, 2, 6, 8]]
[[0, 1, 2, 3, 4, 5, 6, 8, 9], 'and', [0, 1, 2, 3, 4, 5, 6, 8, 9], 'and', [0, 2, 6, 8]]
[0, 2, 6, 8]
------------
Request : antibody AND plasma AND (cells OR receptors)

['antibodi', 'and', 'plasma', 'and', '(', 'cell', 'or', 'receptor', ')']
[[0, 1, 2, 3, 4, 6, 8, 9], 'and', [0, 1, 3, 4, 8], 'and', '(', [0, 1, 3, 4, 8, 9], 'or', [0, 2, 4, 8, 9], ')']
[[0, 1, 2, 3, 4, 6, 8, 9], 'and', [0, 1, 3, 4, 8], 'and', [0, 1, 3, 4, 8, 9, 0, 2, 4, 8, 9]]
[0, 1, 3, 4, 8]
------------
Request : antimalarial drugs OR antiviral agents OR immunomodulators

['antimalari', 'drug', 'or', 'antivir', 'agent', 'or', 'immunomodul']
[[0, 4], 'and', [0, 1, 3, 4, 6, 8], 'or', [0, 2, 3, 4, 8], 'and', [0, 1, 2, 3, 4], 'or', [3]]
[[0, 4], 'and', [0, 1, 3, 4, 6, 8], 'or', [0, 2, 3, 4, 8], 'and', [0, 1, 2, 3, 4], 'or', [3]]
[0, 4, 2, 3]
------------
Request : NOT plasma AND risk of infection AND restrictions

['not', 'plasma', 'and', 'risk', 'of', 'infect', 'and', 'restrict']
['not', [0, 1, 3, 4, 8], 'and', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'and', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'and', [0, 1, 2, 3, 4, 6, 7, 8, 9], 'and', [0, 6, 7, 8, 9]]
['not', [0, 1, 3, 4, 8], 'and', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'and', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'and', [0, 1, 2, 3, 4, 6, 7, 8, 9], 'and', [0, 6, 7, 8, 9]]
[6, 7, 9]
------------
Request : (older adults AND antibodies) AND NOT (genomes OR variant)

['(', 'older', 'adult', 'and', 'antibodi', ')', 'and', 'not', '(', 'genom', 'or', 'variant', ')']
['(', [0, 1, 2, 3, 4, 5, 9], 'and', [0, 1, 5, 8, 9], 'and', [0, 1, 2, 3, 4, 6, 8, 9], ')', 'and', 'not', '(', [0], 'or', [0, 4], ')']
[[0, 1, 9], 'and', 'not', [0, 0, 4]]
[1, 9]
------------
Request : antibody treatments

['antibodi', 'treatment']
[[0, 1, 2, 3, 4, 6, 8, 9], 'and', [0, 1, 2, 3, 4, 6, 8, 9]]
[[0, 1, 2, 3, 4, 6, 8, 9], 'and', [0, 1, 2, 3, 4, 6, 8, 9]]
[0, 1, 2, 3, 4, 6, 8, 9]
------------
Request : efficacy and safety of the treatments

['efficaci', 'and', 'safeti', 'of', 'the', 'treatment']
[[1, 2, 3, 4, 5, 9], 'and', [0, 1, 2, 3, 4], 'and', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'and', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'and', [0, 1, 2, 3, 4, 6, 8, 9]]
[[1, 2, 3, 4, 5, 9], 'and', [0, 1, 2, 3, 4], 'and', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'and', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'and', [0, 1, 2, 3, 4, 6, 8, 9]]
[1, 2, 3, 4]
------------
Request : family access to hospitals

['famili', 'access', 'to', 'hospit']
[[0, 1, 3, 7], 'and', [0, 1, 2, 3, 7, 8], 'and', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'and', [0, 1, 2, 3, 4, 6, 7, 8, 9]]
[[0, 1, 3, 7], 'and', [0, 1, 2, 3, 7, 8], 'and', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'and', [0, 1, 2, 3, 4, 6, 7, 8, 9]]
[0, 1, 3, 7]
------------
```
