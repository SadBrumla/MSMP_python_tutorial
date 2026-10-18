"""
LEKCE 1 - SAMOSTATNÁ CVIČENÍ A ÚKOLY
Doplňte kód pod příslušná zadání.
"""

"""
ÚKOL 1: Proměnné a datové typy
Zadání:
Nadefinujte proměnné pro moderní tříválcový motor 1.0 TSI.
1. Vytvořte proměnnou pro název motoru.
2. Vytvořte proměnnou pro počet válců (3).
3. Vytvořte proměnné pro vrtání (74.5 mm) a zdvih (76.4 mm).
4. Pomocí funkce type() si vypište na obrazovku a ověřte, že počet válců 
   je celočíselný typ (int) a vrtání je desetinné číslo (float).
"""
# Sem napište kód pro Úkol 1:





"""
ÚKOL 2: Matematika a vzorce
Zadání:
Máme zadaný kompresní objem jednoho válce V_c = 0.000045 m3.
1. Vypočítejte zdvihový objem jednoho válce V_z v m3 (použijte vrtání a zdvih z Úkolu 1).
   Nezapomeňte milimetry nejprve převést na metry. Zadejte 'import math' pro číslo pí.
2. Vypočítejte kompresní poměr epsilon. Vzorec: epsilon = (V_z + V_c) / V_c
3. Vypočítejte střední pístovou rychlost c_s [m/s] při otáčkách n = 4000 min-1.
   Vzorec: c_s = 2 * z * (n / 60), kde z je zdvih v metrech.
"""
V_c = 0.000045
n_otacky = 4000
# Sem napište kód pro Úkol 2:




"""
ÚKOL 3: Formátovaný výstup (F-stringy)
Zadání:
Vypište na obrazovku hezky zformátovanou větu, která bude obsahovat 
vypočtený kompresní poměr (zaokrouhlený na 1 desetinné místo) a 
střední pístovou rychlost (zaokrouhlenou na 2 desetinná místa) z Úkolu 2.
"""
# Sem napište kód pro Úkol 3:




"""
ZÁVĚREČNÝ ÚKOL: Termodynamický oběh (Sabatheho/Dual cycle)
Zadání:
Sabatheho oběh kombinuje izochorický i izobarický přívod tepla.
Vaším úkolem je dopočítat stavové veličiny (tlak p, teplotu T, objem v) pro body 1 až 5.

- Bod 1: Sání (výpočet 'v1' ze stavové rovnice)
- Bod 2: Izoentropická komprese (v2 = v1/eps, p2 = p1*eps^kappa, T2 = T1*eps^(kappa-1))
- Bod 3: Izochorický přívod tepla (v3 = v2, p3 = p2*alpha, T3 = T2*alpha)
- Bod 4: Izobarický přívod tepla (p4 = p3, v4 = v3*beta, T4 = T3*beta)
- Bod 5: Izoentropická expanze (v5 = v1, p5 = p4*(v4/v5)^kappa, T5 = T4*(v4/v5)^(kappa-1))

U každého bodu vypište jeho stavové veličiny pomocí print() a f-stringu!
"""
# Zadané konstanty
r = 287.15        # Plynová konstanta vzduchu [J/(kg.K)]
kappa = 1.4       # Poissonova konstanta [-]
p1 = 100000       # Počáteční tlak [Pa]
T1 = 293.15       # Počáteční teplota [K]

# Termodynamické parametry Sabatheho oběhu
epsilon = 16.5    # Kompresní poměr (v1 / v2)
alpha = 1.6       # Stupeň zvýšení tlaku (p3 / p2)
beta = 1.4        # Stupeň předběžné expanze (v4 / v3)

# ZDE ZAČNĚTE POČÍTAT:

# Bod 1:


# Bod 2:


# Bod 3:


# Bod 4:


# Bod 5: