"""
CVIČENÍ 2 - FUNKCE - ŘEŠENÍ (pro lektora)

Téma: funkce - def, parametry, return, výchozí hodnoty, lokální platnost.
Teorie a vzorové příklady: Obsidian, "Cvičení 2 - Funkce a práce se soubory".

STRUKTURA: tenhle soubor má stejné banery a stejná zadání jako
l2_funkce_task.py - dají se tedy porovnat vedle sebe.
Pod každým banerem je hotové řešení. Spustitelné: python l2_funkce_results.py
"""
import math



# ============================================================================
# ÚKOL F1: První vlastní funkce
# ============================================================================
# Napište funkci plocha_pistu_cm2(vrtani_mm), která:
# 1. má jeden parametr - vrtání v milimetrech,
# 2. spočítá plochu pístu podle S = pi * d^2 / 4,
# 3. VRÁTÍ (return) plochu v cm2, nikoli v mm2 (1 cm2 = 100 mm2).
# Pak ji zavolejte pro vrtání 79.5 mm a 81.0 mm a výsledky vypište
# f-stringem na 2 desetinná místa.
# Kontrola: pro 79,5 mm má vyjít přibližně 49,64 cm2.
# ----------------------------------------------------------------------------

print("\n>>> ÚKOL F1: První vlastní funkce")

def plocha_pistu_cm2(vrtani_mm):
    """Plocha pístu [cm2] z vrtání [mm]."""
    plocha_mm2 = math.pi * vrtani_mm ** 2 / 4
    return plocha_mm2 / 100                  # 1 cm2 = 100 mm2


print(f"Vrtání 79.5 mm -> {plocha_pistu_cm2(79.5):.2f} cm2")
print(f"Vrtání 81.0 mm -> {plocha_pistu_cm2(81.0):.2f} cm2")


# ============================================================================
# ÚKOL F2: Opravte rozbitou funkci (return vs. print)
# ============================================================================
# Funkce kompresni_pomer() má spočítat epsilon = (V_z + V_c) / V_c,
# ale místo vrácení hodnoty ji jen vypisuje - program proto spadne.
# 1. Odkomentujte dva řádky s voláním, spusťte a přečtěte si chybu.
# 2. Opravte funkci tak, aby výsledek VRACELA (return).
# 3. Pomocí podmínky if doplňte rozhodnutí: epsilon nad 14 -> "vznětový motor",
#    jinak -> "zážehový motor".
# Kontrola: epsilon ~ 16,5 -> vznětový motor.
# ----------------------------------------------------------------------------

print("\n>>> ÚKOL F2: Opravte rozbitou funkci (return vs. print)")

V_z = 0.000474        # zdvihový objem jednoho válce [m3]
V_c = 0.0000306       # kompresní objem [m3]

# Oprava: print(epsilon) nahrazeno za return epsilon
def kompresni_pomer(V_z, V_c):
    """Kompresní poměr [-] ze zdvihového a kompresního objemu."""
    return (V_z + V_c) / V_c


eps = kompresni_pomer(V_z, V_c)
print(f"Kompresní poměr: {eps:.1f}")

if eps > 14:
    print("-> vznětový motor")
else:
    print("-> zážehový motor")


# ============================================================================
# ÚKOL F3: Výchozí hodnota parametru + cyklus for
# ============================================================================
# 1. Napište funkci stredni_pistova_rychlost(zdvih_mm, otacky=4000), která
#    vrátí c_s = 2 * z * n / 60 v m/s (z je zdvih v METRECH).
# 2. Zavolejte ji jednou bez druhého argumentu (použijí se výchozí 4000 1/min).
# 3. Pak ji cyklem for zavolejte pro každé otáčky ze seznamu otacky_list
#    a vypište tabulku.
# 4. Uvnitř cyklu přidejte if: pokud c_s > 13 m/s, připište
#    "!! nad doporučenou mezí".
# Kontrola: při 4000 1/min vyjde 12,73 m/s; mez překročí až 5000 1/min.
# ----------------------------------------------------------------------------

print("\n>>> ÚKOL F3: Výchozí hodnota parametru + cyklus for")

zdvih = 95.5                                    # [mm], motor 1.9 TDI
otacky_list = [1000, 2000, 3000, 4000, 5000]

def stredni_pistova_rychlost(zdvih_mm, otacky=4000):
    """Střední pístová rychlost [m/s]. Výchozí otáčky 4000 1/min."""
    return 2 * (zdvih_mm / 1000) * otacky / 60


print(f"Výchozí otáčky (4000): c_s = {stredni_pistova_rychlost(zdvih):.2f} m/s\n")

for otacky in otacky_list:
    c_s = stredni_pistova_rychlost(zdvih, otacky)
    radek = f"{otacky:>5} 1/min -> c_s = {c_s:5.2f} m/s"
    if c_s > 13:
        radek += "   !! nad doporučenou mezí"
    print(radek)


# ============================================================================
# ÚKOL F4: Funkce vracející více hodnot
# ============================================================================
# Napište funkci stav_po_izochorickem_privodu(p, T, v, alpha) - přívod tepla
# při konstantním objemu (přechod 2 -> 3):
#    v3 = v2,   p3 = p2 * alpha,   T3 = T2 * alpha
# Vrátí trojici (p3, T3, v3). Zavolejte ji na připravený stav po kompresi
# (bod 2 níž) pro alpha = 1.6 a bod 3 vypište.
# Kontrola: T3 ~ 1440 K, p3 ~ 81 bar.
# ----------------------------------------------------------------------------

print("\n>>> ÚKOL F4: Funkce vracející více hodnot")

# Připravený stav po kompresi (bod 2) - stejná čísla jako v Cvičení 1
r = 287.15
p1 = 100000
T1 = 293.15
kappa = 1.4
epsilon = 16.5

v1 = r * T1 / p1
v2 = v1 / epsilon
p2 = p1 * epsilon ** kappa
T2 = T1 * epsilon ** (kappa - 1)

def stav_po_izochorickem_privodu(p, T, v, alpha):
    """Izochorický přívod tepla 2 -> 3. Vrací trojici (p3, T3, v3)."""
    v3 = v
    p3 = p * alpha
    T3 = T * alpha
    return p3, T3, v3


p3, T3, v3 = stav_po_izochorickem_privodu(p2, T2, v2, alpha=1.6)

print(f"Bod 1: p = {p1 / 1e5:6.2f} bar, T = {T1:6.1f} K, v = {v1:.4f} m3/kg")
print(f"Bod 2: p = {p2 / 1e5:6.2f} bar, T = {T2:6.1f} K, v = {v2:.4f} m3/kg")
print(f"Bod 3: p = {p3 / 1e5:6.2f} bar, T = {T3:6.1f} K, v = {v3:.4f} m3/kg")


# ============================================================================
# ÚKOL F5: "Engine builder" - Sabatheho oběh jako funkce
# ============================================================================
# V Cvičení 1 jsme Sabatheho oběh spočítali jednou, ručně dopsanými řádky.
# Tady z něj udělejte nástroj.
#
# 1. sabatheho_obeh(p1, T1, epsilon, alpha, beta, kappa=1.4, r=287.15)
#    spočítá všech 5 bodů a vrátí TŘI SEZNAMY: (tlaky, teploty, objemy).
#    Plňte je bod po bodu pomocí .append().
#      bod 1: v1 = r*T1/p1
#      bod 2: v2 = v1/eps,  p2 = p1*eps^kappa,  T2 = T1*eps^(kappa-1)
#      bod 3: v3 = v2,      p3 = p2*alpha,      T3 = T2*alpha
#      bod 4: p4 = p3,      v4 = v3*beta,       T4 = T3*beta
#      bod 5: v5 = v1,      p5 = p4*(v4/v5)^kappa,  T5 = T4*(v4/v5)^(kappa-1)
# 2. tepelna_ucinnost(teploty, kappa=1.4)
#      eta = 1 - (T5 - T1) / ((T3 - T2) + kappa*(T4 - T3))
# 3. vypis_obeh(nazev, tlaky, teploty, objemy) vypíše oběh jako tabulku.
#    Tahle funkce nic nevrací - její úkol JE ten výpis.
# 4. Cyklem for proženěte funkcemi všechny tři motory ze seznamu motory.
#
# Otázky na konec:
#  - Který motor má nejvyšší účinnost a čím to je?
#  - Co se stane s účinností, když u zážehového motoru zvednete epsilon
#    z 10,5 na 14? A jde to v praxi? (Nápověda: detonační spalování.)
# ----------------------------------------------------------------------------

print("\n>>> ÚKOL F5: 'Engine builder' - Sabatheho oběh jako funkce")

# Každý motor je jedna čtveřice: nazev, epsilon, alpha, beta
motory = [
    ("1.9 TDI PD  (vznětový)", 16.5, 1.6, 1.4),
    ("2.0 TDI CR  (vznětový)", 18.5, 1.5, 1.3),
    ("1.0 TSI     (zážehový)", 10.5, 3.2, 1.0),   # beta = 1.0 -> čistý Ottův oběh
]

p1_obeh = 100000      # [Pa]
T1_obeh = 293.15      # [K]

def sabatheho_obeh(p1, T1, epsilon, alpha, beta, kappa=1.4, r=287.15):
    """Sabatheho oběh - 5 bodů. Vrací (tlaky, teploty, objemy)."""
    tlaky = []
    teploty = []
    objemy = []

    # BOD 1 - sání
    v1 = r * T1 / p1
    tlaky.append(p1)
    teploty.append(T1)
    objemy.append(v1)

    # BOD 2 - izoentropická komprese
    v2 = v1 / epsilon
    p2 = p1 * epsilon ** kappa
    T2 = T1 * epsilon ** (kappa - 1)
    tlaky.append(p2)
    teploty.append(T2)
    objemy.append(v2)

    # BOD 3 - izochorický přívod tepla
    v3 = v2
    p3 = p2 * alpha
    T3 = T2 * alpha
    tlaky.append(p3)
    teploty.append(T3)
    objemy.append(v3)

    # BOD 4 - izobarický přívod tepla
    p4 = p3
    v4 = v3 * beta
    T4 = T3 * beta
    tlaky.append(p4)
    teploty.append(T4)
    objemy.append(v4)

    # BOD 5 - izoentropická expanze
    v5 = v1
    p5 = p4 * (v4 / v5) ** kappa
    T5 = T4 * (v4 / v5) ** (kappa - 1)
    tlaky.append(p5)
    teploty.append(T5)
    objemy.append(v5)

    return tlaky, teploty, objemy


def tepelna_ucinnost(teploty, kappa=1.4):
    """Termická účinnost Sabatheho oběhu [-]."""
    T1, T2, T3, T4, T5 = teploty
    privedene = (T3 - T2) + kappa * (T4 - T3)
    odvedene = T5 - T1
    return 1 - odvedene / privedene


def vypis_obeh(nazev, tlaky, teploty, objemy):
    """Vypíše oběh jako tabulku. Nic nevrací - její úkol JE ten výpis."""
    print(f"\n{nazev}")
    print(f"{'bod':>4} {'p [bar]':>10} {'T [K]':>9} {'v [m3/kg]':>11}")
    for i in range(len(tlaky)):
        print(f"{i + 1:>4} {tlaky[i] / 1e5:>10.2f} {teploty[i]:>9.1f} {objemy[i]:>11.4f}")


for nazev, epsilon, alpha, beta in motory:
    tlaky, teploty, objemy = sabatheho_obeh(p1_obeh, T1_obeh, epsilon, alpha, beta)
    vypis_obeh(nazev, tlaky, teploty, objemy)
    print(f"     Termická účinnost: {tepelna_ucinnost(teploty) * 100:.1f} %")

print("""
Odpovědi na otázky:
 - Nejvyšší účinnost má 2.0 TDI CR - rozhoduje hlavně KOMPRESNÍ POMĚR (18,5).
   Čím vyšší epsilon, tím vyšší termická účinnost oběhu.
 - Zvýšení epsilon u zážehového motoru z 10,5 na 14 účinnost zvedne, ale
   v praxi to nejde: rostoucí teplota a tlak na konci komprese vedou
   k detonačnímu (klepavému) spalování. Proto mají vznětové motory vyšší
   účinnost "zdarma" - naftu nic nenutí držet epsilon nízko.
""")
