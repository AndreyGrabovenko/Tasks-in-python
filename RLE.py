
class rle():
    def __init__(self, compressed_file = None, file_to_compress = None):
        self._compressed_file = compressed_file
        self._file_to_compress = file_to_compress
        self.__count = 1
        self.__temp = []
    def to_compress(self):
        self.p = len(self._file_to_compress)
        for i in range(self.p-1):
            if i <= self.p:
                if self._file_to_compress[i] == self._file_to_compress[i+1]:
                    self.__count +=1
                else:
                    self.__temp.append(self.__count)
                    self.__temp.append(self._file_to_compress[i])
                    self.__count = 1
        self.__temp.append(self.__count)
        self.__temp.append(self._file_to_compress[i])
        return self.__temp
    def compressed(self):
        self.__list = ''
        self._p = len(self._compressed_file)
        for i in range(0, self._p, 2):
            for j in range(self._compressed_file[i]):
                self.__temp.append(self._compressed_file[i+1])
        self.__list = ''.join(self.__temp)
        return self.__list
