###################################Задача1###############################################
with open('workwithfile.txt') as f:
    cook_book = {}
    while True:
        ingridients = []
        name = f.readline().strip()
        f.readline()

        if not name:
            break

        for line in f:
            if not line.strip():
                break
            ing = line.split(' | ')
            ingridients.append({'ingredient_name': ing[0],
                                'quantity': ing[1],
                                'measure': ing[2]})
        cook_book[name] = ingridients
print(cook_book)

###################################Задача2###############################################
def get_shop_list_by_dishes(dishes, person_count):
    unique_list = set(dishes)
    amount_ingridients = {}
    for ingridient_list in unique_list:
        for dish, ingridient in cook_book.items():
            if ingridient_list == dish:
                for ingridient_iteration in ingridient:
                    amount_ingridients[ingridient_iteration['ingredient_name']] = \
                        {'measure': ingridient_iteration['measure'],
                         'quantity': int(ingridient_iteration['quantity']) * person_count}
    return amount_ingridients


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Омлет'], 2))

###################################Задача3###############################################
content = {}
for text_i in range(1, 4):
    with open(f"{text_i}.txt") as f:
        counter = 0
        for line in f:
            counter += 1
        f.seek(0)
        content[counter] = [f.read()]
        content[counter].append(f"{text_i}.txt")

with open('original.txt', 'w') as f:
    for write_i in sorted(content):
        for item_write, value_write in content.items():
            if item_write == write_i:
                f.write(value_write[1] + '\n')
                f.write(str(item_write) + '\n')
                f.write(value_write[0] + '\n')
