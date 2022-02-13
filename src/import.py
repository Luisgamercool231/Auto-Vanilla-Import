# script for importing Ettob's Vanilla icons into studio for you
import shutil
import os
from time import time
versions_path = os.environ["USERPROFILE"] + "\AppData\Local\Roblox\Versions"
icons = "ClassImages.png"
def add():
    start_time = time()
    if True:
        versions = os.listdir(versions_path)
        for version in versions:
           version_path = f'{versions_path}/{version}'
           file_type = os.path.splitext(version_path)
        if file_type != ".exe":
            textures_path = f'{version_path}/content/textures'
            shutil.copy(icons, textures_path)      # copies the icons into the textures path
            completion_time = time() - start_time
            completion_time = str(completion_time)
        print(f'successfully completed operation in {completion_time}')    
add()
