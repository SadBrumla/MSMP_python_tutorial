""" 
LEKCE 2: (podmínky, cykly a vizualizace) 

PREZENTACE - Comparisions
PREZENTACE - If / Else

""" 


""" 
PŘÍKLAD 1: Typ přeplňování a jednoduchý if elif else
Zadání: Kontrola typu přeplňování motoru. Vypočítej hodnoty v sání motoru 
pokud je proměnná preplnovani nastavená na "Turbodmychadlo", "Mechanické" nebo "Bez přeplňování"
do terminálu vypiš formátovaný text (viz 1. Lekce)

BONUS:
Otestuj, jestli tlak a teplota po následné adiabatické kompresi ve válci 
(poměr objemů je epsilon) nepřekročí maximální povolené úrovně pro daný motor. 
Použij logickou spojku AND nebo OR. Pokud hodnoty limit nepřesáhnou, vypiš je.

p_max = 5.5  # MPa
T_max = 1100 # °C
epsilon = 12 # Kompresní poměr

"""
p_atm = 101325 # Pa (standardní atmosférický tlak)
T_atm = 30     # °C
kappa = 1.4
stlaceni_TD = 2.2
stlaceni_mech = 2
preplnovani = "Turbodmychadlo" # Zkuste změnit na "Mechanické" nebo "Bez přeplňování"













"""
PREZENTACE - For loops

PŘÍKLAD 3: Výpočet účinnosti
Zadání: Na základě zadaných kompresních poměrů a teplot nasávaného vzduchu
(pro různé nadmořské výšky/stavy chlazení) vypočítejte pomocí vnořeného cyklu
termodynamickou účinnost Ottova cyklu: eta = 1 - (1 / (epsilon ** (kappa - 1))).
BONUS: 
- ulož hodnoty účinností do nového seznamu pomocí funkce .append
-přidej vnořený cyklus pro různé hodnoty kappa = [1.3 , 1.35 , 1.4]

"""
# Seznam zkoumaných kompresních poměrů (epsilon)
epsilon_hodnoty = [8, 9, 10, 11]
kappa = 1.4









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

