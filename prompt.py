from sys import argv

script, user_name = argv
prompt = " > "

print(f"hello, {user_name},i'm {script},your assistant.")
print("i would like to ask you some questions.")
print(f"what do you like,{user_name}?")

likes = input(prompt)

print("whats your favourite food?")

likes = input(prompt)

print(f"Whats your other name {user_name}?")

name = input(prompt)

print("How old are you?")

age = input(prompt)



