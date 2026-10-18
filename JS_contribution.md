# Osnova — co musí člověk vědět, než začne programovat

> Záměrně **ne** o syntaxi Pythonu, ale o *řemesle* okolo: nástroje, návyky, bezpečnost, spolupráce. Syntaxi se člověk doučí, tohle ne.

---

## 1. Čím a proč — volba nástrojů

- **Jazyk: Python.** Proč právě on (čitelnost, knihovny, komunita, nízká vstupní bariéra) a proč se na začátku vyhnout čemukoli složitějšímu (C++, Rust, Java).
- **Knihovny.** Co to je, odkud se berou (PyPI, `pip`), proč jejich použití vědomě omezovat — každá závislost je něco, co se rozbije, zestárne a musí se instalovat u kolegy.
- **Editor: VS Code.** Jedno prostředí pro vše — editace, spuštění, terminál, git, debugger. Proč ne Notepad + dvojklik na `.py`. Přeplácanej ale free a ez,

## 2. Verzování kódu — Git a GitHub

- **K čemu git vlastně je**: historie, návrat zpět (Při používání LLM **nutnost**)
- **GitHub**: proč mít kód mimo svůj laptop, co to řeší.
- **Základní operace**: `commit`, `push`, `pull`, `fetch` — a co která z nich dělá.
- **Private vs. public repo** — kdy co, a co to znamená pro data a tokeny.
- **`.gitignore`** — co do repa nepatří (venv, data, výstupy, tajné soubory).

## 3. Hygiena projektu („slušnost“)

- **`README.md`** — co projekt dělá, jak se spustí. Minimum, které očekává každý.
- **`requirements.txt`** — aby to šlo rozchodit i někde jinde.
- **`venv`** — proč neinstalovat balíčky globálně, jak se do prostředí vstupuje a vystupuje.
- Struktura repa: kód / data / výstupy odděleně.

## 4. Data

- **Formáty**: CSV, JSON, XML, XLSX — co je čitelné pro člověka, co pro stroj.
- **Proč preferovat JSON** (struktura, vnořená data, standard, čitelný diff).
- **Kde data nemají být**: velká a binární data do gitu nepatří.

## 5. Výstupy programu

- Co program může vracet: text/`txt`, tabulka, graf, log.
- Výstupy jsou **generované** — patří do `.gitignore`, ne do repa.

## 6. Bezpečnost

- **SSH klíče, API tokeny, hesla** — nikdy v kódu, nikdy v commitu.
- Jak to dělat správně: proměnné prostředí, `.env` + `.gitignore`.
- Pokud nevím co to je vyhnout se obloukem
## 7. LLM jako součást práce

- **Používat ho v editoru**, ne v prohlížeči — ať umí přímo editovat skript, spustit ho a přečíst si chybu.
- **NIKDY NEKOPÍROVAT KÓD Z WEBU**
- **Instrukce pro model**: co má a nemá dělat, jak si vynutit malé kroky.
- **Kontrola zůstává na člověku.** Vždy vím, co se změnilo a proč.
- Zamysle se co "prodávám" a co může být vibe code 

## 8. Typy programů / rozhraní

- **CLI** — výchozí volba, nejjednodušší, skriptovatelné.
- **TUI, GUI, webová aplikace** — co to je, kolik to stojí práce, kdy to má smysl.
- Pravidlo: začni CLI, rozhraní přidej, až když je potřeba.

## 9. Spolupráce na kódu (Optional)

- **Branch + Pull Request** — proč se nepracuje přímo v `main`.
- Review: čtení cizího kódu, komentáře, dohoda.
- **Issues / TODO** — kde se eviduje, co je potřeba udělat.

