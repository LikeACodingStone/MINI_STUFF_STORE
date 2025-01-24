from PIL import Image
import io

def compress_image(image_file, max_size=(800, 800), quality=85):
    """
    压缩图片
    :param image_file: 原始图片文件
    :param max_size: 最大尺寸
    :param quality: 压缩质量（1-100）
    :return: 压缩后的图片数据
    """
    img = Image.open(image_file)
    
    # 保持宽高比例缩放
    img.thumbnail(max_size, Image.LANCZOS)
    
    # 转换为RGB模式（如果是RGBA）
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
    
    # 压缩
    output = io.BytesIO()
    img.save(output, format='JPEG', quality=quality, optimize=True)
    output.seek(0)
    
    return output 