def trace_gen(before, step):
    number_gen = int.from_bytes(before, 'big')
    number_gen += step
    nextable = number_gen.to_bytes(len(before), 'big')
    return nextable
