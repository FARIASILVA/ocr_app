import cv2
import numpy as np
import base64

def desenhar_resultados(img, resultados):
    for r in resultados:
        box = np.array(r['box']).astype(int)
        cv2.polylines(img, [box], isClosed=True, color=(0, 255, 0), thickness=2)
        cv2.putText(img, r['text'], tuple(box[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    return img

def encode_image_base64(img):
    _, buffer = cv2.imencode(".png", img)
    return base64.b64encode(buffer).decode("utf-8")

