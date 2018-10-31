import numpy as np

def rgb2hex(rgb):
    """RGBを16進法表記に変換する"""
    r, g, b = rgb[0], rgb[1], rgb[2]
    _hex = '#{:02x}{:02x}{:02x}'.format(r, g ,b)
    return _hex

def hex2rgb(_hex):
    """16進数表記をRGBに変換する"""
    rgb = (int(_hex[1:3], 16), int(_hex[3:5], 16), int(_hex[5:7], 16))
    return rgb

def calc_dist_rgb_euclid(rgb1, rgb2):
    """2つのRGBを受け取りユークリッド距離を返す"""
    r1, g1, b1 = rgb1[0], rgb1[1], rgb1[2]
    r2, g2, b2 = rgb2[0], rgb2[1], rgb2[2]
    return np.sqrt((r2 - r1)**2 + (g2 - g1)**2 + (b2 - b1)**2)

