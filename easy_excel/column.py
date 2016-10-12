class Column(object):

    def __init__(self, name, func_get_attr_for_object=None):
        self.name = name
        self.set_get_attr_for(func_get_attr_for_object)


    def set_get_attr_for(self, func_get_attr_for_object):

        if not func_get_attr_for_object:
            func_get_attr_for_object = lambda x: getattr(x, self.name, None)

        if not callable(func_get_attr_for_object):
            raise Exception('func_get_attr_for_object need be callable')

        self.get_attr_for = func_get_attr_for_object
