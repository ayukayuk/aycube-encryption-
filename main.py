letters =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o","p" 'Q', 's', 't', 'u', 'v',  'w', "x", "y" "z"]


direction = input("the encdoe is for encrpt and decode is for decrypt.\n").lower()
text =input("type your word\n")
shift= int(input("how many number do you want to shift\n"))

def encrypt(nice,good_amount):
       dyf =""
       for u in nice:
              ayuk= letters.index(u) +good_amount
              ayuk  %=len(letters)
              dyf +=letters[ayuk]
              print(f"my result is {dyf}")
              
              
encrypt("text", shift)
