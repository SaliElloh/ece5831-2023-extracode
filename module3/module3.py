import and_gate as ag

x1 = 1
x2 = 0

print(f'The output of {x1} and {x2} is {ag.and_gate(x1, x2)}')

#this show that  after importing, this part of code is not run,
#  it is only used for testing without having to create new variables

# import logic_gate as lg

# logic_gate = lg.LogicGate()

# logic_gate.and_gate(1, 0)
# logic_gate.print_output('AND')

# logic_gate.or_gate(1, 0)
# logic_gate.print_output('OR')