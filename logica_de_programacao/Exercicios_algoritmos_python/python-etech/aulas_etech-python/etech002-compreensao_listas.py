from collections import namedtuple
from datetime import date

resident = namedtuple('residentes', ['nome', 'especie', 'salario', 'sexo', 'nascimento'])

f1 = resident(nome='Alex', especie='humano', salario=2100, sexo='M', nascimento=date(1998, 9, 24))
f2 = resident(nome='Si', especie='humano', salario=4000, sexo='F', nascimento=date(1999, 11, 17))
f3 = resident(nome='Pheobe', especie='felino', salario=10000, sexo='F', nascimento=date(2018, 2, 15))
f4 = resident(nome='Nala', especie='felino', salario=2100, sexo='F', nascimento=date(2019, 5, 12))
f5 = resident(nome='Pastel', especie='felino', salario=2100, sexo='F', nascimento=date(2019, 5, 12))

residentes = []

for l in range(0, 5):
    residentes.append(f1)
    residentes.append(f2)
    residentes.append(f3)
    residentes.append(f4)
    residentes.append(f5)
    print(residentes[l])

