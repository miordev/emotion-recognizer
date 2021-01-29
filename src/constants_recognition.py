import os

# ----- Emociones -----
HAPPY = 'Felicidad'
ANGRY = 'Molesto'
SURPRISE = 'Sorpresa'
SAD = 'Tristeza'

EMOTIONS = [HAPPY, ANGRY, SURPRISE, SAD]

# ----- Métodos -----
EIGEN_FACES = 'EigenFaces'
FISHER_FACES = 'FisherFaces'
LBPH = 'LBPH'

# ----- Umbrales -------
LIMIT_EIGEN_FACES = 5700
LIMIT_FISHER_FACES = 500
LIMIT_LBPH = 600

# ----- Dimensiones -----
HORIZONTAL_DIMENSION = 48
VERTICAL_DIMENSION = 48

DIMENSIONS = (HORIZONTAL_DIMENSION, VERTICAL_DIMENSION)

# ----- Rutas -------
DIRNAME = os.path.dirname(__file__)

MODELS_PATH = os.path.join(DIRNAME, '..models')
DATA_PATH = os.path.join(DIRNAME, '../data')