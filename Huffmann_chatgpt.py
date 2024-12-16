import heapq
from collections import Counter, defaultdict


# Étape 1 : Calculer la fréquence des caractères
def calculate_frequencies(text):
    return Counter(text)


# Étape 2 : Construire l'arbre de Huffman
def build_huffman_tree(frequencies):
    heap = [[weight, [char, ""]] for char, weight in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


# Étape 3 : Générer un dictionnaire de codage
def create_huffman_dict(huffman_tree):
    return {char: code for char, code in huffman_tree}


# Étape 4 : Encoder la phrase
def huffman_encode(text, huffman_dict):
    return ''.join(huffman_dict[char] for char in text)


# Étape 5 : Décoder une chaîne encodée
def huffman_decode(encoded_text, huffman_dict):
    reverse_dict = {code: char for char, code in huffman_dict.items()}
    current_code = ""
    decoded_text = ""

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_dict:
            decoded_text += reverse_dict[current_code]
            current_code = ""

    return decoded_text


# Exemple avec "compression sans perte"
text = "compression sans perte"
frequencies = calculate_frequencies(text)
huffman_tree = build_huffman_tree(frequencies)
huffman_dict = create_huffman_dict(huffman_tree)

encoded_text = huffman_encode(text, huffman_dict)
decoded_text = huffman_decode(encoded_text, huffman_dict)

# Résultats
print("Texte original :", text)
print("Fréquences des caractères :", frequencies)
print("Arbre de Huffman :", huffman_tree)
print("Dictionnaire de Huffman :", huffman_dict)
print("Texte encodé :", encoded_text)
print("Texte décodé :", decoded_text)