class Statistics:
    def values(self, string):
        if string == "":
            return [0, 0]
        elif ',' in string:
            cadena = string.split(",")
            return [len(cadena)]
        else:
            return [1, int(string)]
