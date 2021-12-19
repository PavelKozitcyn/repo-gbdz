import os
from collections import defaultdict


def folder_1():
    root_dir = 'my_project'
    all_files = defaultdict(int)
    for root, dirs, names_files in os.walk(root_dir):
        for file in names_files:
            size_threshold = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            all_files[size_threshold] += 1
    for size_threshold, nums_val in sorted(all_files.items()):
        print(f'{size_threshold}:{nums_val}')


folder_1()
