import sys


def load(f):
    return f.read()


def build(f):
    loaded = load(f)
    loaded = loaded.replace('mov', '10')
    loaded = loaded.replace('eax', '01')
    loaded = loaded.replace(',', '')
    loaded = loaded.replace('\t', ' ')
    loaded = loaded.replace('0x', '')
    loaded = loaded.replace('int', '20')

    try:
        bf = open(sys.argv[1][:-4] + '_compiled.vmc', 'w')
    except:
        bf = open('hello_compiled.vmc', 'w')
    bf.write(loaded)



try:
    f = open(sys.argv[1], 'r')
except:
    f = open('hello.vm', 'r')
build(f)
f.close()
