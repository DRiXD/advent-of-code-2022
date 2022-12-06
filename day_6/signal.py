file = open('day_6/input.txt', 'r')
input_signal = file.readlines()
signal_string = ''.join(input_signal)

stopper = True
n=0
while(stopper):
    consumed_chars = []
    consumed_chars.append(signal_string[n])

    for i in range(1,14):

        current_char = signal_string[n+i]
        print(f"I: {i}, Consumed: {consumed_chars}, current: {current_char}")
        if current_char in consumed_chars:
            break
        else:
            consumed_chars.append(current_char)

    if len(consumed_chars) == 14:
        n = n + len(consumed_chars)
        print(f"We found the signal! It starts at index: {n}")
        stopper = False
    else:
        n = n +1
