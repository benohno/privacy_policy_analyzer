import tempfile
import tensorflow as tf
from tensorflow.keras.metrics import AUC
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import BinaryCrossentropy
from transformers import TFDistilBertForSequenceClassification, \
    DistilBertConfig, DistilBertTokenizerFast


export_dir = './model/policy_model.h5'
reloaded = tf.keras.models.load_model(export_dir)

print(reloaded.summary())
