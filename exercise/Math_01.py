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
        #pass

    # Operator in index for roman number
    def _Operator(self): # Select index for numbers
        list = ["I", "V"]
        outdata=[]
        for x in range(int(self.test)): 
            outdata.append(list[0])
        Strend = "".join(outdata)
        return Strend

# Waiting for data
while True:
    data=input("Convert - decimal numerals to roman numerals / roman numerals to decimal numerals: \n")
    call = decimal(data)
    print(call._Operator())
    break
