import os
from easy_excel import Column, Sheet, Excel


class CustomTemplateSheet(Sheet):
    title = 'Example title sheet'
    name = 'Example name sheet'
    columns = [
        Column('first', lambda x: x['first']),
        Column('this is second', lambda x: x['second'], width=15000),
    ]

excel = Excel()
objects = [
    {'first': "I'm first", 'second': 'Hi'},
    {'first': '1', 'second': 2},
    {'first': 'and me', 'second': 'and you'},
    {'first': 'and me', 'second': 'and you'},
    {'first': 'and me', 'second': 'and you'},
    {'first': 'and me', 'second': 'and you'},
    {'first': 'and me', 'second': 'and you'},
    {'first': 'and me', 'second': 'and you'},
]
sheet1 = CustomTemplateSheet(objects=objects)
sheet2 = CustomTemplateSheet(name='Im second sheet', title='Im for first object', object=objects[0])

excel.add_sheet(sheet1)
excel.add_sheet(sheet2)

base_dir = os.path.dirname(os.path.abspath(__file__))
excel.save(file_name='example2', dir=base_dir + '/excel/')