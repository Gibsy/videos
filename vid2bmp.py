from PIL import Image 
import numpy as np
import math

def vid2bmp(vid_path, bmp_path):
    with open(vid_path, "rb") as f:
        data = f.read()
        
    size = len(data)
    
    size_bytes = size.to_bytes(4, byteorder='big')
    data = size_bytes + data
    
    pixel_needed = math.ceil(len(data) / 3)
    side = math.ceil(math.sqrt(pixel_needed))
    
    padded = data + b'\x00' * (side * side * 3 - len(data))
    arr = np.frombuffer(padded, dtype=np.uint8).reshape((side, side, 3))
    Image.fromarray(arr, 'RGB').save(bmp_path, format='BMP')
    print(f"Ready! {size} bytes in {side}x{side} pixels")
    
vid2bmp("init.mp4", "output.bmp")