from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from codigo.extracao_recursos import Extracao_Recursos
from sklearn.metrics import accuracy_score,precision_score
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import GridSearchCV, KFold,RepeatedKFold
from sklearn.model_selection import GroupKFold
import os
import cv2
import numpy as np
from joblib import dump


class Criar_classificadores():
    def __init__(self,dados,classes):
        sc_X = StandardScaler()
        #print(dados)
        self.dados = sc_X.fit_transform(dados)
        self.classes = np.array(classes)
        self.x_train, self.x_test, self.y_trein, self.y_test = train_test_split(np.array(self.dados), np.array(self.classes),
                                                            test_size=0.33)

    def classificador_rf(self):
        modelo = RandomForestClassifier(n_estimators=1000)
        val_scores = cross_val_score(modelo, self.dados, self.classes, cv=10)
        print("---RF---")
        #print('Acurácia nos k-folds:', val_scores)
        print('Média: {:.2} | Desvio: {:.2}'.format(np.mean(val_scores), np.std(val_scores)))
        modelo.fit(self.dados, self.classes)
        return modelo

    def classificador_reg_logistica(self):
        modelo = LogisticRegression(solver="saga",max_iter=300)
        print("---RL---")
        val_scores = cross_val_score(modelo, self.dados, self.classes, cv=10)
        #print('Acurácia nos k-folds:', val_scores)
        print('Média: {:.2} | Desvio: {:.2}'.format(np.mean(val_scores), np.std(val_scores)))
        modelo.fit(self.dados, self.classes)
        return modelo

    def classificador_MLP(self):
        modelo = MLPClassifier(hidden_layer_sizes=(200,100), activation="tanh", random_state=1)
        val_scores = cross_val_score(modelo, self.dados, self.classes, cv=10,scoring='accuracy')
        print("---MLP---")
        #print('Acurácia nos k-folds:', val_scores)
        print('Média: {:.2} | Desvio: {:.2}'.format(np.mean(val_scores), np.std(val_scores)))
        modelo.fit(self.dados,self.classes)
        return modelo

    def classificador_SVM(self):
        parameters = {'kernel': ('linear', 'rbf','poly'),'degree':[1, 10], 'C': [1, 10]}
        #modelo = svm.SVC(kernel="linear",degree=4,C=3)
        svc = svm.SVC()
        modelo = GridSearchCV(svc, parameters, cv = RepeatedKFold(n_splits=10,n_repeats=10))
        cross_val = cross_val_score(modelo, self.dados, self.classes, cv = KFold(10,shuffle=True),)
        print("---SVM---")
        modelo.fit(self.dados,self.classes)
        #print(grid.best_score_)
        #modelo = svm.SVC(grid.best_score_)
        print('Média: {:.2} | Desvio: {:.2}'.format(np.mean(cross_val), np.std(cross_val)))
        #modelo.fit(self.dados,self.classes)
        #arquivo = 'arquivos_treinados/svm.joblib.pkl'
        #dump(modelo, arquivo, compress=9)
        return modelo

    def gerar_classificador_knn(self):
        modelo = KNeighborsClassifier(n_neighbors=9)
        val_scores = cross_val_score(modelo, self.dados, self.classes, cv=10)
        print("---KNN---")
        # print('Acurácia nos k-folds:', val_scores)
        print('Média: {:.2} | Desvio: {:.2}'.format(np.mean(val_scores), np.std(val_scores)))
        modelo.fit(self.dados, self.classes)
        return modelo

    def gerar_classificador_NB(self):
        modelo = GaussianNB()
        val_scores = cross_val_score(modelo, self.dados, self.classes, cv=10)
        print("---NB---")
        # print('Acurácia nos k-folds:', val_scores)
        print('Média: {:.2} | Desvio: {:.2}'.format(np.mean(val_scores), np.std(val_scores)))
        modelo.fit(self.dados, self.classes)
        return modelo

    def gerar_classificador_AdaBost(self):
        modelo = AdaBoostClassifier()
        val_scores = cross_val_score(modelo, self.dados, self.classes, cv=10)
        print("---AdaBost---")
        # print('Acurácia nos k-folds:', val_scores)
        print('Média: {:.2} | Desvio: {:.2}'.format(np.mean(val_scores), np.std(val_scores)))
        modelo.fit(self.dados, self.classes)
        return modelo


def main():
    recursos = Extracao_Recursos("../base_dados/base_dados_cinza_preparada")
    dados, classes = recursos.extrair_recursos("haralick")
    classificadores = Criar_classificadores(dados, classes)
    modelo1 = classificadores.classificador_MLP()
    modelo2 = classificadores.classificador_reg_logistica()
    modelo3 = classificadores.classificador_rf()
    modelo4 = classificadores.classificador_SVM()
    modelo5 = classificadores.gerar_classificador_knn()

    #modelo6 = classificadores.gerar_classificador_NB()
    #modelo7 = classificadores.gerar_classificador_AdaBost()



def main2():
    recursos = Extracao_Recursos("../base_dados_cinza")
    dados, classes = recursos.extrair_recursos("LBP")
    classificadores = Criar_classificadores(dados, classes)

    modelo = classificadores.gerar_classificador_AdaBost()
    # Testar na imagem 1
    imagem1 = cv2.imread("../base_dados_cinza/neut/img_22.png")
    vetor_img = recursos.extrair_LBP(imagem1)
    vetor_img = np.array(vetor_img)
    print(modelo.predict([vetor_img]))
    # Testar na imagem 2
    imagem2 = cv2.imread("../base_dados_cinza/eosi/img_6.png")
    tor_img = recursos.extrair_LBP(imagem2)
    vetor_img = np.array(vetor_img)
    print(modelo.predict([vetor_img]))
    #Testar na imagem 3
    imagem3 = cv2.imread("../base_dados_cinza/mono/img_3.png")
    tor_img = recursos.extrair_LBP(imagem3)
    vetor_img = np.array(vetor_img)
    print(modelo.predict([vetor_img]))

main()

