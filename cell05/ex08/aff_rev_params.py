import sys

if len(sys.argv) < 3:
    print("none")
else:
    print("\n".join(sys.argv[:0:-1]))