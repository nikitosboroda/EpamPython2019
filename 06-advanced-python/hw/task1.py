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


class PrintableFolder:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __str__(self):
        count = self.name.count(os.path.sep) + 1
        result = 'V ' + os.path.basename(self.name) + '\n'
        for dir, _, files in self.content:
            depth_dir = len(dir.split(os.sep))
            result += (depth_dir - count - 1) * '|\t' + '|-> V ' + os.path.basename(dir) + '\n'
            for file in files:
                result += (depth_dir - count) * '|\t' + str(PrintableFile(file)) + '\n'
        return result

    def __contains__(self, file):
        return (True for _, _, files in self.content for f in files if f == file.name)


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '|-> ' + self.name


if __name__ == '__main__':
    contents = []
    for dir, dirname, files in os.walk('.'):
        # print(dir, dirname, files)
        contents.append((dir, dirname, files))

    folder1 = PrintableFolder('.', contents)
    print(folder1)
    file1 = PrintableFile('task1.py')
    print(file1 in folder1)
    assert (file1 in folder1) == 0
