from pynput import keyboard
import time, csv, sys

prior = ''
prior_time = -1
t0 = time.time()
g = dict()
final_res = dict()
data_file_name = "data.csv"
name = sys.argv[1]

def find_avg(g):
    for k, v in g.items():
        g[k] = sum(v)/len(v)
    return g

def writeCsv(g):
    global data_file_name, name
    with open(data_file_name, 'a', newline='') as file:
        w = csv.writer(file)
        ls = []
        for key, value in g.items():
            ls.append(value)
        transpose = list(map(list, zip(*ls)))
        print(transpose)
        for e in transpose:
            w.writerow(e + [name])

def on_press(key):
    global prior, t0, mode, prior_time, final_res
    try:
        if len(prior) == 0:
            g.clear()
            recorded = time.time() - t0
            prior_time = recorded
        else:
            recorded = time.time() - t0
            if (prior, key.char) not in g:
                g[(prior, key.char)] = [recorded - prior_time]
            else:
                g[(prior, key.char)].append(recorded - prior_time)
            prior_time = recorded
        prior = key.char
    except AttributeError:
        if key == keyboard.Key.space:
            recorded = time.time() - t0
            if (prior, 'space') not in g:
                g[(prior, 'space')] = [recorded - prior_time]
            else:
                g[(prior, 'space')].append(recorded - prior_time)
            prior_time = recorded
            prior = 'space'
        elif(key == keyboard.Key.enter):
            prior = ''
            prior_time = -1
            if len(final_res) == 0:
                for key, value in find_avg(g).items():
                    final_res[key] = [value]
                print(f"\nFinal res = {final_res}")
            else:
                for key, value in find_avg(g).items():
                    final_res[key].append(value)
                print(f"\nFinal res = {final_res}")
            
        elif(key == keyboard.Key.esc):
            writeCsv(final_res)
            print("Exiting...")
            exit(0)

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
