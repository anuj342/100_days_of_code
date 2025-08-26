def cipher():
    user_input = input("Do u want to encode or decode: ").lower()
    message = input("Write the message: ")
    shift = int(input("How many shifts you want: "))
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for letter in message:
        if letter.lower() in alphabet:
            idx = alphabet.index(letter.lower())
            
            if user_input == 'encode':
                new_idx = (idx + shift) % 26
            elif user_input == 'decode':
                new_idx = (idx - shift) % 26
            else:
                print("invalid choice")
        
            new_letter = alphabet[new_idx]
            if letter.isupper():
                new_letter = new_letter.upper()

            result += new_letter
        else:
            result += letter   
    if user_input == 'encode':
        print(f"Encrpyted message: {result}")
    else:
        print(f"Decypted message: {result}")    
cipher()