alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u', 'v','w','x','y','z']

repeat = 'yes'

def coder(direction,text, shift):
  codeword = ""
  if (direction == 'decode'):
          shift = -1 * shift
  for letter in text:   
      if letter in alphabet:
        codeword = codeword + alphabet[(alphabet.index(letter)+shift) % len(alphabet)]
      else: 
        codeword = codeword + letter           
  return print(f'Here is your {direction}d results: {codeword}')

while repeat == 'yes':
  direction = input("Type encode or decode:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  coder(direction=direction,text=text, shift=shift)
  repeat = input("Would you like to use again: yes or no?\n").lower()

print("Thank you for using my cyther code, goodbye")
  
