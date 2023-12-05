def simple_assembler(program):
    registers = {}
    index = 0
    while index < len(program):
        commands = program[index].split(' ')

        if commands[0] == 'mov':
            if commands[2].isdigit():
                registers[commands[1]] = int(commands[2])
            else:
                registers[commands[1]] = registers[commands[1]]

        elif commands[0] == 'inc':
            registers[commands[1]] += 1

        elif commands[0] == 'dec':
            registers[commands[1]] -= 1

        elif commands[0] == 'jnz':
            if int(commands[2]) == -5:
                z = 0
            if commands[1].isdigit():
                if int(commands[1]) > 0:
                    index += int(commands[2])
                    if int(commands[2]) < 0: 
                        continue
            else:
                if registers[commands[1]] > 0:
                    index += int(commands[2])
                    if int(commands[2]) < 0: 
                        continue



        index += 1
    
    # return a dictionary with the registers
    print(registers)
    return registers

codes = ['''\
mov a 5
jnz a 1
inc a
dec a
dec a
jnz a -1
inc a''',
'''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''
]
for code in codes:
    simple_assembler(code.splitlines()) # {'a': 1}
