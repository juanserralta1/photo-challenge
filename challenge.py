import cv2
import numpy as np
import sys
from pprint import pprint

WHITE = [255,255,255]
BLACK = [0,0,0]

def get_matches_left(to_match, blocks):
    to_match_pxs = get_px_from_corners(to_match)
    color_blocks = blocks[get_pixel_key(to_match_pxs[2])]
    
    matches = []
    for block in color_blocks:
        block_pxs = get_px_from_corners(block)
        if (px_match(to_match_pxs[2],block_pxs[0]) and px_match(to_match_pxs[3],block_pxs[1])):
            matches.append(block)
    return matches



def get_px_from_corners(block):
    left_upper = block[0,0]
    left_lower = block[47,0]
    right_upper = block[0,47]
    right_lower = block[47,47]
    return [left_upper, left_lower, right_upper, right_lower]

def px_match(px_1, px_2):
    return get_pixel_key(px_1) == get_pixel_key(px_2)

def is_black_or_white(px):
    return get_pixel_key(px) in [get_pixel_key(WHITE), get_pixel_key(BLACK)]


def get_pixel_key(px):
    return "{}_{}_{}".format(px[0],px[1],px[2])

img = cv2.imread("challenge.png")
blocks = {}

for i in range(0,20):
    for j in range(0,20):
        x_min = 50 * i + 1
        x_max = 50 * (i + 1) - 1
        y_min = 50 * j + 1
        y_max = 50 * (j + 1) - 1
        sub = img[x_min:x_max,y_min:y_max]
        px = sub[0,0]

        px_key = get_pixel_key(px)

        if (px_key not in blocks):
            blocks[px_key] = []

        blocks[px_key].append(sub)
        


blacks = blocks[get_pixel_key(BLACK)]
lu_corner = None

# ya se que la esquina superior izquierda es negra
for black in blacks:
    cv2.imwrite("black_{}.png".format(i), black)
    pxs = get_px_from_corners(black)
    
    if (is_black_or_white(pxs[1]) and is_black_or_white(pxs[2])):
        lu_corner = black


hola = get_matches_left(lu_corner, blocks)

cv2.imwrite("lu_corner.png", lu_corner)
pprint(hola)
for k in range(0,4):
    cv2.imwrite("hola_{}.png".format(k), hola[k]) 

# print(len(hola))

#init output
output_image = np.zeros([1000,1000,3],dtype=np.uint8)
output_image.fill(255)



