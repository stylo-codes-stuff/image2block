import os
import tempfile as tp   
import shutil
from PIL import Image
'''these functions are solely for creating the datapacks and sending them'''
fp = tp.TemporaryFile()

'''creates the datapack to be sent to the client'''
def create_pack(image_name=""):#https://stackoverflow.com/questions/18550127/how-to-do-virtual-file-processing
    with tp.TemporaryDirectory() as f:
        shutil.copy(f.name, 'new-name')
        print('created temporary directory', f)
create_pack()
print(fp)