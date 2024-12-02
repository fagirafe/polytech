storage = 1.44 * 1024 * 1024
pages = 100
lines = 50
symbols = 25
need = 4
size = pages * lines * symbols * need
number = storage // size
print("Количество книг, помещающихся на дискету:", int(number))