class Statistics:
    def values(self, string):
        if string == "":
            return [0, 0]
        elif ',' in string:
            cadena = list(map(int, string.split(",")))
            return [len(cadena), min(cadena)]
        else:
            return [1, int(string)]
