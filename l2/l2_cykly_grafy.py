""" 
LEKCE 2: (podmínky, cykly a vizualizace) 

""" 


""" 
PŘÍKLAD 1: Typ přeplňování a jednoduchý if elif else
Zadání: Kontrola typu přeplňování motoru. Vypočítej hodnoty v sání motoru 
pokud je proměnná preplnovani nastavená na "Turbodmychadlo", "Mechanické" nebo "Bez přeplňování"
do terminálu vypiš formátovaný text (viz 1. Lekce)
"""
p_atm = 10135 # Pa
T_atm = 30
kappa = 1.4
stlaceni_TD = 2.2
stlaceni_mech = 2
preplnovani = "Turbodmychadlo" # nebo preplnovani = "Mechanické" nebo preplnovani = "Bez přeplňování"

T_atm_K = T_atm + 273.15

if preplnovani == "Turbodmychadlo":
    p_sani = stlaceni_TD * p_atm
    T_sani = T_atm_K * stlaceni_TD**((kappa-1)/kappa)
elif preplnovani == "Mechanické":
    p_sani = stlaceni_mech * p_atm
    T_sani = T_atm_K * stlaceni_mech**((kappa-1)/kappa)
else:
    p_sani = p_atm
    T_sani = T_atm


print(f"Byl zvolo přeplňování {preplnovani}, tlak na saní motoru se rovná {p_sani} Pa a teplota se rovná {T_sani:.2} °C")


"""
PŘÍKLAD 2: 
Otestuj jestli se tlak a teplota po stlačení ve válci nevysktují nad maximálními urovněmi
použij logické spojku AND nebo OR, pokud hodnoty po adiabatické expanzi (poměr objemů je epsilon) nepřesáhnou tak hodnoty
ulož do proměnných p_expanze, T_expanze
"""
p_max = 5.5 #MPa
T_max = 1100 #°C
epsilon = 12



"""
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
PŘÍKLAD 4: Výpočet charakteristiky motoru a základní graf
Zadání: Z naměřených hodnot točivého momentu a otáček (pro 11 pracovních bodů)
vypočítejte efektivní výkon motoru (Pe v kW) a střední efektivní tlak (pe v barech). 
Doplňte cyklus pro výpočet, výsledky vypište a na závěr vykreslete základní graf 
pomocí knihovny matplotlib.
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