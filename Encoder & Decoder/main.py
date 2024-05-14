from Alphabet import alphabet
from logo import logo

print(f" '\n' {logo}  '\n' ")

restart = True
while restart == True:
    direction = input("Type 'encode' if you want to encode an message and type 'decode' if you want to decode an encoded message: \n").lower()
    text = input("Enter your text: \n").lower()
    shift = int(input("Enter the Shift number: "))

    while shift > 26:
       shift %= 26


    def encrypt(the_text, the_shift):
        cipher_text = ""
        for char in the_text:
            if char in alphabet:
                shift_of_letter = alphabet.index(char)
                new_shift = shift_of_letter + the_shift
                cipher_text += alphabet[new_shift]
            else:
                cipher_text += char
            # cipher_text += new_letter
        print(f"The encoded text is:  {cipher_text}")

    def decrypt(crypted_text, the_shift):
        crypt_text = ""
        for char in crypted_text:
            if char in alphabet:
                shift_of_letter = alphabet.index(char)
                new_shift = shift_of_letter - the_shift
                crypt_text += alphabet[new_shift]
            else:
                crypt_text += char
            # crypt_text += new_letter
        print(f"The decoded text is:  {crypt_text}")


    if direction == "encode":
        encrypt(the_text=text , the_shift=shift)
    elif direction == "decode":
        decrypt(crypted_text=text, the_shift=shift)

    restart = input("Do you want to start again Type ' yes ' or ' no '?  ").lower()

    if restart == "yes":
        restart = True
    elif restart == "no":
        print("Good bye \n")
        restart = False
    else:
        print("Wrong choose")
        restart = False


#Second form of code(using just 1 function):{
#
# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#       shift_amount *= -1
#   for letter in start_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     end_text += alphabet[new_position]
#   print(f"Here's the {direction}d result: {end_text}")



# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
#}
