
import random

import time, sys
another_question ="yes"
while another_question == "yes":
  str(input("Welcome Enter your question: ")).lower()

  print("Predicting...")
  time.sleep (1)
  print("4...")
  time.sleep (1)
  print("3...")
  time.sleep (1)
  print("2...")
  time.sleep (1)
  print("1...")
  time.sleep (1)
  print()
  
  random_number = random.randint(1,9)
 #print(random_number) <-- making sure the random generator was working
 

if random_number == 1:
  print('Yes - it will definitely happen')
elif random_number == 2:
  print('It is decidedly so')
elif random_number == 3:
  print('Without a doubt')
elif random_number == 4:
  print("I'm getting some interference from the other side. Try asking a different question")
elif random_number == 5:
  print('Try asking in a different way.')
elif random_number == 6:
  print('Better not tell you now. It would change your life too much.')
elif random_number == 7:
  print('My sources say no')
elif random_number == 8:
  print("The outlook isn't so good")
elif random_number == 9:
  print('Very doubtful')
else: 
  print("I don't understand that question. Why don't you try asking a different way!")

  another_question = str(input("Shall we beseech the spirits to answer another question? yes/no ")).lower()
  if another_question == 'no':
      print("Then goodbye! Thanks for playing.")
      time.sleep (1)
      sys.exit

  
  

