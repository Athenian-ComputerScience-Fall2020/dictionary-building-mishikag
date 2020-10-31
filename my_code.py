# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  none
pet_names = {}

while True:
    key = input("please enter a key ")
    if key == "quit":
        break
    value = input("please enter a value ")
    if value == "quit":
        break
    pet_names.update({key:value})

for key, value in pet_names.items():
    print(key, ' : ', value)

if key=="quit":
    print(pet_names)
    print("okay you are done")




