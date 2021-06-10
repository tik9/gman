from os import path
from pathlib import Path

home=str(Path.home())

with open(path.join(home,'ghtoken'),'r') as file_: 
    token=file_.read()
    # print(token)
