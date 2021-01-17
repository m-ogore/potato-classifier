# import the necessary packages
import os

# initialize the path to the *original* input directory of images
# ORIG_INPUT_DATASET = "Potatoes"

# initialize the base path to the *new* directory that will contain
# our images after computing the training and testing split
ORIG_BASE_PATH = "ready_base"
ORIG_IMAGES = os.path.sep.join([ORIG_BASE_PATH, "ready"])
ORIG_ANNOTS = os.path.sep.join([ORIG_BASE_PATH, "Annotations"])

BASE_PATH = "dataset"
POSITVE_PATH = os.path.sep.join([BASE_PATH, "Good"])
NEGATIVE_PATH = os.path.sep.join([BASE_PATH, "Bad"])
# initialize the list of class label names
CLASSES = ["Good", "Bad"]
#INPUT_DIMS=(224, 224)

# set the batch size when fine-tuning
BATCH_SIZE = 32

# initialize the label encoder file path and the output directory to
# where the extracted features (in CSV file format) will be stored
ENCODER_PATH = os.path.sep.join(["output", "le.cpickle"])
BASE_CSV_PATH = "output"


# define the number of max proposals used when running selective
# search for (1) gathering training data and (2) performing inference
MAX_PROPOSALS = 2000
MAX_PROPOSALS_INFER = 200
# define the maximum number of positive and negative images to be
# generated from each image
MAX_POSITIVE = 30
MAX_NEGATIVE = 10

# initialize the input dimensions to the network
#MODEL_PATH = "potato.model"
INPUT_DIMS = (96, 96)
# define the path to the output model and label binarizer
MODEL_PATH = "potato.model"
#MODEL_PATH = "potato_detector.h5"
ENCODER_PATH = "lb.pickle"
# define the minimum probability required for a positive prediction
# (used to filter out false-positive predictions)
MIN_PROBA = 0.50
MAX_PROBA= 1.00	
