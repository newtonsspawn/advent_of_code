import csv


def intcode(init_state, input_init=1):
    state = init_state.copy()
    output_vals = []
    pos = 0
    
    def mode(mode_t, pos_t):
        if mode_t == 0:
            return state[state[pos_t]]
        elif mode_t == 1:
            return state[pos_t]
    
    while pos <= len(state) + 1:
        modes = [int(d) for d in str(state[pos]).rjust(4, '0')]
        if modes[3] == 1:
            state[state[pos + 3]] = mode(modes[1], pos + 1) + \
                                    mode(modes[0], pos + 2)
            pos += 4
            continue
        elif modes[3] == 2:
            state[state[pos + 3]] = mode(modes[1], pos + 1) * \
                                    mode(modes[0], pos + 2)
            pos += 4
            continue
        elif modes[3] == 3:
            state[state[pos + 1]] = input_init
            pos += 2
            continue
        elif modes[3] == 4:
            output_vals.append(mode(modes[1], pos + 1))
            print(f'diagnostic test output: {output_vals[-1]}')
            pos += 2
            continue
        elif modes[3] == 5:
            if mode(modes[1], pos + 1) != 0:
                pos = mode(modes[0], pos + 2)
            else:
                pos += 3
            continue
        elif modes[3] == 6:
            if mode(modes[1], pos + 1) == 0:
                pos = mode(modes[0], pos + 2)
            else:
                pos += 3
            continue
        elif modes[3] == 7:
            if mode(modes[1], pos + 1) < mode(modes[0], pos + 2):
                state[state[pos + 3]] = 1
            else:
                state[state[pos + 3]] = 0
            pos += 4
            continue
        elif modes[3] == 8:
            if mode(modes[1], pos + 1) == mode(modes[0], pos + 2):
                state[state[pos + 3]] = 1
            else:
                state[state[pos + 3]] = 0
            pos += 4
            continue
        elif modes[3] == 9:
            break
        else:
            print(
                    f'Error: Value {state[pos]} as position {pos}'
            )
            break
    
    print(f'output state: {state[0]}')
    return state[0], output_vals[-1]


if __name__ == '__main__':
    
    with open('input.csv', 'r') as f:
        reader = csv.reader(f)
        initial_state = list(reader)

    initial_state = [int(i) for i in initial_state[0]]
    print(initial_state)

    intcode(initial_state)
    
    intcode(initial_state, input_init=5)
