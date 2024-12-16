def calculate_luhn_digit(card_number):

    # Convertir le numéro en liste d'entiers
    digits = [int(d) for d in str(card_number)]

    if len(digits) != 15:
        raise ValueError("Le numéro de carte doit être une chaîne de 15 chiffres.")


    # Appliquer l'algorithme de Luhn
    checksum = 0
    for i in range(len(digits)):
        if i % 2 == 0:  # Indices pairs pour une longueur de 15 chiffres
            doubled = digits[-(i + 1)] * 2
            checksum += doubled if doubled < 10 else doubled - 9
        else:
            checksum += digits[-(i + 1)]

    # Calculer le chiffre de contrôle
    control_digit = (10 - (checksum % 10)) % 10

    return control_digit

while True:
    try:
        user_input = input("Entrez un numéro de carte de crédit de 15 chiffres : ")
        luhn_digit = calculate_luhn_digit(user_input)
        print("Le dernier chiffre (chiffre de contrôle) est :", luhn_digit)
        break
    except ValueError as error:
        print(error)