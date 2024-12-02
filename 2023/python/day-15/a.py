import sys

def main():
    data = sys.stdin.read()
    s = 0
    for x in data.split(","):
        s+=chash(x)
    print(s)

def chash(text):
    val = 0
    for x in text:
        val+=ord(x)
        val*=17
        val = val % 256
    return val

main()