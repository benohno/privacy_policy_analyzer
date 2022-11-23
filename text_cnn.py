import os
import re
import shutil
import string
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import losses
from sklearn.preprocessing import MultiLabelBinarizer

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

print(tf.__version__)

batch_size = 32
seed = 42

raw_train_ds = tf.keras.utils.text_dataset_from_directory(
    './data/train/',
    batch_size=batch_size,
    validation_split=0.2,
    subset='training',
    seed=seed)

