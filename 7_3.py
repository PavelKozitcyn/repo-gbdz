from os import path, walk, listdir
import shutil

project_name = 'my_project'
try:
    for root, directories, names_files in walk(project_name):
        if 'templates' in directories and root != project_name:
            for entrance in listdir(path.join(root, 'teplates')):
                shutil.copytree(path.join(root, 'templates', entrance),
                                path.join(project_name, 'templates', basename(root)))

except FileExistsError:
    print('Файлы уже существуют')
