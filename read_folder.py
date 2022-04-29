import os
from pathlib import Path
files = os.listdir("/Users/arifin/work/Robosub Dataset/task") #Location of the your file


with open ('test1.txt', 'w') as f: #Create a .txt file and paste the location of it
    for x in files:
        image = Path(x).stem
        f.writelines(image +", ")



