"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной, например так:

> print(folder1)

V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1

А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True

"""
import os
import os.path


class PrintableFolder:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __str__(self):
        path = ''
        for i, key in enumerate(self.content.keys()):
            if key != self.name:
                path += f"{'|   ' * (i - 1)}|-> V {key}\n"
            else:
                path += f'V {key} \n'

        dir_count = len(self.content.keys()) - 1
        list_of_values = list(self.content.values())
        for value in reversed(list_of_values):
            for i in range(len(value)):
                path += f"{'|   ' * dir_count}|-> {value[i]}\n"
            dir_count -= 1
        return path

    def __contains__(self, file):
        all_folders = list(self.content.values())
        for curr_folder in range(len(all_folders)):
            if file in all_folders[curr_folder]:
                return True
        return False


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '|-> ' + self.name