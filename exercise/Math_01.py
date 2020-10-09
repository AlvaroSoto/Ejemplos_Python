# Convert data
# Alvaro Soto. 2020
# Cod. Math_01.py
# Min: 1 and I, Max: 3999 and MMMCMXCIX

class roman(object):
    pass
    def __init__(args):
        pass
    def function(args):
        pass

class decimal(roman):

    def __init__(self, data):
        #self.count = len(data)
        self.test = int(data)
        self.list = ("I", "V", "X", "L", "C", "D", "M")
        self.a=[]
        #pass
    # Operator in index for roman number
    def _Operator(self): # Select index for numbers
        for x in range(int(self.test)): 
            self.a.append(self.list[0])
        Strend = "".join(self.a)
        return Strend

# Waiting for data
while True:
    data=input("Convert - decimal numerals to roman numerals / roman numerals to decimal numerals: \n")
    try:
        if int(data) >= 1 and int(data) <= 3999:
            call = decimal(data)
            print(call._Operator())
    except :
        pass

    try:
        if True:
            call = decimal(data)
            print(call._Operator())
    except :
        pass

    break
