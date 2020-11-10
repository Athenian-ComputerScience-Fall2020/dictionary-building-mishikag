# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  none
pet_names = {}

while True:
    key = input("please enter a key ")
    if key == "quit":
        end = True
        break
    value = input("please enter a value ")
    if value == "quit":
        end = True
        break
    pet_names.update({key:value})

if end == True:
    for key, value in pet_names.items():
        print(key, ':', value)
