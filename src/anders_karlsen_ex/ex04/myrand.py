# -*- coding: utf-8 -*-

__author__ = 'Anders Karlsen'
__email__ = 'anderska@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.last_r = seed
        self.current_r = 0

    def rand(self):
        a = 7**5
        m = 2**31-1
        self.current_r = (a * self.last_r) % m
        self.last_r = self.current_r
        return self.current_r


class ListRand:
    def __init__(self, input_list):
        self.input_list = input_list
        self.index = 0

    def rand(self):
        self.index += 1
        if self.index > len(self.input_list):
            raise RuntimeError("There are no more numbers in the list")
        else:
            return self.input_list[self.index-1]


if __name__ == "__main__":
    lr = ListRand([1, 2, 3])
    LCG = LCGRand(16)
    for _ in range(3):
        print(lr.rand())
        print(LCG.rand())
