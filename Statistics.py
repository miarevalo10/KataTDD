class Statistics:
    def values(self, string):
        if string == "":
            return [0, 0, 0]
        elif ',' in string:
            cadena = list(map(int, string.split(",")))
            return [len(cadena), min(cadena), max(cadena)]
        else:
            num = int(string)
            return [1, num, num]
