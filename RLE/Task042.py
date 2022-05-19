# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах
from RLE.RLE import *
import pickle

with open('../file_text.txt') as f:
    file = f.read()
wee = rle(file_to_compress=file)
wee1 = wee.to_compress()
y = list(wee1)

with open('../file_text_b.bin', 'wb') as f:
    pickle.dump(y, f)

with open('../file_text_b.bin', 'rb') as f:
    bs = pickle.load(f)
wiz = rle(compressed_file=bs)
wiz1 = wiz.compressed()
print(wiz1)
