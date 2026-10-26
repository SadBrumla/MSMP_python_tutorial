"""
CVIČENÍ 2 - VZOROVÉ PŘÍKLADY (pro lektora)

Ukazuje, CO program vypíše - bez toho, aby se kód psal na hodině.
ID příkladů jsou stejná jako v poznámce (PŘÍKLAD F1, S3, ...).

    python3 l2_priklady.py              # seznam všech příkladů
    python3 l2_priklady.py F3           # spustí F3 a vypíše výstup
    python3 l2_priklady.py F3 -k        # vypíše i kód (--kod)
    python3 l2_priklady.py F            # všechny příklady z funkcí
    python3 l2_priklady.py S            # všechny příklady ze souborů
    python3 l2_priklady.py all          # všechno

POZOR: spouštějte ze složky l2/, aby fungovaly relativní cesty do data/.
Příklady S5-S7 zapisují soubory do aktuální složky - to je jejich účel.

Kód, který se vypíše s -k, je přesně ten, který se spustí (čte se přes
inspect.getsource), takže se nemůže rozejít s tím, co vidíte ve výstupu.
"""
import inspect
import sys

PRIKLADY = {}
PORADI = []


def priklad(ident, nazev):
    def deco(fn):
        PRIKLADY[ident] = (nazev, fn)
        PORADI.append(ident)
        return fn
    return deco


# ============================================================================
# FUNKCE
# ============================================================================

@priklad("F1", "Tři motory, jeden vzorec, tři kopie (najdi chybu)")
def _f1():
    import math

    # Motor A: 1.9 TDI PD
    vrtani_mm = 79.5
    zdvih_mm = 95.5
    pocet_valcu = 4
    objem_A = (math.pi * (vrtani_mm / 1000) ** 2 / 4) * (zdvih_mm / 1000) * pocet_valcu
    print(f"Motor A (1.9 TDI): {objem_A * 1000:.3f} l")

    # Motor B: 1.0 TSI
    vrtani_mm = 74.5
    zdvih_mm = 76.4
    pocet_valcu = 3
    objem_B = (math.pi * (vrtani_mm / 1000) ** 2 / 4) * (zdvih_mm / 1000) * pocet_valcu
    print(f"Motor B (1.0 TSI): {objem_B * 1000:.3f} l")

    # Motor C: 2.0 TDI
    vrtani_mm = 81.0
    zdvih_mm = 95.5
    pocet_valcu = 4
    objem_C = (math.pi * (vrtani_mm / 1000) * 2 / 4) * (zdvih_mm / 1000) * pocet_valcu
    print(f"Motor C (2.0 TDI): {objem_C * 1000:.3f} l")
    print("\n(Motor C má mít ~1,97 l.)")


@priklad("F2", "Ten samý vzorec, ale jen jednou")
def _f2():
    import math

    def zdvihovy_objem_l(vrtani_mm, zdvih_mm, pocet_valcu):
        vrtani_m = vrtani_mm / 1000
        zdvih_m = zdvih_mm / 1000
        plocha_pistu_m2 = math.pi * vrtani_m ** 2 / 4
        objem_m3 = plocha_pistu_m2 * zdvih_m * pocet_valcu
        return objem_m3 * 1000              # vracíme litry

    # Definice výše nic nespočítala. Počítá se teprve při volání:
    print(f"Motor A (1.9 TDI): {zdvihovy_objem_l(79.5, 95.5, 4):.3f} l")
    print(f"Motor B (1.0 TSI): {zdvihovy_objem_l(74.5, 76.4, 3):.3f} l")
    print(f"Motor C (2.0 TDI): {zdvihovy_objem_l(81.0, 95.5, 4):.3f} l")


@priklad("F3", "return vs. print() - dvě skoro stejné funkce")
def _f3():
    import math

    def objem_print(vrtani_mm, zdvih_mm):
        objem = math.pi * (vrtani_mm / 1000) ** 2 / 4 * (zdvih_mm / 1000)
        print(objem)                # jen vypíše na obrazovku

    def objem_return(vrtani_mm, zdvih_mm):
        objem = math.pi * (vrtani_mm / 1000) ** 2 / 4 * (zdvih_mm / 1000)
        return objem                # vrátí hodnotu do programu

    a = objem_print(79.5, 95.5)
    b = objem_return(79.5, 95.5)

    print(f"a = {a}      <- do proměnné 'a' se dostalo None!")
    print(f"b = {b}      <- tady máme skutečné číslo")

    # Tenhle řádek spadne na TypeError:
    # print(a * 4)

    print(f"Objem celého čtyřválce: {b * 4 * 1000:.3f} l     <- s 'b' počítat jde")


@priklad("F4", "Výchozí hodnoty a pojmenované argumenty")
def _f4():
    def teplota_po_kompresi(T1, epsilon, kappa=1.4):
        return T1 * epsilon ** (kappa - 1)

    T_sani = 293.15     # 20 °C

    # 1) kappa neuvedeme -> použije se výchozích 1.4
    print(f"Vzduch (kappa=1.4):       {teplota_po_kompresi(T_sani, 16.5):.1f} K")

    # 2) kappa uvedeme -> přebije výchozí hodnotu
    print(f"Jiný plyn (kappa=1.35):   {teplota_po_kompresi(T_sani, 16.5, 1.35):.1f} K")

    # 3) pojmenované argumenty - na pořadí nezáleží
    print(f"Totéž, ale čitelněji:     {teplota_po_kompresi(epsilon=16.5, T1=T_sani):.1f} K")


@priklad("F5", "Funkce vracející tři hodnoty (bod 2 oběhu)")
def _f5():
    def stav_po_kompresi(p1, T1, v1, epsilon, kappa=1.4):
        """Izoentropická komprese 1 -> 2. Vrací trojici (p2, T2, v2)."""
        v2 = v1 / epsilon
        p2 = p1 * epsilon ** kappa
        T2 = T1 * epsilon ** (kappa - 1)
        return p2, T2, v2

    r = 287.15
    p1 = 100000
    T1 = 293.15
    v1 = r * T1 / p1

    p2, T2, v2 = stav_po_kompresi(p1, T1, v1, epsilon=16.5)

    print(f"Bod 1: p = {p1 / 1e5:6.2f} bar, T = {T1:6.1f} K, v = {v1:.4f} m3/kg")
    print(f"Bod 2: p = {p2 / 1e5:6.2f} bar, T = {T2:6.1f} K, v = {v2:.4f} m3/kg")


@priklad("F6", "Lokální platnost - co z funkce proleze a co ne")
def _f6():
    import math

    def vypocet_objemu(vrtani_mm, zdvih_mm):
        plocha = math.pi * (vrtani_mm / 1000) ** 2 / 4     # lokální proměnná
        objem = plocha * (zdvih_mm / 1000)                 # lokální proměnná
        return objem

    objem_valce = vypocet_objemu(79.5, 95.5)
    print(f"Objem válce: {objem_valce * 1e6:.1f} cm3       <- prošel přes return")

    # NameError: name 'plocha' is not defined
    try:
        print(plocha)
    except NameError as e:
        print(f"print(plocha) -> NameError: {e}")


@priklad("F7", "Funkce s dokumentací a help()")
def _f7():
    def efektivni_vykon_kw(p_e_bar, V_zd_l, otacky, pocet_dob=4):
        """Efektivní výkon pístového motoru.

        Parametry:
            p_e_bar   -- střední efektivní tlak [bar]
            V_zd_l    -- zdvihový objem celého motoru [l]
            otacky    -- otáčky [1/min]
            pocet_dob -- 4 pro čtyřdobý, 2 pro dvoudobý motor

        Vrací:
            efektivní výkon [kW]
        """
        p_e_pa = p_e_bar * 1e5
        V_zd_m3 = V_zd_l / 1000
        tau = pocet_dob / 2                 # otáčky na jeden pracovní cyklus
        return p_e_pa * V_zd_m3 * (otacky / 60) / tau / 1000

    print(f"Výkon: {efektivni_vykon_kw(12.0, 1.896, 4000):.1f} kW")
    print(f"Dvoudobý: {efektivni_vykon_kw(12.0, 1.896, 4000, pocet_dob=2):.1f} kW")
    help(efektivni_vykon_kw)


# ============================================================================
# PRÁCE SE SOUBORY
# ============================================================================

@priklad("S1", "Kde vlastně jsme - cesty")
def _s1():
    import os

    print("Pracovní složka:")
    print(" ", os.getcwd())

    print("\nCo v ní leží:")
    for nazev in sorted(os.listdir(".")):          # "." znamená "tato složka"
        print("  -", nazev)

    print("\nExistuje náš datový soubor?")
    cesta = "data/mereni_brzda.csv"
    print(" ", cesta, "->", os.path.exists(cesta))


@priklad("S2", "Přečteme soubor celý - a co v něm doopravdy je")
def _s2():
    with open("data/mereni_brzda.csv", "r", encoding="utf-8") as f:
        obsah = f.read()

    print("Datový typ toho, co jsme přečetli:", type(obsah))
    print("Délka ve znacích:", len(obsah))

    print("\n--- prvních 120 znaků, jak je vidí člověk ---")
    print(obsah[:120])
    print("--- totéž, jak to vidí Python (všimněte si \\n) ---")
    print(repr(obsah[:120]))


@priklad("S3", "Hlavička a první řádek - ze souboru leze vždycky str")
def _s3():
    with open("data/mereni_brzda.csv", "r", encoding="utf-8") as f:
        radky = f.readlines()              # seznam řádků (pořád text!)

    hlavicka = radky[0].strip().split(";")
    print("Názvy sloupců:  ", hlavicka)

    prvni_radek = radky[1].strip().split(";")
    print("První měření:   ", prvni_radek)
    print("Je to seznam?   ", type(prvni_radek), "o", len(prvni_radek), "prvcích")

    otacky_text = prvni_radek[0]
    print(f"\notacky_text  = {otacky_text!r}   typ: {type(otacky_text)}")
    print(f"otacky_text * 2 = {otacky_text * 2!r}   <- NEnásobí, zdvojuje text!")

    otacky_cislo = float(otacky_text)
    print(f"\notacky_cislo = {otacky_cislo}   typ: {type(otacky_cislo)}")
    print(f"otacky_cislo * 2 = {otacky_cislo * 2}   <- tohle už je počítání")


@priklad("S4", "Naměřená data + naše funkce")
def _s4():
    def stredni_pistova_rychlost(zdvih_mm, otacky):
        """Střední pístová rychlost [m/s]."""
        return 2 * (zdvih_mm / 1000) * otacky / 60

    def litrovy_vykon_kw_l(vykon_kw, objem_l):
        """Litrový (objemový) výkon [kW/l]."""
        return vykon_kw / objem_l

    otacky, vykon = [], []
    with open("data/mereni_brzda.csv", "r", encoding="utf-8") as f:
        for radek in f.readlines()[1:]:
            h = radek.strip().split(";")
            otacky.append(float(h[0]))
            vykon.append(float(h[2]))

    zdvih_mm = 95.5       # 1.9 TDI PD
    objem_l = 1.896

    # Hledání maxima cyklem
    max_vykon = 0.0
    otacky_max = 0.0
    for i in range(len(otacky)):
        if vykon[i] > max_vykon:
            max_vykon = vykon[i]
            otacky_max = otacky[i]

    print(f"Maximální výkon:    {max_vykon:.1f} kW při {otacky_max:.0f} 1/min")
    print(f"Litrový výkon:      {litrovy_vykon_kw_l(max_vykon, objem_l):.1f} kW/l")
    print(f"c_s v tomto bodě:   {stredni_pistova_rychlost(zdvih_mm, otacky_max):.2f} m/s")


@priklad("S5", "Zápis textového protokolu")
def _s5():
    otacky, vykon = [], []
    with open("data/mereni_brzda.csv", "r", encoding="utf-8") as f:
        for radek in f.readlines()[1:]:
            h = radek.strip().split(";")
            otacky.append(float(h[0]))
            vykon.append(float(h[2]))

    nazev_motoru = "1.9 TDI PD"
    objem_l = 1.896
    max_vykon = max(vykon)
    otacky_max = otacky[vykon.index(max_vykon)]

    with open("protokol.txt", "w", encoding="utf-8") as f:
        f.write("PROTOKOL O MĚŘENÍ NA MOTOROVÉ BRZDĚ\n")
        f.write("=" * 42 + "\n")
        f.write(f"Motor:            {nazev_motoru}\n")
        f.write(f"Zdvihový objem:   {objem_l:.3f} l\n")
        f.write(f"Naměřených bodů:  {len(otacky)}\n")
        f.write("-" * 42 + "\n")
        f.write(f"Maximální výkon:  {max_vykon:.1f} kW při {otacky_max:.0f} 1/min\n")

    print("Zapsáno. A hned si zkontrolujeme, co jsme vyrobili:\n")

    with open("protokol.txt", "r", encoding="utf-8") as f:
        print(f.read())


@priklad("S6", "Totéž pomocí modulu csv")
def _s6():
    import csv

    otacky2, vykon2 = [], []

    with open("data/mereni_brzda.csv", "r", encoding="utf-8", newline="") as f:
        cteni = csv.DictReader(f, delimiter=";")        # hlavičku zpracuje sám
        for radek in cteni:
            otacky2.append(float(radek["otacky"]))      # převod zůstává na nás!
            vykon2.append(float(radek["vykon_kW"]))

    print(f"Načteno {len(otacky2)} bodů.")
    print(f"První bod: {otacky2[0]:.0f} 1/min, {vykon2[0]:.1f} kW")

    with open("vysledky_csv_modul.csv", "w", encoding="utf-8", newline="") as f:
        zapis = csv.writer(f, delimiter=";")
        zapis.writerow(["otacky", "vykon_kW"])
        for i in range(len(otacky2)):
            zapis.writerow([otacky2[i], round(vykon2[i], 1)])

    print("Soubor vysledky_csv_modul.csv zapsán.")


@priklad("S7", "JSON - uložíme a načteme popis motoru")
def _s7():
    import json

    motor = {
        "nazev": "1.9 TDI PD",
        "pocet_valcu": 4,
        "vrtani_mm": 79.5,
        "zdvih_mm": 95.5,
        "preplnovany": True,
        "obeh": {"epsilon": 16.5, "alpha": 1.6, "beta": 1.4},
        "mereno_pri_otackach": [1000, 2000, 3000, 4000],
    }

    with open("motor.json", "w", encoding="utf-8") as f:
        json.dump(motor, f, indent=2, ensure_ascii=False)

    with open("motor.json", "r", encoding="utf-8") as f:
        nacteny = json.load(f)

    print("Typ načteného:  ", type(nacteny))
    print("Název:          ", nacteny["nazev"])
    print("Počet válců:    ", nacteny["pocet_valcu"], type(nacteny["pocet_valcu"]))
    print("Epsilon oběhu:  ", nacteny["obeh"]["epsilon"], "  <- slovník ve slovníku")
    print("Druhé otáčky:   ", nacteny["mereno_pri_otackach"][1], "  <- seznam ve slovníku")
    print("\nPočet válců se vrátil jako int, ne jako text. To CSV neumí.")


# ============================================================================
# SPOUŠTĚČ
# ============================================================================

def kod(fn):
    """Vrátí tělo funkce jako text - bez dekorátoru, bez def, bez odsazení."""
    radky = inspect.getsource(fn).split("\n")
    i = next(i for i, r in enumerate(radky) if r.startswith("def ")) + 1
    telo = radky[i:]
    return "\n".join(r[4:] if r.startswith("    ") else r for r in telo).strip("\n")


def spust(ident, s_kodem):
    nazev, fn = PRIKLADY[ident]
    print()
    print("=" * 76)
    print(f"PŘÍKLAD {ident}: {nazev}")
    print("=" * 76)
    if s_kodem:
        print(kod(fn))
        print("-" * 76)
        print("výstup:")
        print("-" * 76)
    fn()


def seznam():
    print(__doc__.strip())
    print("\nDostupné příklady:\n")
    for ident in PORADI:
        print(f"  {ident:<4} {PRIKLADY[ident][0]}")


def main(argv):
    if not argv:
        seznam()
        return 0

    s_kodem = any(a in ("-k", "--kod") for a in argv)
    cile = [a for a in argv if not a.startswith("-")]

    if not cile:
        seznam()
        return 0

    vybrane = []
    for c in cile:
        c = c.upper()
        if c == "ALL":
            vybrane = list(PORADI)
            break
        if c in ("F", "S"):
            vybrane += [i for i in PORADI if i.startswith(c)]
        elif c in PRIKLADY:
            vybrane.append(c)
        else:
            print(f"Neznámý příklad: {c}\n")
            seznam()
            return 1

    for ident in vybrane:
        spust(ident, s_kodem)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
