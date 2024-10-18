alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u', 'v','w','x','y','z']

direction = input("Type encode or decode:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def coder(direction,text, shift):
  codeword = ""
  for letter in text:
    if (direction == 'encode'):
      codeword = codeword + alphabet[(alphabet.index(letter)+shift) % len(alphabet)]
    elif(direction == 'decode'):
      codeword = codeword + alphabet[(alphabet.index(letter)-shift) % len(alphabet)]
  return print(f'here is your results: {codeword}')

coder(direction=direction,text=text, shift=shift)
