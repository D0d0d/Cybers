import string 

class Affine:
    
    def __init__(self):
        rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        alpha = rus+rus.upper()+string.printable
        self.alpha = {}
        for i,j in enumerate(list(alpha)):
            self.alpha[i]=j
        self.m = len(alpha)
    
    def _mmi(self,a):
        for n in range(self.m):
            if (a * n) % self.m == 1:
                return n

    def set_ab(self,a,b):
        self.mmi = self._mmi(a)
        if not self.mmi:
            return 1
        else:
            self.a = a
            self.b = b
            return 0
            
        
    def encrypt(self, msg):
        msg = list(msg)
        for i in range(len(msg)):
            key = list(self.alpha.keys())[list(self.alpha.values()).index(msg[i])]
            msg[i] = self.alpha[(self.a*key+self.b)%self.m]
        return "".join(msg)
        
    def decrypt(self,msg):
        msg = list(msg)

        for i in range(len(msg)):
            key = list(self.alpha.keys())[list(self.alpha.values()).index(msg[i])]
            msg[i] = self.alpha[(self.mmi * (key - self.b)) % self.m]
        return "".join(msg)

affine = Affine()

while affine.set_ab(int(input("Введите a: ")),int(input("Введите b: ")))!=0:
    print("Некорректные ключи, попробуйте еще раз")
msg = input("""
1. Шифровать 
2. Дешифровать
Выберите вариант ответа 1-2: """)
match msg:
    case "1": print(affine.encrypt(input("Введите сообщение для шифрования: ")))
    case "2": print(affine.decrypt(input("Введите сообщение для расшифрования: ")))