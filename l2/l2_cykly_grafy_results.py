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

# Převod na Kelviny pro výpočet
T_atm_K = T_atm + 273.15

if preplnovani == "Turbodmychadlo":
    p_sani = stlaceni_TD * p_atm
    T_sani_K = T_atm_K * stlaceni_TD**((kappa-1)/kappa)
elif preplnovani == "Mechanické":
    p_sani = stlaceni_mech * p_atm
    T_sani_K = T_atm_K * stlaceni_mech**((kappa-1)/kappa)
else:
    p_sani = p_atm
    T_sani_K = T_atm_K

# Převod zpět na °C pro výpis
T_sani = T_sani_K - 273.15

print(f"Bylo zvoleno přeplňování: {preplnovani}")
print(f"Tlak v sání motoru se rovná {p_sani:.0f} Pa a teplota se rovná {T_sani:.2f} °C\n")

p_max = 5.5  # MPa
T_max = 1100 # °C
epsilon = 12 # Kompresní poměr


# Výpočet hodnot po adiabatické kompresi ve válci
p_komprese = p_sani * (epsilon ** kappa)
T_komprese_K = T_sani_K * (epsilon ** (kappa - 1))

# Převod na stejné jednotky pro porovnání
p_komprese_MPa = p_komprese / 1000000
T_komprese_C = T_komprese_K - 273.15

# Logický test pomocí OR (stačí, aby jedna hodnota překročila limit)
if p_komprese_MPa > p_max or T_komprese_C > T_max:
    print("Hodnoty překročili horní limit")












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

# Vnořený cyklus pro projití všech kombinací epsilon a teplot
for eps in epsilon_hodnoty:
    ucinnost = 1 - (1 / (eps ** (kappa - 1)))
    print(f"Epsilon: {eps} -> Účinnost: {ucinnost:.3f}")















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
V_z = 1.984                                                            # Zdvihový objem [dm3]

Pe_list = []
pe_list = []

# Výpočet odvozených veličin
for i in range(len(n)):
    # 1. Výpočet efektivního výkonu [kW]
    Pe = (Mt[i] * n[i]) / 9548.8
    Pe_list.append(round(Pe, 1))
    
    # 2. Výpočet středního efektivního tlaku [bar]
    pe = (120.0 * Pe) / (V_z * n[i])
    pe_list.append(round(pe, 2))

print(f"Výkon [kW]: {Pe_list}")
print(f"Tlak [bar]: {pe_list}")

# Úplně základní vizualizace
plt.plot(n, Mt, label="Točivý moment [Nm]")
plt.plot(n, Pe_list, label="Výkon [kW]")
plt.legend()
plt.show()