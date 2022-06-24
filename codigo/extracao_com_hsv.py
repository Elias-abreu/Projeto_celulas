from qt_core import *

def contarBrancas():
    # Converter para o espaço de cor definido
    hsv = cv2.cvtColor(img, cv2.COLOR_LBGR2LAB)

    # Pegar a nargura e altura da imagem e dividir por 4, objetivo não ter imagens-IF grandes
    largura = int(img.shape[0] / 4)
    altura = int(img.shape[1] / 4)
    # Realizar a suavsão da imagem
    blur = cv2.GaussianBlur(hsv, (5, 5), 0)

    # Configuração das cores a serem cortadas
    # valor_minimo = np.array([122,148,138])
    # valor_maximo = np.array([156,182,172])

    valor_minimo = np.array([130, 146, 20])
    valor_maximo = np.array([255, 255, 180])

    mask = cv2.inRange(blur, valor_minimo, valor_maximo)

    # Remover rupidos de fazer a dinação para juntas as partes
    kernal = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal, iterations=2)
    final = cv2.dilate(opening, kernal, iterations=3)

    # Pegar todos os contornos
    objetos, lx = cv2.findContours(final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # percorrer todos os objetos encontrados
    for i in objetos:
        x, y, w, h = cv2.boundingRect(i)
        # pegar a parte do objeto e gerar uma imagem
        ROI = img[y:y + h, x:x + w]
        larguraR = int(ROI.shape[0] / 4)
        alturaR = int(ROI.shape[1] / 4)
        if (larguraR > 20):
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


#Ler a imagem
img = cv2.imread('../base_dados/ifro/Eusinofilos/eusinofilo_03.jpg')


largura = int(img.shape[0] / 4)
altura = int(img.shape[1] / 4)
img = cv2.resize(img,(altura,largura))
contarBrancas()
cv2.imshow('Original', img)
cv2.waitKey(0)

