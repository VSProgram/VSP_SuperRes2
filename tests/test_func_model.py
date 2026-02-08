from PIL import Image
from func_model import sr_func

def test_returns_pil_image():
    img = Image.new('RGB', (32, 32), color='blue')
    result = sr_func(img)
    assert isinstance(result, Image.Image)

def test_output_size_4x():
    img = Image.new('RGB', (50, 30), color='green')
    result = sr_func(img)
    assert result.size == (200, 120)