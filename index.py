import base64
import bottle
import random
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_gpu=False)


@bottle.route('/orc', method='POST')
def login():
    filePath = './temp/' + (''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 5)))
    with open(filePath, 'wb') as f:
        f.write(base64.b64decode(bottle.request.body.read().decode("utf-8").split(',')[1]))
    ocrResult = ocr.ocr(filePath, cls=False)
    return {'result': [[line[1][0], float(line[1][1])] for line in ocrResult]}


bottle.run(host='0.0.0.0', port=8080)
