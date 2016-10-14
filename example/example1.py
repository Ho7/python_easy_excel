import os
from easy_excel import Column, Sheet, Excel


class A:
    def __init__(self, a='Nothing', b='Hello my friend', c=43):
        self.a, self.b, self.c = a, b, c


excel_example = Excel()
columns = [
    Column('a', lambda x: x.b, width=5000),
    Column('b', lambda x: x.b, width=6000),
    Column('Thi is C', lambda x: x.c)
]
sheet = Sheet('New sheet', columns=columns, objects=[A(), A(b='54'), A('Hi', 'example')])
excel_example.add_sheet(sheet)

base_dir = os.path.dirname(os.path.abspath(__file__))
excel_example.save(file_name='example1', dir=base_dir + '/excel/')
