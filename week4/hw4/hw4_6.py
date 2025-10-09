def Contradiction_str(first_letter, second_letter):
    counter = 0
    for first_letter, second_letter in zip(first_letter, second_letter):
        if first_letter != second_letter:
            counter += 1
    return counter
print(Contradiction_str("cOoL", "colL"))