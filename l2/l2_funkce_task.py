"""
CVIČENÍ 2 - FUNKCE - ÚKOLY (pro studenty)

Téma: funkce - def, parametry, return, výchozí hodnoty, lokální platnost.
Teorie a vzorové příklady: Obsidian, "Cvičení 2 - Funkce a práce se soubory".

STRUKTURA: tenhle soubor má stejné banery a stejná zadání jako
l2_funkce_results.py - dají se tedy porovnat vedle sebe.
Pod každým banerem je místo na váš kód.
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

def plocha_pistu_cm2(vrtani_mm):
    # 1) spočítejte plochu v mm2
    # 2) převeďte na cm2
    # 3) vraťte výsledek pomocí return
    pass        # <-- tento řádek smažte, až budete mít tělo funkce


# A tady funkci zavolejte a výsledky vypište:


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

V_z = 0.000474        # zdvihový objem jednoho válce [m3]
V_c = 0.0000306       # kompresní objem [m3]

# Rozbitá verze - chybí jí return:
def kompresni_pomer(V_z, V_c):
    epsilon = (V_z + V_c) / V_c
    print(epsilon)


# Krok 1 - odkomentujte, spusťte a přečtěte si chybu (TypeError na None):
# eps = kompresni_pomer(V_z, V_c)
# print(f"Kompresní poměr: {eps:.1f}")

# Kroky 2 a 3 - sem napište opravenou funkci a rozhodnutí o typu motoru:


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

zdvih = 95.5                                    # [mm], motor 1.9 TDI
otacky_list = [1000, 2000, 3000, 4000, 5000]

def stredni_pistova_rychlost(zdvih_mm, otacky=4000):
    pass        # <-- doplňte tělo a smažte pass


# Volání s výchozími otáčkami:


# Cyklus for přes celý seznam + podmínka if:


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
    pass        # <-- doplňte tělo a smažte pass


# Zavolejte na p2, T2, v2 pro alpha = 1.6 a bod 3 vypište:


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

    # BOD 1 - hotovo jako vzor, pokračujte stejným způsobem
    v1 = r * T1 / p1
    tlaky.append(p1)
    teploty.append(T1)
    objemy.append(v1)

    # BOD 2 (izoentropická komprese) - DOPLŇTE

    # BOD 3 (izochorický přívod tepla) - DOPLŇTE

    # BOD 4 (izobarický přívod tepla) - DOPLŇTE

    # BOD 5 (izoentropická expanze) - DOPLŇTE

    return tlaky, teploty, objemy


def tepelna_ucinnost(teploty, kappa=1.4):
    """Termická účinnost Sabatheho oběhu [-]."""
    pass        # DOPLŇTE


def vypis_obeh(nazev, tlaky, teploty, objemy):
    """Vypíše oběh jako tabulku. Nic nevrací."""
    pass        # DOPLŇTE


# Řádek níž rozbalí každou čtveřici do čtyř proměnných - stejné rozbalení
# jako u "p, T, v = funkce()" v Úkolu F4.
for nazev, epsilon, alpha, beta in motory:
    pass        # DOPLŇTE: sabatheho_obeh -> vypis_obeh -> tepelna_ucinnost
