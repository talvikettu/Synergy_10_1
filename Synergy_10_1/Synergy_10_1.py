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

last_digit = int(str(pets[pet_name]["Возраст питомца"])[-1])

if last_digit==1:
    line = "год."
elif pets[pet_name]["Возраст питомца"] < 10 and last_digit>=2 and 4>=last_digit:
    line="года."
elif 5<=pets[pet_name]["Возраст питомца"]<=20:
    line="лет."
elif pets[pet_name]["Возраст питомца"]>20 and 2<=last_digit<=4:
    line="год."
elif pets[pet_name]["Возраст питомца"]>20 and (5<=last_digit<=9 or last_digit==0):
    line = "лет."

print("Это ",pets[pet_name]["Вид питомца"]," по кличке ",next(iter(pets)), ". Возраст: ", pets[pet_name]["Возраст питомца"]," ",line," Имя владельца: ", pets[pet_name]["Имя владельца"])