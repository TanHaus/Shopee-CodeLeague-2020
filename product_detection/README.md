# Product Detection

Student Category

TanHaus achieved rank 133 in the Private Leaderboard ([link](https://www.kaggle.com/c/shopee-product-detection-student/leaderboard)), with Top-1 accuracy score of 0.79218 and placed at top 20%.

## Outline of the work
- Oversample the minority classes to create a balanced dataset
- Perform transfer learning on a pre-trained BiT-M R50x1 from TensorFlow Hub ([link](https://tfhub.dev/google/bit/m-r50x1/1))
- Apply traditional and moden image augmentation techniques (e.g. CutOut, MixUp)

BiT-M was chosen because it was designed specifically for efficient and fast transfer learning. The team also tried transfer learning with EfficientNet B3 and ResNet50, but was not able to match the performance of BiT-M.

Training was done on Google Colab (K80, T4, or P100), Kaggle notebook (P100), and GCP notebook (T4).

Detailed explanation of the code can be found in the [notebook](notebook.ipynb)

## Link to dataset

Link 1: https://drive.google.com/drive/folders/1V_sHZN2MmhcfeVao3hoJpjRWLSnm1_Pe

Link 2: https://drive.google.com/drive/folders/1PIJHZ6QXU5rjskT7dIimyEUdQJ84YvoR

## Resources

TensorFlow has a good collection of tutorials. Most of TanHaus code for Product Detection is derived from the official tutorials

Name | Link | What
-----|------|------
Load image dataset | https://www.tensorflow.org/tutorials/load_data/images | Use `tf.data.Dataset` for fast and efficient data loading
Transfer learning with TensorFlow Hub| https://www.tensorflow.org/tutorials/images/transfer_learning_with_hub | Transfer learning from a model on TensorFlow Hub

### Coursera - Introduction to TensorFlow

Title | Notebook link
------|--------------
TensorFlow Hello World | https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Course%201%20-%20Part%202%20-%20Lesson%202%20-%20Notebook.ipynb
Introduction to Computer Vision | https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Course%201%20-%20Part%204%20-%20Lesson%202%20-%20Notebook.ipynb
Introduction to Convolution and Max Pooling | https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Course%201%20-%20Part%206%20-%20Lesson%202%20-%20Notebook.ipynb
Build a classification model for Horse and Human | https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Course%201%20-%20Part%208%20-%20Lesson%202%20-%20Notebook.ipynb

### Coursera - CNN with TensorFlow

Title | Notebook link
------|--------------
Build a simple model on Cats and Dogs data | https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Course%202%20-%20Part%202%20-%20Lesson%202%20-%20Notebook.ipynb
Data Augmentation on Cats and Dogs data | https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Course%202%20-%20Part%204%20-%20Lesson%202%20-%20Notebook%20(Cats%20v%20Dogs%20Augmentation).ipynb
A model on Horse and Human data | https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Course%202%20-%20Part%204%20-%20Lesson%204%20-%20Notebook.ipynb
Transfer learning from InceptionV3 for Cats and Dogs data | https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Course%202%20-%20Part%206%20-%20Lesson%203%20-%20Notebook.ipynb
Multiclass classification with Rock - Paper - Scissors | https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Course%202%20-%20Part%208%20-%20Lesson%202%20-%20Notebook%20(RockPaperScissors).ipynb
