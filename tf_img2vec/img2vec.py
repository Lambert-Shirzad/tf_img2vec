from tensorflow import keras
from tensorflow.keras.applications import resnet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model

import numpy as np
from os import path
import shutil
import requests

    
class Img2Vec(object):

    def __init__(self):
        
        model_path = '../model/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5'
        if path.exists(model_path) == False:
            print('Downloading the model weights...')
            url = 'https://github.com/keras-team/keras-applications/releases/download/resnet/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5'
            with requests.get(url, stream=True) as r:
                with open(model_path, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
            
        print('Loading the model weights from \n', model_path)
        
        model = resnet50.ResNet50(include_top=False, weights=model_path, pooling='avg')
        self.embedding_model = Model(inputs=model.input, 
                                     outputs=model.output)


    def get_vec(self, image_path):
        """ Gets a vector embedding from an image of size 2048.
        :param image_path: path to image on filesystem
        :returns: numpy ndarray
        """
        
        _TARGET_SIZE = (224, 224)
        img = image.load_img(image_path, target_size=_TARGET_SIZE)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = resnet50.preprocess_input(x)
        embedding_vector = self.embedding_model.predict(x)
        
        return embedding_vector[0]
    
if __name__ == "main":
     pass    