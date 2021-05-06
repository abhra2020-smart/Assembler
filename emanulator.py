import sys

mem = {'01': 0x00}


def load(f):
    return f.read()


def run(f):
    loaded = load(f)
    loaded = loaded.split(' ')
    for i in range(0, len(loaded)):
        instruction = loaded[i]

        if instruction == '10':
            mem[loaded[i + 1]] = loaded[i + 2]
            continue
        elif instruction == '20':
            if loaded[i + 1] == '80':
                if mem['01'] == '01':
                    continue


try:
    f = open(sys.argv[1], 'r')
except:
    f = open('hello_compiled.vmc', 'r')
run(f)
f.close()
