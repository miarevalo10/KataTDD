class Statistics:
    def values(self, string):
        if string == "":
            return [0, 0, 0]
        elif ',' in string:
            cadena = string.split(",")
            num1 = int(string[0])
            num2 = int(string[2])
            return [len(cadena), min(num1, num2), max(num1, num2)]
        else:
            num = int(string)
            return [1, num, num]
