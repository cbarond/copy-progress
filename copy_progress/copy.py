"""
A very minimal `cp` clone that displays a progress bar.
"""
import os
import shutil
import sys
import time

from rich.progress import Progress, TransferSpeedColumn, FileSizeColumn, TotalFileSizeColumn

def setup():
    progress_bar = Progress(
        *Progress.get_default_columns(),
        TransferSpeedColumn(),
        FileSizeColumn(),
        TotalFileSizeColumn()
    )
    return progress_bar

def copy_dir(progress):
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

def copy_file(progress):
    with progress as progress:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        desc = os.path.basename(arg1)
        with progress.open(arg1, "rb", description=desc) as src:
            with open(arg2, "wb") as dst:
                shutil.copyfileobj(src, dst)
    
def main():
    progress_bar = setup()
    if len(sys.argv) == 3:
        if os.path.isdir(sys.argv[1]):
            copy_dir(progress_bar)
        if os.path.isfile(sys.argv[1]):
            copy_file(progress_bar)
    else:
        print("Copy a file with a progress bar.")
        print("Usage:\n\tcopy-progress SRC DST")

if __name__ == "__main__":
    main()
