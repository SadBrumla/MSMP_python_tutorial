""" 
LEKCE 2: ZÁKLADY PYTHONU V AUTOMOTIVE A MOTOROVÉM INŽENÝRSTVÍ 
(Přeplňování turbodmychadlem, mez pumpování, podmínky, cykly a vizualizace) 
""" 

""" 
PŘÍKLAD 1: Typ přeplňování a jednoduchý if elif else
Zadání: Kontrola typu přeplňování motoru. Vypočítej hodnoty v sání motoru 
pokud je proměnná preplnovani nastavená na "Turbodmychadlo", "Mechanické" nebo "Bez přeplňování"
""" 
p_atm = 10135 # Pa
T_atm = 30
kappa = 1.4
stlaceni_TD = 2.2
stlaceni_mech = 2
preplnovani = "Turbodmychadlo" # nebo preplnovani = "Mechanické" nebo preplnovani = "Bez přeplňování"


if preplnovani == "Turbodmychadlo":
    p_sani = stlaceni_TD * p_atm
    T_sani = T_atm * stlaceni_TD**((kappa-1)/kappa)
elif preplnovani == "Mechanické":
    p_sani = stlaceni_mech * p_atm
    T_sani = T_atm * stlaceni_mech**((kappa-1)/kappa)
else:
    p_sani = p_atm
    T_sani = T_atm


print(f"Byl zvolo přeplňování {preplnovani}, tlak na saní motoru se rovná {p_sani} Pa a teplota se rovná {T_sani}")


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
PŘÍKLAD 3: Optimalizace účinnosti pomocí cyklů
Zadání: Na základě zadaných kompresních poměrů a teplot nasávaného vzduchu
(pro různé nadmořské výšky/stavy chlazení) vypočítejte pomocí vnořeného cyklu
termodynamickou účinnost Ottova cyklu: eta = 1 - (1 / (epsilon ** (kappa - 1))).
Zjistěte, který stav splňuje minimální požadovanou účinnost 0.55.
"""

kappa = 1.4
minimalni_ucinnost = 0.55

# Seznam zkoumaných kompresních poměrů (epsilon)
epsilon_hodnoty = [8, 9, 10, 11]

# Seznam teplot nasávaného vzduchu v °C (např. různé stavy chlazení)
teploty_sani = [20, 40, 60]

print("--- Analýza účinnosti pro různé stavy ---")

# Vnořený cyklus pro projití všech kombinací epsilon a teplot
for eps in epsilon_hodnoty:
    for T in teploty_sani:
        # Výpočet termodynamické účinnosti (nezávisí na T, ale v reálu by T ovlivnilo výkon)
        ucinnost = 1 - (1 / (eps ** (kappa - 1)))
        
        # Logické vyhodnocení
        if ucinnost >= minimalni_ucinnost:
            stav = "VYHOVUJE"
        else:
            stav = "NEVYHOVUJE"
            
        print(f"Epsilon: {eps}, Teplota sání: {T}°C -> Účinnost: {ucinnost:.3f} [{stav}]")










""" 
PŘÍKLAD 3: Cykly (For a While) - Testování otáčkového spektra a náběhu turba 
Zadání: Navazuje na předchozí parametry. 
1) Pomocí cyklu 'for' projdeme otáčkové spektrum motoru od 1000 do 6000 ot/min. 
2) Pomocí cyklu 'while' nasimulujeme náběh plnicího tlaku turbodmychadla při akceleraci z volnoběhu. 
""" 
# přidat pro každé od
for rpm in range(1000, 6001, 1000): 
    print(f"Měřicí bod: n = {rpm} ot/min") 

print("\n--- Cyklus WHILE: Náběh plnicího tlaku p_s (Turbo-lag) ---") 
p_s_aktualni = 1.0 # Atmosférický tlak [bar] 
p_s_cilovy = 2.2 # Požadovaný plnicí tlak [bar] 

while p_s_aktualni < p_s_cilovy: 
    print(f"Aktuální plnicí tlak p_s: {p_s_aktualni:.2f} bar -> Náběh dmychadla...") 
    p_s_aktualni += 0.3 # Postupné stlačování dmychadlem 

print(f"[CÍL DOSAŽEN]: Dosáhnuto plného plnicího tlaku p_s = {p_s_aktualni:.1f} bar.") 
















"""
JEDNODUCHÝ MODEL MAPY KOMPRESORU PRO STUDENTY
Zadání: Z naměřených počátečních bodů pro různé otáčky kompresoru 
vytvořte matematický model tlakových křivek a vykreslete mapu turbodmychadla.
Křivky jsou aproximovány zjednodušenou rovnicí paraboly.
"""

import matplotlib.pyplot as plt
import numpy as np

# 1. Definice zkoumaných stavů (otáčky dmychadla v ot/min)
otacky_stavy = [60000, 80000, 100000, 120000]

plt.figure(figsize=(9, 6))

# 2. Vykreslení teoretické meze pumpování (Surge line)
# Modelujeme ji jednoduchou kvadratickou rovnicí: Pi_k = 1 + c * (m_k)^2
m_k_surge = np.linspace(0.01, 0.25, 20) # Rozsah průtoků pro mez pumpování
pi_k_surge = 1.0 + 35 * m_k_surge**2    # Zjednodušená rovnice
plt.plot(m_k_surge, pi_k_surge, 'r--', linewidth=2.5, label='Mez pumpování (Teoretická)')

# 3. Cyklus přes jednotlivé naměřené stavy otáček
for n in otacky_stavy:
    
    # KROK A: Simulace naměřeného hmotnostního průtoku pro dané otáčky [kg/s]
    # S rostoucími otáčkami se začátek křivky posouvá k vyšším průtokům
    m_k_start = (n / 100000) * 0.1 
    # Vytvoříme pole 15 bodů od počátečního průtoku směrem doprava
    m_k_mereni = np.linspace(m_k_start, m_k_start + 0.12, 15)
    
    # KROK B: Matematický model tlakového poměru pro dané otáčky
    # Využijeme rovnici klesající paraboly: Pi_k = Max_Tlak - k * (průtok - posun)^2
    max_tlak = 1.0 + (n / 60000)**2 * 0.25  # Maximální dosažitelný tlak pro tyto otáčky
    k_odpor = 18.0                          # Ztrátová konstanta kompresoru
    
    # Aplikace rovnice na celé pole průtoků
    pi_k_mereni = max_tlak - k_odpor * (m_k_mereni - m_k_start)**2
    
    # KROK C: Vykreslení křivky pro aktuální stav
    # Křivku vykreslíme i se značkami bodů, jako by šlo o laboratoř
    plt.plot(m_k_mereni, pi_k_mereni, marker='o', markersize=4, label=f'Stav: n = {n} ot/min')


# 4. Finální formátování grafu pro inženýrský výstup
plt.title('Zjednodušený výpočtový model charakteristiky kompresoru', fontsize=14, fontweight='bold')
plt.xlabel('Hmotnostní průtok vzduchu $\dot{m}_k$ [kg/s]', fontsize=12)
plt.ylabel('Tlakový poměr $\Pi_k$ [-]', fontsize=12)

# Omezení os na smysluplné fyzikální hodnoty
plt.xlim(0, 0.35)
plt.ylim(1.0, 2.5)

# Zapnutí mřížky a legendy
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='lower right', fontsize=10)
plt.tight_layout()

# Zobrazení grafu na obrazovce
plt.show()


