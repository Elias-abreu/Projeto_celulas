
#############################> CODIGO <#############################

'''
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from classificadores.extracao_recursos import Extracao_Recursos
from sklearn.metrics import accuracy_score,precision_score
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.model_selection import GroupKFold
import os
import cv2


import mahotas
from mahotas.features import surf
from sklearn.feature_extraction import image
from skimage import feature
from skimage.transform import resize
import matplotlib.pyplot as plt
'''

#############################> GUI <#############################

# IMPORT MODULES
import sys
from PySide6.QtCore import QPropertyAnimation
from PySide6 import QtCore
from PySide6.QtGui import QColor
from PySide6.QtWidgets import *
import os
import cv2
import numpy as np

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


#from skimage import feature
