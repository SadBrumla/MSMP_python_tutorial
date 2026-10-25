"""
CVIČENÍ 2 - PRÁCE SE SOUBORY - ÚKOLY (pro studenty)

Téma: cesty, with open(), čtení, zápis, modul csv, modul json.
Teorie a vzorové příklady: Obsidian, "Cvičení 2 - Funkce a práce se soubory".

POZOR: spouštějte ze složky l2/, aby fungovaly relativní cesty do data/.
STRUKTURA: tenhle soubor má stejné banery a stejná zadání jako
l2_soubory_results.py - dají se tedy porovnat vedle sebe.
Pod každým banerem je místo na váš kód.
"""
import os
import csv
import json
import math

CESTA_MERENI = "data/mereni_brzda.csv"
CESTA_MOTOR = "data/motor_2-0tdi.json"
SLOZKA_VYSTUPU = "vystupy"



# ============================================================================
# ÚKOL S1: Načtěte měření do seznamů
# ============================================================================
# Soubor data/mereni_brzda.csv je protokol z motorové brzdy
# (1.9 TDI PD, plné zatížení). Sloupce jsou oddělené středníkem:
#     otacky;moment_Nm;vykon_kW;spotreba_g_kWh
#     1000;170.0;17.8;240
#
# Naplňte čtyři seznamy ČÍSLY (ne textem!):
# 1. Hlavičku přeskočte.
# 2. Každý řádek nejdřív .strip(), pak .split(";").
# 3. Hodnoty převeďte na float a přidejte .append()em.
# 4. Vypište, kolik bodů jste načetli, a první a poslední otáčky.
# Kontrola: 10 bodů, od 1000 do 4500 1/min.
#
# Tyhle seznamy používají i všechny další úkoly - ať jsou správně.
# ----------------------------------------------------------------------------

otacky = []
moment = []
vykon = []
spotreba = []

with open(CESTA_MERENI, "r", encoding="utf-8") as f:
    radky = f.readlines()

# radky[0] je hlavička -> data začínají na radky[1]
for radek in radky[1:]:
    pass        # DOPLŇTE: strip -> split -> float -> append


print(f"Načteno bodů: {len(otacky)}")


# ============================================================================
# ÚKOL S2: Nejhospodárnější bod motoru
# ============================================================================
# 1. Napište funkci index_minima(seznam), která vrátí INDEX nejmenší hodnoty
#    (ne hodnotu samotnou - s indexem se dostanete do všech čtyř seznamů
#    najednou).
# 2. Zavolejte ji na seznam spotreba a vypište otáčky, moment, výkon
#    i spotřebu v nalezeném bodě.
# Tip: začněte tím, že za nejmenší prohlásíte nultý prvek, a cyklem zkoušejte,
# jestli nenajdete menší.
# Kontrola: minimum měrné spotřeby je v okolí 2000-2500 1/min.
# ----------------------------------------------------------------------------

def index_minima(seznam):
    """Vrátí index nejmenší hodnoty v seznamu."""
    pass        # DOPLŇTE


# Zavolejte na seznam spotreba a vypište celý nalezený bod:


# ============================================================================
# ÚKOL S3: Vlastní CSV s výsledky
# ============================================================================
# Zapište soubor vysledky.csv, který ke každému naměřenému bodu přidá dvě
# dopočítané hodnoty: střední pístovou rychlost a litrový výkon.
# 1. Nejdřív hlavička: otacky;vykon_kW;c_s_m_s;litrovy_vykon_kW_l
# 2. Cyklem for zapište každý bod jako jeden řádek
#    (hodnoty oddělené ;, na konci \n).
# 3. Čísla zaokrouhlete f-stringem na 2 desetinná místa.
# 4. Na konci soubor znovu otevřete a vypište pro kontrolu.
#
# Pozn.: vysledky.csv je GENEROVANÝ výstup -> patří do .gitignore, ne do repa.
# ----------------------------------------------------------------------------

# Funkce z části o funkcích - tady je používáme znovu
def stredni_pistova_rychlost(zdvih_mm, otacky):
    """Střední pístová rychlost [m/s]."""
    return 2 * (zdvih_mm / 1000) * otacky / 60


def litrovy_vykon_kw_l(vykon_kw, objem_l):
    """Litrový (objemový) výkon [kW/l]."""
    return vykon_kw / objem_l


zdvih_mm = 95.5       # 1.9 TDI PD
objem_l = 1.896

with open("vysledky.csv", "w", encoding="utf-8") as f:
    f.write("otacky;vykon_kW;c_s_m_s;litrovy_vykon_kW_l\n")
    for i in range(len(otacky)):
        pass    # DOPLŇTE: spočítat c_s a litrový výkon, zapsat jeden řádek


# A tady si soubor přečtěte zpátky pro kontrolu:


# ============================================================================
# ÚKOL S4: Motor z JSON do výpočtu
# ============================================================================
# Ve složce data leží soubor motor_2-0tdi.json s popisem jiného motoru.
# 1. Načtěte ho pomocí json.load().
# 2. Vytáhněte z něj vrtání, zdvih a počet válců a předejte je funkci
#    zdvihovy_objem_l() (je připravená níž).
# 3. Vypište název motoru a jeho zdvihový objem v litrech.
# 4. Do slovníku PŘIDEJTE nový klíč "zdvihovy_objem_l" s vypočtenou hodnotou
#    a celý slovník uložte jako motor_2-0tdi_doplneny.json.
# 5. Otevřete si výsledný soubor v editoru a podívejte se, co v něm přibylo.
# Kontrola: 2.0 TDI má zdvihový objem přibližně 1,968 l.
# ----------------------------------------------------------------------------

def zdvihovy_objem_l(vrtani_mm, zdvih_mm, pocet_valcu):
    """Zdvihový objem celého motoru [l]. Z části o funkcích."""
    plocha_m2 = math.pi * (vrtani_mm / 1000) ** 2 / 4
    return plocha_m2 * (zdvih_mm / 1000) * pocet_valcu * 1000

# 1) načtěte CESTA_MOTOR pomocí json.load()


# 2) a 3) spočítejte objem a vypište název motoru + objem


# 4) doplňte klíč "zdvihovy_objem_l" a uložte do nového souboru


# ============================================================================
# ÚKOL Z: Celý řetězec od měření k protokolu (velký závěrečný)
# ============================================================================
# Tohle je JEDINÝ velký úkol za celé dnešní cvičení a potřebujete v něm
# obojí: funkce z první poloviny i práci se soubory z druhé.
#
# Napište program, který udělá celou úlohu od začátku do konce - a každý
# krok ať je ve své funkci. Napište těchto sedm funkcí:
#
#   nacti_motor(cesta)
#       -> načte JSON s popisem motoru, vrátí slovník
#   nacti_mereni(cesta)
#       -> načte CSV, vrátí (otacky, moment, vykon, spotreba) jako seznamy čísel
#   dopocitej(otacky, vykon, motor)
#       -> vrátí dva seznamy: c_s [m/s] a litrový výkon [kW/l] pro každý bod
#          (zdvih a objem si vezme ZE SLOVNÍKU motor, ne z čísla v kódu!)
#   najdi_extremy(otacky, vykon, spotreba)
#       -> vrátí slovník s klíči "max_vykon_kw", "otacky_max_vykonu",
#          "min_spotreba", "otacky_min_spotreby"
#   zapis_protokol(cesta, motor, extremy)
#       -> zapíše čitelný textový protokol
#   zapis_vysledky(cesta, otacky, vykon, c_s, litrovy_vykon)
#       -> zapíše CSV se všemi body včetně dopočítaných sloupců
#   zapis_souhrn_json(cesta, motor, extremy)
#       -> uloží popis motoru i extrémy do jednoho JSON
#
# Pravidla, která chceme vidět:
#  - Výstupy do složky vystupy/  (os.makedirs("vystupy", exist_ok=True))
#  - Na obrazovku jen jedna, dvě věty o tom, kam se co zapsalo.
#    Funkce, které počítají, mají return. print() je jen na konci, pro člověka.
#
# A pak zkuste tohle:
# Seznamy otacky a vykon jsou přesně ten tvar dat, který matplotlib potřebuje
# na křivku výkonu. Dokreslete ji a uložte:
#     plt.savefig("vystupy/vykon.png", dpi=150)
# Tím máte celý řetězec: soubor -> výpočet -> graf -> soubor.
# To je kostra každé semestrální práce.
# ----------------------------------------------------------------------------

def nacti_motor(cesta):
    """Načte JSON s popisem motoru. Vrací slovník."""
    pass        # DOPLŇTE


def nacti_mereni(cesta):
    """Načte CSV z brzdy. Vrací (otacky, moment, vykon, spotreba)."""
    pass        # DOPLŇTE


def dopocitej(otacky, vykon, motor):
    """Vrací dva seznamy: c_s [m/s] a litrovy vykon [kW/l]."""
    pass        # DOPLŇTE


def najdi_extremy(otacky, vykon, spotreba):
    """Vrací slovník s maximem výkonu a minimem měrné spotřeby."""
    pass        # DOPLŇTE


def zapis_protokol(cesta, motor, extremy):
    """Zapíše textový protokol. Nic nevrací."""
    pass        # DOPLŇTE


def zapis_vysledky(cesta, otacky, vykon, c_s, litrovy_vykon):
    """Zapíše CSV se všemi body a dopočítanými sloupci. Nic nevrací."""
    pass        # DOPLŇTE


def zapis_souhrn_json(cesta, motor, extremy):
    """Uloží popis motoru i extrémy do jednoho JSON. Nic nevrací."""
    pass        # DOPLŇTE


# --- HLAVNÍ PROGRAM ---------------------------------------------------------
# Tady už se jen volá. Kdo si funkce napsal dobře, má tuhle část krátkou.

os.makedirs(SLOZKA_VYSTUPU, exist_ok=True)

# DOPLŇTE volání funkcí v rozumném pořadí a na konci jednu větu o tom,
# kam se co zapsalo.
