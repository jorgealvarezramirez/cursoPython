number = "0165031806510"
modified_number = ""

for digit in number:
    if digit == "0":
        modified_number += "x"
        continue
    modified_number += digit

print(modified_number)
