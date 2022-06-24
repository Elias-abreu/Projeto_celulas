import cv2
from qt_core import *
from codigo.extracao_recursos import Extracao_Recursos
from joblib import dump, load
from codigo.classificador import Criar_classificadores
cont = 51

class Contagem:

    def __init__(self,imagem):
        img = cv2.imread(imagem)
        largura = int(img.shape[0] / 4)
        altura = int(img.shape[1] / 4)
        self.img = cv2.resize(img, (altura, largura))
        totalBrancas, imgV = self.contagem_globulos_brancos()
        totalVermelhas = self.contarVermelhas(imgV)
        #cv2.imshow('BRANCOS: ' + str(totalBrancas), self.img)
        img = cv2.resize(self.img,(600,600))
        cv2.imshow('BRANCOS: '+ str(totalBrancas)+'     VERMELHOS: '+ str(totalVermelhas), img)
        cv2.waitKey(0)

    def contarVermelhas(self,imgV):
        # Transformar em escala de cinza
        imgCinza = cv2.cvtColor(imgV, cv2.COLOR_BGR2GRAY)

        # Suavizar a imagem
        suave = cv2.GaussianBlur(imgCinza, (7, 7), 0)

        # Binarizar a imagem
        ret2, binn2 = cv2.threshold(suave.copy(), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Removendo ruído
        kernel = np.ones((3, 3), np.uint8)
        binn2 = cv2.morphologyEx(binn2, cv2.MORPH_OPEN, kernel, iterations=2)

        # Erosão de 5 na imagem
        kernel = np.ones((3, 3), np.uint8)
        erosao = cv2.erode(binn2, kernel, iterations=1)

        # Dilatação na imagem resultante da erosão
        kernelD = np.ones((9, 9), np.uint8)
        dilation = cv2.dilate(erosao, kernelD, iterations=1)

        # Detectar bordas com Canny
        bordas = cv2.Canny(dilation, 20, 120, apertureSize=7)
        objetos, lx = cv2.findContours(bordas.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        cont = 0
        celulasVermehras = []
        plaquetas = []
        contador = 0
        for i in objetos:
            x, y, w, h = cv2.boundingRect(i)
            ROI = imgV[y:y + (h), x:x + (w)]  # pegar uma imagem do cortorno
            larguraR = int(ROI.shape[0] / 4)
            alturaR = int(ROI.shape[1] / 4)
            if (larguraR > 7 and larguraR < 100) or (alturaR > 7 and alturaR < 100):
                celulasVermehras.append(i)

        cv2.drawContours(self.img, celulasVermehras, -1, (255, 0, 0), 2)
        print(contador)
        return len(celulasVermehras)

    def contagem_globulos_brancos(self):
        tamanhoMinimo = 10
        imgV = self.img.copy()
        # Converter para o espaço de cor definido
        hsv = cv2.cvtColor(self.img, cv2.COLOR_LBGR2LAB)
        # Pegar a nargura e altura da imagem e dividir por 4, objetivo não ter imagens grandes

        # Realizar a suavsão da imagem
        blur = cv2.GaussianBlur(hsv, (5, 5), 0)

        # Configuração das cores a serem cortadas
        # 160,135,91  - 219,166,124
        # 165,140,96  - [219,166,124

        #valor_minimo = np.array([165, 140, 96])
        #valor_maximo = np.array([219, 166, 124])
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
        contador = 0
        global cont
        for i in objetos:
            x, y, w, h = cv2.boundingRect(i)
            # pegar a parte do objeto e gerar uma imagem
            ROI = self.img[y:y + h, x:x + w]
            larguraR = int(ROI.shape[0] / 4)
            alturaR = int(ROI.shape[1] / 4)
            if (larguraR > tamanhoMinimo):
                ext = Extracao_Recursos("")
                imgcinza = cv2.cvtColor(ROI, cv2.COLOR_RGB2GRAY)
                recurso_img = ext.extrair_Haralick(imgcinza)
                dir_folder = "codigo/arquivos_treinados"
                #recursos = Extracao_Recursos("base_dados/base_dados_cinza_preparada")
                #dados, classes = recursos.extrair_recursos("haralick")
                #classificador_c = Criar_classificadores( dados, classes )
                #classifier = classificador_c.classificador_SVM()
                filename = 'codigo/svm.joblib.pkl'
                classifier = load(filename)
                #data = get_data(dir_folder)
                new_predict = classifier.predict([recurso_img])
                if(new_predict == [1]):
                    cv2.putText(self.img, "Basofolo", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,255))
                    #print("baso")
                elif(new_predict == [2]):
                    cv2.putText(self.img, "Eusinofolo", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255))
                    #print("eosi")
                elif (new_predict == [3]):
                    cv2.putText(self.img, "Linfocitos ", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255))
                    #print("lymp")
                elif (new_predict == [4]):
                    cv2.putText(self.img, "Monocito ", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255))
                    #print("Monócito")
                elif (new_predict == [5]):
                    cv2.putText(self.img, "neutrofilo ", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255))
                    #print("neut")
                #print("A classe é ",new_predict)
                #cv2.imwrite("base/neut/" + str(cont) + ".bmp", imgcinza)
                cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                imgV[y:y + h, x:x + w] = 255
                # classe = reconhecimento(str(cont) + ".bmp")
                cont += 1
                contador += 1
                # cv2.putText(img,"QT_FONT_NORMAL",(y+50,x-20),cv2.QT_FONT_NORMAL,1,(0,0,255))

        # imgF = cv2.resize(imgV, (altura, largura))
        # cv2.imshow("T ",imgF)
        return contador, imgV