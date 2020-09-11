# tf_img2vec
This library uses the ResNet50 model in TensorFlow Keras, pre-trained on Imagenet, to generate a 2048 embedding vector for an input image. 

# Install
1. With a local version of the code:

```git clone https://github.com/Lambert-Shirzad/tf_img2vec```

```cd ./tf_img2vec```

```pip install --user ./```

2. Directly from github:

```pip install git+git://github.com/Lambert-Shirzad/tf_img2vec.git```

# Usage
```python
from tf_img2vec.img2vec import Img2Vec
img2vec = Img2Vec()
x = img2vec.get_vec('./examples/tree1.jpeg')
```

# Reference
Majority of the code is taken from https://github.com/jaredwinick/img2vec-keras
The main updates are:
  1. Initialization of the embedding model:
  
  I have used the built-in Keras functions to directly load a ResNet50 model ending at the avg_pool layer. This make the model slightly lighter and faster to load.
  
  2. Downloading of the pre-trained model:
  
  The script was changed to download the weights for the clipped version of ResNet50 into a local `./model` directory. 
