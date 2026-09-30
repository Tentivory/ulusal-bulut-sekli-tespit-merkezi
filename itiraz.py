#!/usr/bin/env python3
"""Itiraz masasi. Yalnizca yagmur iddiasi kabul edilir."""

import random


def itiraz_sonucu(yagmur_var_mi: bool) -> str:
    if not yagmur_var_mi:
        return "RED. Hava acik. Masamiz kapali."
    return random.choice(
        [
            "KABUL — dosya bir ust semaya havale edildi.",
            "KISMEN KABUL — bulutun yarisi resmi, yarisi degil.",
            "ERTELEME — gok gurleyince bakilacak.",
        ]
    )


if __name__ == "__main__":
    print(itiraz_sonucu(False))
    print(itiraz_sonucu(True))
