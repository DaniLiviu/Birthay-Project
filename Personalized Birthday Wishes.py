#Asking what is your Name
user_name = input("Hi what's your name? ")
#Aks what year was born.
age = int(input(f"Hello {user_name} What year the recipient was born in?(ex:1900)? "))
#Ask what is the Recipient's Name
user_name1 = input("What is the recipient's Name? ")
#Aks customer to add special message.
message = input("Please add a special message/mempory that you would like\nto shard with the recipient : ")
print()
print()
a = 2024
b = age
user_age = a - b
print(f"Hello, {user_name1}, Let's celebrate your {user_age}, years of awesomeness!\n")
print(f'Wishing you a day filled with joy and laughter as you turn', {user_age},'year old!!\n')
print(message)
print(f"\n\nWith love and best wishes,\n\n\n {user_name}")
