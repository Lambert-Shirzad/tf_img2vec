rom setuptools import setup, find_packages

setup(
    name='tf_img2vec',
    version='0.1',
    description='Returns a vector embedding for an input image using TensorFlow Keras',
    author='Navid Lambert-Shirzad',
    author_email='n.lambertshirzad@gmail.com',
    url='https://github.com/Lambert-Shirzad/tf_img2vec',
    license='Apache License 2.0',
    packages=find_packages(),
)