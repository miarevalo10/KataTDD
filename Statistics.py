class Statistics:
    def values(self, string):
        if string == "":
            return [0, 0]
        elif ',' in string:
            cadena = string.split(",")
            return [len(cadena), min(int(string[0]), int(string[2]))]
        else:
            return [1, int(string)]
