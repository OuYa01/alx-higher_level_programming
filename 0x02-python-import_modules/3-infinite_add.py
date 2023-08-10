#!/usr/bin/python3
if __name__ == "__main__":
    import sys
i = 1
add = 0
argv = sys.argv
argc = len(argv)
if (argc == 1):
    print("0")
while i < argc:
    add += int(argv[i])
    i += 1
print("{}".format(add))
