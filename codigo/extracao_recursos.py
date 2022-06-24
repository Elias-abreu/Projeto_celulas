from qt_core import *
import mahotas
from mahotas.features import surf
#Ver redes de aprendizados profundos. Deep learning.
#region-based cnn, r-cnn, u-net

class Extracao_Recursos():
    def __init__(self,pasta_dados):
        self.pasta_dados = pasta_dados

    def extrair_recursos(self,algoritmo):
        dados = list() # Armazenar as características das imagens
        classes = list() # Armazenar as classes das imagens
        for pasta in os.listdir(self.pasta_dados):
            subpastas = os.path.join(self.pasta_dados,pasta) # Carregar as subpastas
            if not pasta.startswith('.'):
                if(pasta in ['baso']):
                    label = 1
                elif(pasta in ['eosi']):
                    label = 2
                elif (pasta in ['lymp']):
                    label = 3
                elif (pasta in ['mono']):
                    label = 4
                elif (pasta in ['neut']):
                    label = 5
                else:
                    label = 0

            if os.path.isdir(subpastas):
                print(f"Carregando os dados da classe {subpastas}")
                for arquivoImagem in os.listdir(subpastas):
                    try:
                        imagem = cv2.imread(os.path.join(subpastas,arquivoImagem))
                        #imagem = cv2.resize(imagem,(300,300))
                        if(algoritmo =="haralick"):
                            caracteristicas = self.extrair_Haralick(imagem)
                        elif(algoritmo == "LBP"):
                            caracteristicas = self.extrair_LBP(imagem)
                        elif (algoritmo == "HOG"):
                            caracteristicas = self.extrair_hog(imagem)
                        dados.append(caracteristicas)
                        #print(label)
                        classes.append(label)

                    except Exception as e:
                        print(F"Erro ao carregar a imagem: {arquivoImagem}")
                        print(str(e))
        return dados, classes

    def extrair_Haralick(self,imagem):
        recursos = mahotas.features.haralick(imagem).mean(axis=0)
        return recursos

    def extrair_LBP(self,imagem):
        im = mahotas.colors.rgb2grey(imagem)
        recursos = mahotas.features.lbp(im,radius =50, points = 20)
        #print(recursos)
        return recursos

    def extrair_hog(self,imagem):
        imagem = cv2.resize(imagem, (300, 300))
        fd = feature.hog(imagem,transform_sqrt=True)
        #hog(imagem, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True)
        #fd,hog_feature = hog(imagem, orientations=9, pixels_per_cell=(8, 8),cells_per_block=(2, 2), block_norm='L2-Hys', visualize=False)
        #print(fd)
        #print(len(fd))
        return np.array(fd)


def main():
    recursos = Extracao_Recursos("../base_dados_cinza")
    imagem = cv2.imread("../base_dados_cinza/neut/img_1.png")
    recursos.extrair_hog(imagem)

#main()