"""
CVIČENÍ 2 - PRÁCE SE SOUBORY - ŘEŠENÍ (pro lektora)

Téma: cesty, with open(), čtení, zápis, modul csv, modul json.
Teorie a vzorové příklady: Obsidian, "Cvičení 2 - Funkce a práce se soubory".

POZOR: spouštějte ze složky l2/, aby fungovaly relativní cesty do data/.
STRUKTURA: tenhle soubor má stejné banery a stejná zadání jako
l2_soubory_task.py - dají se tedy porovnat vedle sebe.
Pod každým banerem je hotové řešení. Spustitelné: python l2_soubory_results.py
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

print("\n>>> ÚKOL S1: Načtěte měření do seznamů")

otacky = []
moment = []
vykon = []
spotreba = []

with open(CESTA_MERENI, "r", encoding="utf-8") as f:
    radky = f.readlines()

for radek in radky[1:]:                       # radky[0] je hlavička
    hodnoty = radek.strip().split(";")
    otacky.append(float(hodnoty[0]))
    moment.append(float(hodnoty[1]))
    vykon.append(float(hodnoty[2]))
    spotreba.append(float(hodnoty[3]))

print(f"Načteno bodů: {len(otacky)}")
print(f"Rozsah otáček: {otacky[0]:.0f} - {otacky[-1]:.0f} 1/min")


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

print("\n>>> ÚKOL S2: Nejhospodárnější bod motoru")

def index_minima(seznam):
    """Vrátí index nejmenší hodnoty v seznamu."""
    index = 0
    for i in range(len(seznam)):
        if seznam[i] < seznam[index]:
            index = i
    return index


i_min = index_minima(spotreba)

print(f"Nejnižší měrná spotřeba je v bodě s indexem {i_min}:")
print(f"  otáčky:   {otacky[i_min]:.0f} 1/min")
print(f"  moment:   {moment[i_min]:.1f} Nm")
print(f"  výkon:    {vykon[i_min]:.1f} kW")
print(f"  spotřeba: {spotreba[i_min]:.0f} g/kWh")


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

print("\n>>> ÚKOL S3: Vlastní CSV s výsledky")

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
        c_s = stredni_pistova_rychlost(zdvih_mm, otacky[i])
        lv = litrovy_vykon_kw_l(vykon[i], objem_l)
        f.write(f"{otacky[i]:.0f};{vykon[i]:.2f};{c_s:.2f};{lv:.2f}\n")

with open("vysledky.csv", "r", encoding="utf-8") as f:
    print(f.read())


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

print("\n>>> ÚKOL S4: Motor z JSON do výpočtu")

def zdvihovy_objem_l(vrtani_mm, zdvih_mm, pocet_valcu):
    """Zdvihový objem celého motoru [l]. Z části o funkcích."""
    plocha_m2 = math.pi * (vrtani_mm / 1000) ** 2 / 4
    return plocha_m2 * (zdvih_mm / 1000) * pocet_valcu * 1000

with open(CESTA_MOTOR, "r", encoding="utf-8") as f:
    motor = json.load(f)

objem = zdvihovy_objem_l(motor["vrtani_mm"], motor["zdvih_mm"], motor["pocet_valcu"])

print(f"Motor:          {motor['nazev']}")
print(f"Zdvihový objem: {objem:.3f} l")

motor["zdvihovy_objem_l"] = round(objem, 3)        # nový klíč ve slovníku

with open("motor_2-0tdi_doplneny.json", "w", encoding="utf-8") as f:
    json.dump(motor, f, indent=2, ensure_ascii=False)

print("Uloženo do motor_2-0tdi_doplneny.json")


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

print("\n>>> ÚKOL Z: Celý řetězec od měření k protokolu (velký závěrečný)")

def nacti_motor(cesta):
    """Načte JSON s popisem motoru. Vrací slovník."""
    with open(cesta, "r", encoding="utf-8") as f:
        return json.load(f)


def nacti_mereni(cesta):
    """Načte CSV z brzdy. Vrací (otacky, moment, vykon, spotreba)."""
    otacky, moment, vykon, spotreba = [], [], [], []
    with open(cesta, "r", encoding="utf-8", newline="") as f:
        cteni = csv.DictReader(f, delimiter=";")
        for radek in cteni:
            otacky.append(float(radek["otacky"]))
            moment.append(float(radek["moment_Nm"]))
            vykon.append(float(radek["vykon_kW"]))
            spotreba.append(float(radek["spotreba_g_kWh"]))
    return otacky, moment, vykon, spotreba


def dopocitej(otacky, vykon, motor):
    """Vrací dva seznamy: c_s [m/s] a litrovy vykon [kW/l].

    Zdvih a objem si bere ze slovníku motor - v kódu není žádné číslo.
    """
    zdvih = motor["zdvih_mm"]
    objem = zdvihovy_objem_l(motor["vrtani_mm"], zdvih, motor["pocet_valcu"])

    c_s, litrovy_vykon = [], []
    for i in range(len(otacky)):
        c_s.append(stredni_pistova_rychlost(zdvih, otacky[i]))
        litrovy_vykon.append(litrovy_vykon_kw_l(vykon[i], objem))
    return c_s, litrovy_vykon


def najdi_extremy(otacky, vykon, spotreba):
    """Vrací slovník s maximem výkonu a minimem měrné spotřeby."""
    i_max = 0
    for i in range(len(vykon)):
        if vykon[i] > vykon[i_max]:
            i_max = i
    i_min = index_minima(spotreba)
    return {
        "max_vykon_kw": vykon[i_max],
        "otacky_max_vykonu": otacky[i_max],
        "min_spotreba": spotreba[i_min],
        "otacky_min_spotreby": otacky[i_min],
    }


def zapis_protokol(cesta, motor, extremy):
    """Zapíše textový protokol. Nic nevrací."""
    with open(cesta, "w", encoding="utf-8") as f:
        f.write("PROTOKOL O MĚŘENÍ NA MOTOROVÉ BRZDĚ\n")
        f.write("=" * 48 + "\n")
        f.write(f"Motor:             {motor['nazev']}\n")
        f.write(f"Počet válců:       {motor['pocet_valcu']}\n")
        f.write(f"Vrtání x zdvih:    {motor['vrtani_mm']} x {motor['zdvih_mm']} mm\n")
        f.write(f"Zdvihový objem:    {motor['zdvihovy_objem_l']:.3f} l\n")
        f.write(f"Přeplňovaný:       {'ano' if motor['preplnovany'] else 'ne'}\n")
        f.write("-" * 48 + "\n")
        f.write(f"Maximální výkon:   {extremy['max_vykon_kw']:.1f} kW "
                f"při {extremy['otacky_max_vykonu']:.0f} 1/min\n")
        f.write(f"Min. měrná spotř.: {extremy['min_spotreba']:.0f} g/kWh "
                f"při {extremy['otacky_min_spotreby']:.0f} 1/min\n")


def zapis_vysledky(cesta, otacky, vykon, c_s, litrovy_vykon):
    """Zapíše CSV se všemi body a dopočítanými sloupci. Nic nevrací."""
    with open(cesta, "w", encoding="utf-8", newline="") as f:
        zapis = csv.writer(f, delimiter=";")
        zapis.writerow(["otacky", "vykon_kW", "c_s_m_s", "litrovy_vykon_kW_l"])
        for i in range(len(otacky)):
            zapis.writerow([f"{otacky[i]:.0f}", f"{vykon[i]:.2f}",
                            f"{c_s[i]:.2f}", f"{litrovy_vykon[i]:.2f}"])


def zapis_souhrn_json(cesta, motor, extremy):
    """Uloží popis motoru i extrémy do jednoho JSON. Nic nevrací."""
    with open(cesta, "w", encoding="utf-8") as f:
        json.dump({"motor": motor, "extremy": extremy}, f,
                  indent=2, ensure_ascii=False)


# --- HLAVNÍ PROGRAM ---------------------------------------------------------
os.makedirs(SLOZKA_VYSTUPU, exist_ok=True)

motor_z = nacti_motor(CESTA_MOTOR)
motor_z["zdvihovy_objem_l"] = round(zdvihovy_objem_l(
    motor_z["vrtani_mm"], motor_z["zdvih_mm"], motor_z["pocet_valcu"]), 3)

ot, mo, vy, sp = nacti_mereni(CESTA_MERENI)
cs, lv = dopocitej(ot, vy, motor_z)
extremy = najdi_extremy(ot, vy, sp)

zapis_protokol(f"{SLOZKA_VYSTUPU}/protokol.txt", motor_z, extremy)
zapis_vysledky(f"{SLOZKA_VYSTUPU}/vysledky.csv", ot, vy, cs, lv)
zapis_souhrn_json(f"{SLOZKA_VYSTUPU}/souhrn.json", motor_z, extremy)

print(f"Hotovo. protokol.txt, vysledky.csv a souhrn.json jsou v '{SLOZKA_VYSTUPU}/'.")

# Volitelný graf. Běží jen když je matplotlib k dispozici.
try:
    import matplotlib
    matplotlib.use("Agg")                     # kreslení do souboru bez okna
    import matplotlib.pyplot as plt

    fig, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(ot, vy, marker="o", color="red", label="Výkon [kW]")
    ax1.set_xlabel("Otáčky n [1/min]")
    ax1.set_ylabel("Výkon P [kW]", color="red")
    ax1.grid(True, linestyle="--", alpha=0.6)

    ax2 = ax1.twinx()
    ax2.plot(ot, mo, marker="s", color="blue", label="Moment [Nm]")
    ax2.set_ylabel("Moment M [Nm]", color="blue")

    plt.title(f"Vnější otáčková charakteristika - {motor_z['nazev']}")
    fig.tight_layout()
    plt.savefig(f"{SLOZKA_VYSTUPU}/vykon.png", dpi=150)
    plt.close(fig)
    print(f"Graf uložen do {SLOZKA_VYSTUPU}/vykon.png")
except ImportError:
    print("(matplotlib není nainstalovaný - graf přeskočen)")
