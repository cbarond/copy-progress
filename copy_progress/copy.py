"""
A very minimal `cp` clone that displays a progress bar.
"""
import os
import shutil
import sys
import time

from rich.progress import Progress, TransferSpeedColumn, FileSizeColumn, TotalFileSizeColumn

progress = Progress(
    *Progress.get_default_columns(),
    TransferSpeedColumn(),
    FileSizeColumn(),
    TotalFileSizeColumn()
)

def copy_dir():
    files = os.listdir(sys.argv[1])
    print(files)
    with progress as progress:
        for item in files:
            arg1 = os.path.join(sys.argv[1], item)
            arg2 = os.path.join(sys.argv[2], item)
            desc = os.path.basename(arg1)
            with progress.open(arg1, "rb", description=desc) as src:
                with open(arg2, "wb") as dst:
                    shutil.copyfileobj(src, dst)

def copy_file():
    with progress as progress:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        desc = os.path.basename(arg1)
        with progress.open(arg1, "rb", description=desc) as src:
            with open(arg2, "wb") as dst:
                shutil.copyfileobj(src, dst)
    
def main():
    if len(sys.argv) == 3:
        if os.path.isdir(sys.argv[1]):
            copy_dir()
        if os.path.isfile(sys.argv[1]):
            copy_file()
    else:
        print("Copy a file with a progress bar.")
        print("Usage:\n\tpython cp_progress.py SRC DST")

if __name__ == "__main__":
    main()

""" 
if __name__ == "__main__":
    if len(sys.argv) == 3:
        with progress as progress:
            desc = os.path.basename(sys.argv[1])
            shutil.copytree(sys.argv[1], sys.argv[2], dirs_exist_ok=True)
    else:
        print("Copy a file with a progress bar.")
        print("Usage:\n\tpython cp_progress.py SRC DST")
 """

""" if __name__ == "__main__":
    if len(sys.argv) == 3:
        files = os.listdir(sys.argv[1])
        print(files)
        for item in files:
            arg1 = os.path.join(sys.argv[1], item)
            arg2 = os.path.join(sys.argv[2], item)
            with progress as progress:
                desc = os.path.basename(arg1)
                print(f'{arg1}\t{arg2}')
                #with progress.open(arg1, "rb", description=desc) as src:
                #    with open(arg2, "wb") as dst:
    else:
        print("Copy a file with a progress bar.")
        print("Usage:\n\tpython cp_progress.py SRC DST") """
