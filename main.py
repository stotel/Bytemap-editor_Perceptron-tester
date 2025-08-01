import numpy as np
import tensorflow as tf
import keras

model_path = input("specify model path (Models/model.keras by default)")
if model_path == "":
    model_path = "Models/model.keras"

model = keras.models.load_model(model_path)
