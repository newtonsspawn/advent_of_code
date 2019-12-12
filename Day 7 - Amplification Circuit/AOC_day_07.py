import csv
from itertools import permutations


def intcode(amp_control, input_init, loop=False, amp=0,
            amp_state_input={}, pos_state_input={}, stop_flag=False):
    state = amp_control.copy()
    output_vals = []
    if loop:
        pos = pos_state_input[amp]
    else:
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
            if loop:
                if not input_init:
                    amp_state_input[amp] = state
                    pos_state_input[amp] = pos
                    return output_vals[-1], amp_state_input, \
                           pos_state_input, stop_flag
            state[state[pos + 1]] = input_init[0]
            input_init.pop(0)
            pos += 2
            continue
        elif modes[3] == 4:
            output_vals.append(mode(modes[1], pos + 1))
            # print(f'diagnostic test output: {output_vals[-1]}')
            # if loop:
            #     amp_state_input[amp] = state
            #     return output_vals[-1], amp_state_input
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
            if loop:
                stop_flag = True
                amp_state_input[amp] = state
                pos_state_input[amp] = pos
                return output_vals[-1], amp_state_input, \
                       pos_state_input, stop_flag
            else:
                break
        else:
            print(
                    f'Error: Value {state[pos]} as position {pos}'
            )
            break
    
    return output_vals


def amplify(amp_control, signal):
    out_1 = intcode(amp_control, input_init=[signal[0], 0])[-1]
    out_2 = intcode(amp_control, input_init=[signal[1], out_1])[-1]
    out_3 = intcode(amp_control, input_init=[signal[2], out_2])[-1]
    out_4 = intcode(amp_control, input_init=[signal[3], out_3])[-1]
    out_5 = intcode(amp_control, input_init=[signal[4], out_4])[-1]
    return out_5


def amplify_loop(amp_control, signal):
    amp_state = {
            1: amp_control,
            2: amp_control,
            3: amp_control,
            4: amp_control,
            5: amp_control,
    }
    pos_state = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    i = 1
    out_1, amp_state, \
    pos_state, stop_flag = intcode(amp_state[1],
                                   input_init=[signal[0], 0],
                                   loop=True, amp=1,
                                   amp_state_input=amp_state,
                                   pos_state_input=pos_state)
    out_2, amp_state, \
    pos_state, stop_flag = intcode(amp_state[2],
                                   input_init=[signal[1], out_1],
                                   loop=True, amp=2,
                                   amp_state_input=amp_state,
                                   pos_state_input=pos_state)
    out_3, amp_state, \
    pos_state, stop_flag = intcode(amp_state[3],
                                   input_init=[signal[2], out_2],
                                   loop=True, amp=3,
                                   amp_state_input=amp_state,
                                   pos_state_input=pos_state)
    out_4, amp_state, \
    pos_state, stop_flag = intcode(amp_state[4],
                                   input_init=[signal[3], out_3],
                                   loop=True, amp=4,
                                   amp_state_input=amp_state,
                                   pos_state_input=pos_state)
    out_5, amp_state, \
    pos_state, stop_flag = intcode(amp_state[5],
                                   input_init=[signal[4], out_4],
                                   loop=True, amp=5,
                                   amp_state_input=amp_state,
                                   pos_state_input=pos_state)
    while not stop_flag:
        i += 1
        out_1, amp_state, \
        pos_state, stop_flag = intcode(amp_state[1],
                                       input_init=[out_5],
                                       loop=True, amp=1,
                                       amp_state_input=amp_state,
                                       pos_state_input=pos_state)
        out_2, amp_state, \
        pos_state, stop_flag = intcode(amp_state[2],
                                       input_init=[out_1],
                                       loop=True, amp=2,
                                       amp_state_input=amp_state,
                                       pos_state_input=pos_state)
        out_3, amp_state, \
        pos_state, stop_flag = intcode(amp_state[3],
                                       input_init=[out_2],
                                       loop=True, amp=3,
                                       amp_state_input=amp_state,
                                       pos_state_input=pos_state)
        out_4, amp_state, \
        pos_state, stop_flag = intcode(amp_state[4],
                                       input_init=[out_3],
                                       loop=True, amp=4,
                                       amp_state_input=amp_state,
                                       pos_state_input=pos_state)
        out_5, amp_state, \
        pos_state, stop_flag = intcode(amp_state[5],
                                       input_init=[out_4],
                                       loop=True, amp=5,
                                       amp_state_input=amp_state,
                                       pos_state_input=pos_state)
    return out_5


def max_output(amp_control, loop=False):
    if loop:
        signals = [i for i in permutations([5, 6, 7, 8, 9])]
    else:
        signals = [i for i in permutations([0, 1, 2, 3, 4])]
    outputs = []
    for signal in signals:
        if loop:
            outputs.append(amplify_loop(amp_control, signal))
        else:
            outputs.append(amplify(amp_control, signal))
    highest_signal = max(outputs)
    print(f'Max phase setting: {signals[outputs.index(highest_signal)]}')
    print(f'Highest signal: {highest_signal}')
    return highest_signal


if __name__ == '__main__':
    with open('input.csv', 'r') as f:
        reader = csv.reader(f)
        amp_input = list(reader)
    
    amp_input = [int(i) for i in amp_input[0]]
    
    print('--- Without feedback loop ---')
    max_output(amp_input)
        # Max phase setting: (1, 4, 2, 0, 3)
        # Highest signal: 272368

    print('--- With feedback loop ---')
    max_output(amp_input, loop=True)
        # Max phase setting: (9, 6, 5, 8, 7)
        # Highest signal: 19741286
