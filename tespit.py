#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ulusal Bulut Sekli Tespit Merkezi — cekirdek motor.

Bu yazilim, gokyuzundeki cisimleri resmi evrak diline cevirir.
Hicbir meteorolojik iddia tasimaz. Tasisa bile dilekce ister.
"""

from __future__ import annotations

import argparse
import hashlib
import random
import sys
from datetime import datetime

SEKILLER = [
    "uyuyan mufettis",
    "imzasi unutulmus tutanak",
    "kaybolmus evrak dosyasi",
    "uc basli damga",
    "bekleyen vatandas kuyrugu",
    "cay bardaği silueti",
    "resmi tatil ilani",
    "asiri ciddi mubasir",
    "ruzgarla savrulan dilekce",
    "iki kati komisyon raporu",
]

KARARLAR = [
    "TESPIT EDILMISTIR",
    "INCELEMEYE ALINMISTIR",
    "BILGI ICIN GERI GONDERILMISTIR",
    "UST YAZI BEKLENMEKTEDIR",
    "HAVADAN GELEN EVRAK SAYILMISTIR",
]


def evrak_no(metin: str) -> str:
    h = hashlib.sha256(metin.encode("utf-8")).hexdigest()[:8].upper()
    return f"UBSTM-2026-{h}"


def tespit_et(gozlem: str | None = None) -> str:
    tohum = gozlem or datetime.now().isoformat()
    rng = random.Random(int(hashlib.md5(tohum.encode()).hexdigest(), 16))
    sekil = rng.choice(SEKILLER)
    karar = rng.choice(KARARLAR)
    yogunluk = rng.randint(12, 97)
    no = evrak_no(tohum + sekil)
    saat = datetime.now().strftime("%d.%m.%Y %H:%M")
    return (
        f"T.C.\nULUSAL BULUT SEKLI TESPIT MERKEZI\n"
        f"----------------------------------------\n"
        f"Evrak No : {no}\n"
        f"Tarih    : {saat}\n"
        f"Gozlem   : {gozlem or 'serbest hava bakisi'}\n"
        f"Sekil    : {sekil}\n"
        f"Yogunluk : %{yogunluk}\n"
        f"Karar    : {karar}\n"
        f"----------------------------------------\n"
        f"Not: Itirazlar yalnizca yagmurlu gunlerde kabul edilir.\n"
    )


def main() -> int:
    p = argparse.ArgumentParser(
        description="Gokyuzunu resmi dile ceviren milli yazilim."
    )
    p.add_argument("-g", "--gozlem", help="Ne gordugunu soyle, biz evraka donusturelim.")
    args = p.parse_args()
    print(tespit_et(args.gozlem))
    return 0


if __name__ == "__main__":
    sys.exit(main())
