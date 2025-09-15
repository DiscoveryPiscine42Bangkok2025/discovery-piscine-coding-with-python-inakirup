import sys

if len(sys.argv) != 2 or 'z' not in sys.argv[1]:
    print("none")
else:
    for char in sys.argv[1]:
        if char == 'z':
            print('z')