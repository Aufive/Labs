sort = str.lower(input('Введите строку:'))
print('Виберіть дію: \n 1:сортувати слова \n 2:показати кількість букв')
choice = input(':::')
splsort = sort.split()  #розділяєм строку за допомогою метода спліт
a = set(splsort)
e = ''
d = {}
for i in sorted(a):
    if len(i) > 3: #якщо більше трьох букв то воно працює
        e += ' ' + i
    else:
        continue
if choice == '1':
    print(e)
elif choice == '2':
    for litera in set(e): #set - сортує повторющі елементи в рандомному порядку
        if litera != ' ':
            d[litera] = e.count(litera) #вираховує скільки раз значення зустрічається в списку або строці задана літера
        else:
            continue
    print(d)
else:
    print('Ви обрали неправильно!')