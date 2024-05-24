try:
    with open('test.txt') as f:
        print(f.readline())
        print(f.readline())
        # print(f.readline())
        # f.close()

except FileNotFoundError:
    print('Couldn\'t open the file!! file doesn\'t exist')