# Напишите программу, удаляющую из текста все слова содержащие "абв".
import re
lists = 'ываабв лповап абвцукв алоабвабв ываываыв'
lists1 = re.sub(r'\b\S*абв\S*\b', '', lists)
print(lists1)
