pets = {}

pet_name = input("Введите имя питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

pets[pet_name] = {
    'Вид питомца': pet_type,
    'Возраст питомца': pet_age,
    'Имя владельца': owner_name
}

print(pets)