import inspect
 
def introspection_info(obj):

    obj_type = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not attr.startswith('__')]

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    module = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else '__main__'

    parents = [parent.__name__ for parent in inspect.getmro(type(obj))[1:]] if inspect.isclass(type(obj)) else []

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
        'parents': parents
    }

    return info

number_info = introspection_info(42)
print(number_info)


