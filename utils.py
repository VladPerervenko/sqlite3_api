from ast import literal_eval


def string(max_length=100):
    return [f" VARCHAR({max_length})", 'str']


def integer():
    return [" INTEGER", 'int']


def list_():
    return [" TEXT", 'list']


def add_quotes(value):
    if isinstance(value, str) or isinstance(value, list):
        value = '"{}"'.format(str(value).replace('"', "'"))
    return value


def get_fields(obj):
    fields = [i for i in vars(obj).keys()]
    fields.remove('id')
    return fields


def shadow_fields(obj):
    fields = get_fields(obj)
    return len(set(fields)) != len(fields)


def get_visual(obj):
    if type(obj).__name__ == 'list':
        return [[i for i in vars(obj_class).values()] for obj_class in obj]
    return [i for i in vars(obj).values()]


def convert_to_list(obj):
    return literal_eval(obj)


opt_map = {
    'gt': '>',
    'lt': '<',
    'no': '!=',
    'egt': '>=',
    'elt': '<=',
}