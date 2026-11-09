""" 
PREZENTACE - Modules and Packages (jako minule MATH)
PREZENTACE - PIP a PyPI, ukázat https://pypi.org/

PŘÍKLAD 4: Výpočet charakteristiky motoru a základní graf
Zadání: Z naměřených hodnot točivého momentu a otáček (pro 11 pracovních bodů)
vypočítejte efektivní výkon motoru (Pe v kW) a střední efektivní tlak (pe v barech). 
Doplňte cyklus pro výpočet, výsledky vypište a na závěr vykreslete základní graf 
pomocí knihovny matplotlib.
výkon Pe = Mt * n / 9550
tlak  pe = 120 * Pe / (V_z * n)
""" 

import matplotlib.pyplot as plt

# Vstupní data (realistické hodnoty pro přeplňovaný motor 2.0 TSI)
n = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000] # Otáčky [ot/min]
Mt = [200, 320, 320, 320, 320, 320, 320, 310, 290, 260, 220]           # Točivý moment [Nm]
V_z = 2                                                            # Zdvihový objem [dm3]

Pe_list = []
pe_list = []