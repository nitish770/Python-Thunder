'''
    Probem Task : Returns the total number in ele
    Problem Link : https://edabit.com/challenge/xmwdk2qwyZEt7ph49
'''

def length(l: list):
    length_ = 0
    if len(l) == 0:
        return length_

    for i in l:
        if type(i) != list:
            length_ += 1
        else:
            length_ += length(i)

    return length_


if __name__ == '__main__':
    l = [1, [1, [1, ['a', 'b', 'c'], 2], 2], 2]
    print(length(l))
