def compose(g, f):
    def h(*args, **kwargs):
        return g(f(*args, **kwargs))
    return h


inch_to_foot= lambda x: x/12
foot_meter= lambda x: x * 0.3048
inch_to_meter = compose(foot_meter, inch_to_foot)
print(inch_to_meter(12))   # Output 0.3048
