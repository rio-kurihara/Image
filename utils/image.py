import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def save_img_draw_bbox(img, x1, x2, y1, y2, path_save):
    """imgとBBOXの座標を受け取り、描画して保存"""
    img2 = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
    cv2.imwrite(path_save, img2)

def get_concat_h(img1, img2) -> Image.Image:
    """画像を横に並べて1枚の画像にして返す"""
    if hasattr(img1, '__iter__'):
        #BGRからRGBへ変換
        img1_rgb = img1[:, :, ::-1].copy()
        img1 = Image.fromarray(np.uint8(img1_rgb))
    if hasattr(img2, '__iter__'):
        img2_rgb = img2[:, :, ::-1].copy()
        img2 = Image.fromarray(np.uint8(img2_rgb))

    dst = Image.new('RGB', (img1.width + img2.width, img1.height))
    dst.paste(img1, (0, 0))
    dst.paste(img2, (img1.width, 0))
    return dst

def draw_text(img, text, color, x, y, font_size=20) -> Image.Image:
    font = ImageFont.truetype("../VL-Gothic-Regular.ttf", font_size)
    """画像にテキストを書き込んで返す"""
    if hasattr(img, '__iter__'):
        #BGRからRGBへ変換
        img_rgb = img[:, :, ::-1].copy()
        img = Image.fromarray(np.uint8(img_rgb))
    draw = ImageDraw.Draw(img)
    draw.text((x, y), text, font=font, fill=color)
    return img

def crop_image_by_rate(img_path, _x1, _x2, _y1, _y2):
    img = cv2.imread(img_path)
    img_h = img.shape[0]
    img_w = img.shape[1]
    x1, x2, y1, y2 = round(_x1 * img_w),\
                     round(_x2 * img_w),\
                     round(_y1 * img_h),\
                     round(_y2 * img_h)

    # クロップ用の座標取得
    bbox_w, bbox_h = x2 - x1, y2 - y1
    dst = img[y1:y1+bbox_h, x1:x1+bbox_w]
    return dst

def crop_image_by_abs(img_path, x1, x2, y1, y2):
    img = cv2.imread(img_path)
    # クロップ用の座標取得
    bbox_w, bbox_h = x2 - x1, y2 - y1
    dst = img[y1:y1+bbox_h, x1:x1+bbox_w]
    return dst
