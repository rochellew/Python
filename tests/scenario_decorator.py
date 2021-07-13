import sys

def scenarios(*parameters):
    def decorator(method, parameters=parameters):
        for parameter in ((x,) if not isinstance(x, tuple) else x for x in parameters):
            def method_for_parameter(self, method=method, parameter=parameter):
                method(self, *parameter)
            args_for_parameter = ','.join(repr(y) for y in parameter)
            name_for_parameter = f"{method.__name__}({args_for_parameter})"
            frame = sys._getframe(1)
            frame.f_locals[name_for_parameter] = method_for_parameter
        return None

    return decorator