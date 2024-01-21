message = input("Write something") #input() allows to type something and this command will be performed
print(message)

#Program will ask about type of car and later it will generate the message that is checking the database 
message = input("Which car would you like to rent? Please type a car brand in the bracket")
print(f'We are checking if {message.title()} is availble.')

#Code will check if user is over 18 and able to vote
age = input("Please write your age: ")
age = int(age)
if age >= 18:
    print(f'You are {age}, you can vote')
else:
    print('You are under 18, you cannot vote')

#While basic code
current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1

#While and message ""
prompt = "\nWrite something here: "
prompt += "\nIf you want to end, write 'end' "
message = "" 
while message != 'end':
    message = input(prompt)
    print(message)

#Flag
prompt = "\nWrite something here: "
prompt += "\nIf you want to end, write 'end' "
active = True
while active:
    message = input(prompt)

    if message == 'end':
        active = False
    else:
        print(message)

#Break command
prompt = "\nWrite cities that you want to visit: "
prompt += "\n(If you want to end, write 'end'.) "

while True:
    city = input(prompt)

    if city == 'end':
        break
    else:
        print(f'I wanna visit {city.title()}')

#Collect data regarding name and holidays
responses = {}

polling_active = True
while polling_active:
        name = input('\What is your name?')
        response = input("What is your holiday destination?")
        
        responses[name]=response

        repeat = input('Is there anyone else to share his wishies? (Yes/No)')
        if repeat == 'No':
            polling_active = False
for name, response in responses.items():
    print(f'{name.title()} wants to visit {response}')