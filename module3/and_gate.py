def and_gate(x1, x2):
    w1 = 0.5
    w2 = 0.5
    th = 0.99

    if w1*x1 + w2*x2 > th:
        return 1
    else:
        return 0
    

x1 = 0
x2 = 0
out = and_gate(x1, x2)

print(f'The output of {x1} AND {x2} is {out}')