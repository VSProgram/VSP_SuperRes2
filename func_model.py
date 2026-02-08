from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer
import numpy as np
from PIL import Image
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'

if device == 'cpu':
    half = False
if device == 'cuda':
    half = True

model = RRDBNet(
    num_in_ch=3,
    num_out_ch=3,
    num_feat=64,
    num_block=23,
    num_grow_ch=32,
    scale=4
)


upsampler = RealESRGANer(
    scale=4,
    model_path='weights/RealESRGAN_x4plus.pth',
    model=model,
    tile=0,
    tile_pad=10,
    pre_pad=0,
    half=half  
)

def sr_func(image):
    img = np.array(image)
    output, _ = upsampler.enhance(img, outscale=4)
    return Image.fromarray(output)
