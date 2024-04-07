alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

sentence = input("Please enter a sentence: ").lower()
shift = input("Please enter the number of shifts: ")
cipher = ""
for letter in sentence:

  if letter in alphabet:
    position = alphabet.index(letter)
    new_position = position + int(shift)
    new_letter = alphabet[new_position]
    cipher += new_letter
  else:
    new_letter = letter
    cipher += letter
print(cipher)
