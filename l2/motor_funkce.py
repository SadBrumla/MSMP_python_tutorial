"""
motor_funkce.py — vlastní malá knihovna motorových výpočtů (Cvičení 2)

Tohle není nic jiného než soubor .py s funkcemi. Přesně takhle vypadá
každá knihovna, kterou jste zatím importovali (math, matplotlib) — jen
tuhle jsme napsali my.

Použití z jiného skriptu ve stejné složce:

    from motor_funkce import zdvihovy_objem_l, efektivni_vykon_kw
"""

import math

# --- Geometrie motoru -------------------------------------------------------

def plocha_pistu_cm2(vrtani_mm):
    """Plocha pístu [cm2] z vrtání [mm]."""
    return math.pi * vrtani_mm ** 2 / 4 / 100


def zdvihovy_objem_l(vrtani_mm, zdvih_mm, pocet_valcu):
    """Zdvihový objem celého motoru [l].

    Parametry:
        vrtani_mm   -- vrtání [mm]
        zdvih_mm    -- zdvih [mm]
        pocet_valcu -- počet válců [-]
    """
    vrtani_m = vrtani_mm / 1000
    zdvih_m = zdvih_mm / 1000
    plocha_m2 = math.pi * vrtani_m ** 2 / 4
    return plocha_m2 * zdvih_m * pocet_valcu * 1000


def kompresni_pomer(V_z, V_c):
    """Kompresní poměr [-] ze zdvihového a kompresního objemu (stejné jednotky)."""
    return (V_z + V_c) / V_c


def stredni_pistova_rychlost(zdvih_mm, otacky=4000):
    """Střední pístová rychlost [m/s]. Výchozí otáčky 4000 1/min."""
    return 2 * (zdvih_mm / 1000) * otacky / 60


# --- Výkonové parametry -----------------------------------------------------

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
    tau = pocet_dob / 2          # počet otáček na jeden pracovní cyklus
    return p_e_pa * V_zd_m3 * (otacky / 60) / tau / 1000


def litrovy_vykon_kw_l(vykon_kw, objem_l):
    """Litrový (objemový) výkon [kW/l]."""
    return vykon_kw / objem_l


# --- Termodynamický oběh ----------------------------------------------------

def stav_po_kompresi(p1, T1, v1, epsilon, kappa=1.4):
    """Izoentropická komprese 1 -> 2. Vrací trojici (p2, T2, v2)."""
    v2 = v1 / epsilon
    p2 = p1 * epsilon ** kappa
    T2 = T1 * epsilon ** (kappa - 1)
    return p2, T2, v2


def sabatheho_obeh(p1, T1, epsilon, alpha, beta, kappa=1.4, r=287.15):
    """Sabatheho (smíšený) oběh — 5 bodů.

    Vrací trojici seznamů (tlaky [Pa], teploty [K], objemy [m3/kg]).
    """
    tlaky, teploty, objemy = [], [], []

    # Bod 1 — sání
    v1 = r * T1 / p1
    tlaky.append(p1); teploty.append(T1); objemy.append(v1)

    # Bod 2 — izoentropická komprese
    v2 = v1 / epsilon
    p2 = p1 * epsilon ** kappa
    T2 = T1 * epsilon ** (kappa - 1)
    tlaky.append(p2); teploty.append(T2); objemy.append(v2)

    # Bod 3 — izochorický přívod tepla
    v3 = v2
    p3 = p2 * alpha
    T3 = T2 * alpha
    tlaky.append(p3); teploty.append(T3); objemy.append(v3)

    # Bod 4 — izobarický přívod tepla
    p4 = p3
    v4 = v3 * beta
    T4 = T3 * beta
    tlaky.append(p4); teploty.append(T4); objemy.append(v4)

    # Bod 5 — izoentropická expanze
    v5 = v1
    p5 = p4 * (v4 / v5) ** kappa
    T5 = T4 * (v4 / v5) ** (kappa - 1)
    tlaky.append(p5); teploty.append(T5); objemy.append(v5)

    return tlaky, teploty, objemy


def tepelna_ucinnost(teploty, kappa=1.4):
    """Termická účinnost Sabatheho oběhu [-] z pěti teplot bodů oběhu."""
    T1, T2, T3, T4, T5 = teploty
    privedene = (T3 - T2) + kappa * (T4 - T3)
    odvedene = T5 - T1
    return 1 - odvedene / privedene


def vypis_obeh(nazev, tlaky, teploty, objemy):
    """Vypíše oběh jako tabulku na obrazovku. Nic nevrací."""
    print(f"\n{nazev}")
    print(f"{'bod':>4} {'p [bar]':>10} {'T [K]':>9} {'v [m3/kg]':>11}")
    for i in range(len(tlaky)):
        print(f"{i + 1:>4} {tlaky[i] / 1e5:>10.2f} {teploty[i]:>9.1f} {objemy[i]:>11.4f}")


if __name__ == "__main__":
    # Spustí se jen při `python motor_funkce.py`, ne při importu.
    objem = zdvihovy_objem_l(79.5, 95.5, 4)
    print(f"1.9 TDI PD: zdvihový objem {objem:.3f} l")
    print(f"            výkon při 4000 1/min {efektivni_vykon_kw(12.0, objem, 4000):.1f} kW")

    tlaky, teploty, objemy = sabatheho_obeh(100000, 293.15, 16.5, 1.6, 1.4)
    vypis_obeh("1.9 TDI PD — Sabatheho oběh", tlaky, teploty, objemy)
    print(f"\nTermická účinnost: {tepelna_ucinnost(teploty) * 100:.1f} %")
