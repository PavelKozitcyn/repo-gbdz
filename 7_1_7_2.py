import os


def create_folder(workspace, folder):
    path = os.path.join(workspace, folder)
    if not os.path.exists(path):
        os.makedirs(path)
        print(f'создаем папку с путём {path}')
    else:
        print(f'папка существуе {path}')


create_folder('my_project', 'settings')
create_folder('my_project', 'mainapp')
create_folder('my_project', 'adminapp')
create_folder('my_project', 'authapp')
