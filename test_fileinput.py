import fileinput

# read from /dev/device and print to console
for line in fileinput.input('/dev/device'):
    print(line)