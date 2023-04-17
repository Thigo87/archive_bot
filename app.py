import os
from pathlib import Path
import shutil
from tkinter.filedialog import askdirectory

p = askdirectory()
path = Path(p)
l=[]
for filename in path.glob('*'):
    if os.path.isfile(filename):
        name = filename.suffix[1:]
        l.append(name)
    elif os.path.isdir(filename):
        pass

l = set(l)

for i in l:
    os.mkdir(f"{p}/{i}")

for filename in path.glob('*'):
    if os.path.isfile(filename):
        name = filename.suffix[1:]
        shutil.move(filename, f"{p}/{name}")
    elif os.path.isdir(filename):
        pass