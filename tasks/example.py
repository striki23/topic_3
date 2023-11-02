num_1 = 10
num_2 = 10

print(id(num_1), id(num_2), sep='\n')

line_1 = 'hello'
line_2 = 'hello'

print(id(line_1), id(line_2), sep='\n')

# атомарные типы и ссылочные типы

line_1 == line_2

line_1 is line_2

line_1 is None

id(line_1) == id(line_2)
