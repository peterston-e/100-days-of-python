alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text, shift, direction):
  caesar_text = ""
  
  for i in text:
    position = alphabet.index(i)
    # could have done in a different way. 
    # check if direction is decode * -1 which would turn to a negative number. then you only write newposition once. 
    if direction == "encode":
      new_position = position + shift
      caesar_text += alphabet[new_position]
    elif direction == "decode":
      new_position = position - shift
      caesar_text += alphabet[new_position]
  print(f"The {direction}d text is: {caesar_text}")


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text=text, shift=shift, direction=direction)