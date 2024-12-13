import os
import time
# print(os.getcwd())
# print(os.walk('.'))

for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(r'D:\AyzekMendes\Pyton\taks1\module_7_5')
        filetime = os.path.getmtime('.')
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize('.')
        parent_dir =  os.path.dirname

print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

#Вывод: Обнаружен файл: module_7_5.py, Путь: D:\AyzekMendes\Pyton\taks1\module_7_5, Размер: 0 байт,
# Время изменения: 13.12.2024 23:18, Родительская директория: <function dirname at 0x0000024FC4EC3CE0>