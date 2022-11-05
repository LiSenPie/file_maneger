import os
import shutil

print("Текущая деректория:", os.getcwd()) # вывести текущую директорию

def where_r_u():
    t = str(os.getcwd())
    return(f'Текущая деректория: {t}')

def change_directory(p):
    os.chdir(p)
    
def createfol(p): # создать пустой каталог (папку)
    os.mkdir(p)
    
def filecreate(p): # создать файл
    text_file = open(p, "w")
    
def filedelete(p): # удалить файл
    p = str(p)
    os.remove(p)
    
def rename(p, p1): # переименовать папку или файл
    os.rename(p, p1)
    
def moveto(p, p1): # перемещение в другую директорию
    shutil.move(p, p1) #g1 должна быть вида "folder/renamed-text.txt"
    
def copy(p, p1): # копирование содержимого папки в другую папку
    shutil.copy2(p, p1) #'/src/dir/file.ext', '/dst/dir/newname.ext' пример ввода
    
def writefile(p, p1): # Запись информации в текстовый файл
    f = open(p, 'w')
    f.write(p1)
    f.close()
    
def readfile(p): # Чтение информации из текстового файла
    f = open(p, 'r')
    buf = f.read()
    print(f'Содержимое файла {p}: \n {buf}')
    f.close

close_fol = ''
k1 = input('Введите "1", если хотите ограничить перемещение по директориям ')
if k1 == '1':
    close_fol = input('Введите имя папки. \n ВНИМАНИЕ! \n Вы не сможете уйти выше данной директории, но можете свободно перемещаться по '
'уже существующим папкам или по тем, которые сами создатите в данной директории. \n Введите "0", чтобы отменить данное действие ')
    if close_fol == '0':
        close_fol = ''
    else:
        change_directory(close_fol)
else:
    None

flag = True

mass = ['createfolder', 'deletefolder', 'change', 'createfile', 'check', 'deletefile', 'rename', 'moveto', 'copyto', 'stop', 'writefile', 'readfile', 'where', 'tostart']

while flag == True:
    print('\nВведите команду: ')
    k = input()
    
    if k not in mass: # проверка существования команды
        print('Такой команды не существет. Попробуйте еще раз')
    
    if k =='createfolder': # создание папки
        print('Введите название новой папки: ')
        f = input() # имя новой папки
        if close_fol != '' and close_fol in f:
            try:
                createfol(f)
                print(f'Папка {f} успешно создана!')
            except:
                print('ERROR')
        else:
            if close_fol != '':
                f = f'{close_fol}\{f}'
            try:
                createfol(f) # функция создания папки
                print(f'Папка {f} успешно создана!')
            except:
                print('Ой! Что-то пошло не так. Попробуйте еще раз')
            
    if k == 'deletefolder': # удаление выбранной папки по имени или пути
        print('Введите название папки, которую хотите удалить: ')
        f3 = input() # имя удаляемой папки
        if (close_fol != '' and close_fol in f3) or (close_fol != '' and f3 in os.listdir()):
            try:
                os.rmdir(f3)
                print(f'Папка {f3} успешно удалена!')
            except:
                print('ERROR')
        else:
            if close_fol != '':
                f3 = f'{close_fol}\{f3}'
            f3 = str(f3)
            try:
                os.rmdir(f3) # функция удаления папки
                print(f'Папка {f3} успешно удалена!')
            except:
                print(f'Папки с именем {f3} не существует в данной директории, попробуйте еще раз')
                continue
            
    if k == 'change': # изменение рабочей директории
        print('Введите директорию, в которую хотите переместиться: ')
        f1 = input() # имя директории, в которую хотим переместиться
        if f1 != '':
            try:
                change_directory(f1)
                #print(where_r_u())
                if close_fol != '' and close_fol not in where_r_u():
                    print('Вы пытаетесь выйти за пределы ограниченной директории! Вы вернулись в начало!')
                    change_directory(close_fol)
                    print(where_r_u())
                else:
                    print(where_r_u())
            except:
                print('Такой папки не существует в данной директории')
        else:
            print('Вы не ввели имя директории!')
            
    if k == 'tostart':
        if close_fol != '':
            change_directory(close_fol)
            where_r_u()
        else:
            print('Вы не выбрали ограничительную директорию!')
            where_r_u()
            
    if k == 'createfile': # создание файла
        print('Введите название файла, который хотите создать (с расширением): ')
        f2 = input() # имя создаваемого файла
        if close_fol != '' and close_fol in f2:
            try:
                filecreate(f2)
                print(f'Файл {f2} успешно создан!')
            except:
                print('ERROR')
        else:
            if close_fol != '':
                f2 = f'{close_fol}\{f2}'
            try:
                filecreate(f2)
                print(f'Файл {f2} успешно создан!')
            except:
                print('Ой! Что-то пошло не так. Попробуйте еще раз')
            
    if k == 'check': # вывод всех папок и фалйов в директории
        print('Все папки и файлы: ', os.listdir())
                
    if k == 'deletefile': # удаление файла по имени
        print('Введите название файла, который хотите удалить: ')
        f4 = input() # имя удаляемого файла
        f4 = str(f4)
        if (close_fol != '' and close_fol in f4) or (close_fol != '' and f4 in os.listdir()):
            try:
                filedelete(f4)
                print(f'Файл {f4} успешно удален!')
            except:
                print('ERROR')
        else:
            if close_fol != '':
                f4 = f'{close_fol}\{f4}'
            try:
                filedelete(f4)
                print(f'Файл {f4} успешно удален!')
            except:
                print('Файла с таким именем не существует. Попробуйте еще раз')
            
    if k == 'rename': # переименование папки или файла
        print('Введите имя файла, которое хотите изменить: ')
        f5 = input() # имя файла или папки, которую надо переименовать
        print('Введите новое имя файла: ')
        f6 = input() # новое имя файла или папки
        if (close_fol != '' and close_fol in f5) or (close_fol != '' and f5 in os.listdir()):
            try:
                rename(f5, f6)
                print(f'Теперь файл {f5} называется {f6}')
            except:
                print('ERROR')
        else:
            if close_fol != '':
                f5 = f'{close_fol}\{f5}'
            try:
                if f5 in os.listdir():
                    rename(f5, f6)
                    print(f'Теперь файл {f5} называется {f6}')
                else:
                    print('Такого файла не существует')
            except:
                print('Ой! Что-то пошло не так. Попробуйте еще раз')
            
    if k == 'moveto': # перемещение файла или папки в новую директорию
        print('Введите имя файла, который хотите переместить: ')
        f7 = input() # имя перемещаемого файла или папки
        print('Введите имя директории, в которую хотите переместить файл: ')
        f8 = input() # имя директории, в которую перемещаем
        if (close_fol != '' and close_fol in f7 and close_fol in f8) or (close_fol != '' and f7 in os.listdir() and close_fol in f8):
            try:
                moveto(f7, f8)
                print(f'Теперь {f7} находится в {f8}')
            except:
                print('ERROR')
        else:
            if close_fol != '':
                f7_ = f'{close_fol}\{f7}'
            try:
                if close_fol in f8:
                    moveto(f7_, f8)
                    print(f'Теперь {f7} находится в {f8}')
                else:
                    print('Выход за ограничения директории')
            except:
                print('Ой! Что-то пошло не так. Попробуйте еще раз. Возможно папки с таким именем не существует')
            
    if k == 'copyto': # копирование файла
        print('Введите имя файла, который хотите копировать: ')
        f9 = input() # название файла
        print('Введите имя директории, куда хотите копировать: ')
        f10 = input() # директория, куда копировать
        if (close_fol != '' and close_fol in f9 and close_fol in f10) or (close_fol != '' and f9 in os.listdir() and close_fol in f10):
            try:
                copy(f9, f10)
                print(f'Объект {f9} успешно скопирован в папку {f10}')
            except:
                print('ERROR')
        if close_fol != '':
                f9_ = f'{close_fol}\{f9}'
        try:
            if close_fol in f10:
                copy(f9_, f10)
                print(f'Объект {f9} успешно скопирован в папку {f10}')
            else:
                print('Выход за ограничения директории')
        except:
            print('Ой! Что-то пошло не так. Попробуйте еще раз. Возможно папки с таким именем не существует')
        
    if k == 'writefile': # запись в файл
        print('Введите имя текстового файла, который хотите изменить: ')
        f11 = input() # имя файла, в который вносятся изменения
        print('Введите текст, который хотите записать: ')
        s = input() # строка, которую вы хотите записать в файл
        s = str(s)
        if (close_fol != '' and close_fol in f11) or (close_fol != '' and f11 in os.listdir()):
            try:
                writefile(f11, s)
                print(f'Запись успешно внесена в файл {f11}')
            except:
                print('ERROR')  
        if close_fol != '':
                f11 = f'{close_fol}\{f11}'
        try:
            if f11 in os.listdir():
                writefile(f11, s)
                print(f'Запись успешно внесена в файл {f11}')
            else:
                print('Файла с таким именем не существует!')
        except:
            print('Ой! Что-то пошло не так. Попробуйте еще раз')
        
    if k == 'readfile': # чтение из файла
        print('Введите имя текстового файла, который хотите прочитать: ')
        f12 = input() # имя файла, из которого хотите считать содержимое
        if (close_fol != '' and close_fol in f12) or (close_fol != '' and f12 in os.listdir()):
            try:
               readfile(f12)
            except:
                print('ERROR')
        else: 
            if close_fol != '':
                    f12 = f'{close_fol}\{f12}'
            try:
                readfile(f12)
            except:
                print('Файла с таким именем не существует. Попробуйте еще раз')
        
    if k == 'where':
        print(where_r_u())
        
    if k == 'stop': # команда для остановки программы
        flag = False