import string


class Caesar:
    def __init__(self, alpha_map=string.printable):
        self.alpha_map = alpha_map

    def encrypt(self, msg, key):
        shifted_alphabet = self.alpha_map[key:] + self.alpha_map[:key]
        table = str.maketrans(self.alpha_map, shifted_alphabet)
        return msg.translate(table)

    def decrypt(self, msg, key):
        key = -key
        shifted_alphabet = self.alpha_map[key:] + self.alpha_map[:key]
        table = str.maketrans(self.alpha_map, shifted_alphabet)
        return msg.translate(table)

    def crack(self, msg, alpha_map=None):
        alpha_map = self.alpha_map if not alpha_map else alpha_map
        res = {}
        for key in range(len(self.alpha_map)):
            shifted_alphabet = alpha_map[-key:] + alpha_map[:-key]
            table = str.maketrans(alpha_map, shifted_alphabet)
            res[key] = msg.translate(table)
        return res
