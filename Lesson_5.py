#=====#1=====

f = open("my_file.txt", 'w')
x = input("введите информацию!\n")

for i in x:
    f.writelines(x)
    x = input ("введите информацию!\n")
    if not x: break

f.close()
f = open('my_file.txt', 'r')
content = f.readlines()
print(content)
f.close()

#=====#2=====

my_f = open("Test2.txt", "r", encoding="UTF-8")
print(f'Число слов: {len(my_f.read().split())}')
my_f.close()

my_f = open("Test2.txt", "r", encoding="UTF-8")
print(f'Число строк: {len(my_f.readlines())}')
my_f.close()

#=====#3=====

with open("Text_3.txt", "r", encoding="utf-8") as f:
    d = {}
    for i in f:
        i = i.split(" ")
        d[i[0]] = float(i[1])
    print(f'Зарплаты ниже 20т.р.: {[k for k,v in d.items() if v<20000]}')
    print(f'Средняя зарплата: {sum(d.values())/len((d.values()))}')

#=====#4=====

d = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Сорок восемь"}

with open("Text_44.txt", "w", encoding="UTF-8") as f1:
    with open("Text_4.txt", "r", encoding="UTF-8") as f:
        f1.writelines([i.replace(i.split()[0], d.get(i.split()[0])) for i in f])

#=====#5=====

import random
n = 100
with open("Text_5.txt", "w", encoding="UTF-8") as f:
    x = [random.randint(1,n) for n in range(1,n)]
    f.write(" ".join(map(str, x)))
    print(f"Сумма: {sum(x)}")

#=====#6=====

d = {}
var = 'r'
with open ("text_6.txt", 'r', encoding="UTF-8") as f:
    for i in f:
        i = i.replace('-','').replace('(л)','').replace('(пр)','').replace('(лаб)', '').replace('.', '')
        d [i.split()[0]]=sum(map(int,i.split()[1:]))
    print(d)

#=====#7=====

import json

with open("text_7.json", 'w', encoding='utf-8') as f1:
    with open("text_7.txt", 'r', encoding='utf-8') as f:
        x = {i.split()[0]:int(i.split()[2])-int(i.split()[3]) for i in f}
        y = [x, {'средняя прибыль': sum([v for k,v in x.items() if v > 0]) / len([v for k,v in x.items() if v > 0])}]
        print(y)

    json.dump(y, f1, ensure_ascii=False, indent=4)