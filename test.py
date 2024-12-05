import cv2
import time
import math

FPS = 30
FORMAT = 'jpeg'  # jpeg or webp
QUALITY = 80  # 0-100

image = cv2.imread('lenna.png')
try:
    quality_param = getattr(cv2, f'IMWRITE_{FORMAT.upper()}_QUALITY')
except AttributeError:
    raise ValueError(f'Format {FORMAT} not supported')
encode_param = [quality_param, QUALITY]

next_time = time.time() + 1 / FPS
while True:
    start_time = time.time_ns()
    cv2.imencode(f'.{FORMAT}', image, encode_param)
    print((time.time_ns() - start_time) / 1e6)  # unit: ms

    diff = next_time - time.time()
    if diff > 0:
        time.sleep(diff)
        next_time += 1 / FPS
    else:
        raise ValueError('Timeout')
