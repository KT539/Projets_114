# NAME: Ex-Limites_Types.py
# AUTHOR: Kilian Testard
# DATE: 11.11.2024

# Code écrit par ChatGPT
import sys


def calculate_c_integer_limits_and_memory():
    # Définition des types et des limites pour les entiers en C
    types = {
        'CHAR': (-2 ** 7, 2 ** 7 - 1, 1),  # 8 bits, signé
        'UNSIGNED CHAR': (0, 2 ** 8 - 1, 1),  # 8 bits, non signé
        'SHORT': (-2 ** 15, 2 ** 15 - 1, 2),  # 16 bits, signé
        'UNSIGNED SHORT': (0, 2 ** 16 - 1, 2),  # 16 bits, non signé
        'INT': (-2 ** 31, 2 ** 31 - 1, 4),  # 32 bits, signé
        'UNSIGNED INT': (0, 2 ** 32 - 1, 4),  # 32 bits, non signé
        'LONG': (-2 ** 31, 2 ** 31 - 1, 4),  # Généralement 32 bits, signé
        'UNSIGNED LONG': (0, 2 ** 32 - 1, 4),  # 32 bits, non signé
        'LONG LONG': (-2 ** 63, 2 ** 63 - 1, 8),  # 64 bits, signé
        'UNSIGNED LONG LONG': (0, 2 ** 64 - 1, 8),  # 64 bits, non signé
    }

    print("Limites et allocation mémoire pour chaque type d'entier simulé (en C) :")

    for type_name, (min_val, max_val, size_in_bytes) in types.items():
        # Création d'un exemple d'entier pour calculer l'utilisation de mémoire
        example_value = max_val if size_in_bytes == 8 else min_val + (max_val - min_val) // 2  # Exemple dans la plage
        size_of_type = sys.getsizeof(example_value)  # Utilisation de sys.getsizeof pour la mémoire utilisée

        # Affichage des limites et de la taille mémoire
        print(
            f"{type_name} : Min = {min_val}, Max = {max_val}, Taille mémoire estimée = {size_of_type} octets (estimation de Python)")


def memory_usage_for_integer_types():
    print("\nExemples de consommation de mémoire pour divers types d'entiers en Python :")
    values = [0, 127, 128, 2 ** 8 - 1, 2 ** 16 - 1, 2 ** 31, 2 ** 63]

    for value in values:
        size = sys.getsizeof(value)
        print(f"Valeur = {value}, Mémoire utilisée = {size} octets")


# Appel des fonctions pour afficher les résultats
calculate_c_integer_limits_and_memory()
memory_usage_for_integer_types()