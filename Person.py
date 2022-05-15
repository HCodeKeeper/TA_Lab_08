import math


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def generate_hashcode(self):
        M = 0
        d = 128
        to_hash = list(self.name + self.surname)
        c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z']
        for i in range(len(to_hash)):
            for j in range(len(c)):
                if to_hash[i] == c[j] or to_hash[i] == c[j].upper():
                    M += (j + 1 << i) * (i + 1 << j)
                    M -= ((j << i) ^ (i << j))
        C = []
        r = 40 + int(d / 4)
        i = 0
        L = 64
        K = 32
        keylen = K.bit_length()
        K = K << (64 - keylen)
        while i < L + 1:
            M = self.PAR(M, d, K, r, i, C, L, keylen)
            i += 1
        return M

    def PAR(self, M, d, K, r, i, C, L, keylen):
        Q = [0x7311c2812425cfa0, 0x6432286434aac8e7, 0xb60450e9ef68b7c1, 0xe8fb23908d9f06f1,
             0xdd2e76cba691e5bf, 0x0cd0d63b2c30bc41, 0x1f8ccf6823058f8a, 0x54e5ed5b88e3775d,
             0x4ad12aae0a6d6031, 0x3e7f16bb88222e0d, 0x8af8671d3fb50c2c, 0x995ad1178bd25c31,
             0xc878c1dd04c4b633, 0x3b72066c7a1552ac, 0x0d6f3522631effcb]
        p = 0
        while M.bit_length() % 384 != 0:
            M = M << 1
            p += 1
        j = max(1, math.ceil(M.bit_length() / 384))
        z = 0
        if j == 1:
            z = 1

        V = r | L | z | L | p | K.bit_length() | keylen | d
        U = i * 2 ** 56 + i
        C.append(Q[j] | K | U | V)

        return M
