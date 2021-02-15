import keyboard, time
first = ''
t0 = time.time()
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if len(first) != 0:
            second = keyboard.read_key()
            print(f'key pressed: {first} -> {second} at time = {time.time() - t0}')
        else:
            second = keyboard.read_key()
            print(f'first key: {second} at time = {time.time() - t0}')
        first = second
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
    except:
        break 