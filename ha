#!/usr/bin/env bash
# ha - uruchom Hatari (Atari 1040STFM + EmuTOS) z podaną dyskietką w napędzie A
# Użycie: ha [-w] [-s] plik.st|.msa|.stx|.zip [dodatkowe opcje hatari]
#   -w   pozwól zapisywać na dyskietce (domyślnie obraz jest chroniony przed zapisem)
#   -m st|ste   typ maszyny (domyślnie st)      -M KB   pamięć RAM (domyślnie 1024)
#   -t plik.img obraz TOS (domyślnie TOS 1.04 GB)
#   -s   wczytuj dyskietkę z prawdziwą prędkością napędu (domyślnie: maksymalna)

HATARI=${HATARI:-hatari}
TOS=${TOS:-$HOME/atarist/tos/tos104gb.img}
MACHINE=st
MEM=1024

protect=on
fastfdc=true
while [ "$1" = "-w" ] || [ "$1" = "-s" ] || [ "$1" = "-m" ] || [ "$1" = "-M" ] || [ "$1" = "-t" ]; do
    case "$1" in
        -w) protect=off ;;
        -s) fastfdc=false ;;
        -m) MACHINE=$2; shift ;;
        -M) MEM=$2; shift ;;
        -t) TOS=$2; shift ;;
    esac
    shift
done

if [ -z "$1" ]; then
    echo "Użycie: ha [-w] plik_dyskietki [opcje hatari]" >&2
    exit 1
fi

disk=$1
shift

if [ ! -f "$disk" ]; then
    echo "ha: nie ma pliku: $disk" >&2
    exit 1
fi

# ścieżka bezwzględna, żeby działało z dowolnego katalogu
disk=$(realpath -- "$disk")

exec "$HATARI" --machine "$MACHINE" --memsize "$MEM" --tos "$TOS" \
    --fullscreen --fastfdc "$fastfdc" --protect-floppy "$protect" --disk-a "$disk" "$@" 2>/dev/null
