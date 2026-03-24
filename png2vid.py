from PIL import Image 
import numpy as np

def bmp2vid(bmp_path, vid_path):
    img = Image.open(bmp_path).convert("RGB")
    arr = np.array(img).flatten()
    
    size = int.from_bytes(arr[:4].tobytes(), byteorder='big')
    
    with open(vid_path, "wb") as f:
        f.write(arr[4:4 + size].tobytes())
    print("Ready!")

bmp2vid("output.png", "recovered.mp4")