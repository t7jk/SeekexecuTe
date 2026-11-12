# SeekexecuTe

**English** | [Polski](#polski)

A graphical browser and launcher for Atari ST floppy-disk collections, built for the [Hatari](https://hatari.tuxfamily.org/) emulator. Browse a large archive of disk images (`.st`, `.msa`, `.stx`, `.zip`), see the cover art and description of each game, and start it in Hatari with one key press.

## Features

- Three-pane GTK 4 interface drawn in the pixel font "Atari ST": file tree on the left, cover top right, description bottom right.
- Browses a local folder or a network share (SMB/CIFS) with the disk archive; can mount the share on start.
- Finds covers and descriptions from a GameBase-style folder layout.
- Categories (Point And Click Adventures, Fire And Destroy, Strategy, Jump And Run, Text Adventure) and a favorites list.
- Choice of emulated machine and TOS: 520ST, 1040ST, 1040STFM, 1040STE with TOS 1.00 / 1.02 / 1.04 / 1.06 / 1.62 or EmuTOS.
- Fully keyboard driven, cached index for fast start-up, fullscreen mode.

## Requirements

- Python 3 with PyGObject and pycairo
- GTK 4, Pango, PangoCairo, GdkPixbuf (GObject introspection typelibs)
- [Hatari](https://hatari.tuxfamily.org/) and TOS (or EmuTOS) images, which are **not** included
- `mount.cifs` (cifs-utils) if you want to mount a network share
- The "Atari ST" font by Patrick H. Lauke ([FontStruct](https://fontstruct.com/), CC BY), installed in `~/.local/share/fonts`

On Fedora: `sudo dnf install python3-gobject python3-cairo gtk4 hatari cifs-utils`

## Installation

```sh
git clone https://github.com/t7jk/SeekexecuTe.git
cd SeekexecuTe
install -m 755 ha ~/.local/bin/ha      # launcher wrapper around Hatari
chmod +x SeekexecuTe
./SeekexecuTe
```

The `ha` wrapper starts Hatari with a disk in drive A. It reads two optional environment variables: `HATARI` (path to the Hatari binary, default `hatari`) and `TOS` (default TOS image).

## Usage

```sh
./SeekexecuTe            # start, using the cached index
./SeekexecuTe --rescan   # rescan the archive first and refresh the cache
```

Put your TOS images in `~/atarist/tos` and your disk archive in `~/atarist/ATARI_ST`, or change both in the settings screen (`c`). Settings are stored in `~/.config/SeekexecuTe/` and the index cache in `~/.cache/SeekexecuTe/`.

| Key | Action |
|---|---|
| `↑` `↓` | Move |
| `→` / Enter | Open folder / run disk in Hatari |
| `←` / Esc | Back |
| `[` `]` | Page up / down |
| `<` `>` | Top / end of list |
| Space | Wide list |
| `-` `=` | Scroll description |
| `a` | Add / remove favorite |
| Tab | Show favorites |
| `t` | Choose machine / TOS |
| `c` | Settings (archive path, network share, credentials) |
| `f` | Fullscreen |
| `R` | Rescan the archive |
| `q` | Quit |

### Tools

`tools/` contains helper scripts used to build the category list (`categories.json`) from GameBase descriptions and TOSEC names: `prep-categories.py`, `merge-categories.py`, `merge-tosec.py`.

## License

GPL-3.0, see [LICENSE](LICENSE).

---

# Polski

Graficzna przeglądarka i launcher kolekcji dyskietek Atari ST dla emulatora [Hatari](https://hatari.tuxfamily.org/). Przeglądasz duże archiwum obrazów dyskietek (`.st`, `.msa`, `.stx`, `.zip`), widzisz okładkę i opis każdej gry i uruchamiasz ją w Hatari jednym klawiszem.

## Funkcje

- Trzypanelowy interfejs GTK 4 rysowany czcionką pikselową „Atari ST”: drzewo plików po lewej, okładka u góry po prawej, opis u dołu po prawej.
- Przegląda lokalny folder lub udział sieciowy (SMB/CIFS) z archiwum dyskietek; potrafi zamontować udział przy starcie.
- Znajduje okładki i opisy w układzie folderów w stylu GameBase.
- Kategorie (Point And Click Adventures, Fire And Destroy, Strategy, Jump And Run, Text Adventure) oraz lista ulubionych.
- Wybór emulowanej maszyny i TOS: 520ST, 1040ST, 1040STFM, 1040STE z TOS 1.00 / 1.02 / 1.04 / 1.06 / 1.62 lub EmuTOS.
- Pełna obsługa z klawiatury, indeks w pamięci podręcznej dla szybkiego startu, tryb pełnoekranowy.

## Wymagania

- Python 3 z PyGObject i pycairo
- GTK 4, Pango, PangoCairo, GdkPixbuf (typelibs GObject Introspection)
- [Hatari](https://hatari.tuxfamily.org/) oraz obrazy TOS (lub EmuTOS), które **nie** są dołączone
- `mount.cifs` (cifs-utils), jeśli chcesz montować udział sieciowy
- Czcionka „Atari ST” autorstwa Patricka H. Lauke ([FontStruct](https://fontstruct.com/), CC BY), zainstalowana w `~/.local/share/fonts`

Na Fedorze: `sudo dnf install python3-gobject python3-cairo gtk4 hatari cifs-utils`

## Instalacja

```sh
git clone https://github.com/t7jk/SeekexecuTe.git
cd SeekexecuTe
install -m 755 ha ~/.local/bin/ha      # skrypt uruchamiający Hatari
chmod +x SeekexecuTe
./SeekexecuTe
```

Skrypt `ha` uruchamia Hatari z dyskietką w napędzie A. Czyta dwie opcjonalne zmienne środowiskowe: `HATARI` (ścieżka do Hatari, domyślnie `hatari`) i `TOS` (domyślny obraz TOS).

## Użycie

```sh
./SeekexecuTe            # start z użyciem zapisanego indeksu
./SeekexecuTe --rescan   # najpierw przeskanuj archiwum i odśwież indeks
```

Obrazy TOS umieść w `~/atarist/tos`, a archiwum dyskietek w `~/atarist/ATARI_ST`, albo zmień obie ścieżki w ustawieniach (`c`). Ustawienia są w `~/.config/SeekexecuTe/`, a pamięć podręczna indeksu w `~/.cache/SeekexecuTe/`.

| Klawisz | Działanie |
|---|---|
| `↑` `↓` | Ruch po liście |
| `→` / Enter | Otwórz folder / uruchom dyskietkę w Hatari |
| `←` / Esc | Wstecz |
| `[` `]` | Strona w górę / w dół |
| `<` `>` | Początek / koniec listy |
| Spacja | Szeroka lista |
| `-` `=` | Przewijanie opisu |
| `a` | Dodaj / usuń z ulubionych |
| Tab | Pokaż ulubione |
| `t` | Wybór maszyny / TOS |
| `c` | Ustawienia (ścieżka archiwum, udział sieciowy, dane logowania) |
| `f` | Pełny ekran |
| `R` | Przeskanuj archiwum |
| `q` | Wyjście |

### Narzędzia

Katalog `tools/` zawiera skrypty pomocnicze do budowy listy kategorii (`categories.json`) na podstawie opisów GameBase i nazw TOSEC: `prep-categories.py`, `merge-categories.py`, `merge-tosec.py`.

## Licencja

GPL-3.0, zobacz [LICENSE](LICENSE).
