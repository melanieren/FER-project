# FER-project

This repository contains the code for our CS 486 class project, which aims to compare different CNN techniques for recognizing facial emotions. 

Two types of CNNs were explored and compared:
1. A simple CNN based on the architecture proposed in the paper [Facial Emotion Recognition using Convolutional Neural Networks](https://ieeexplore-ieee-org.proxy.lib.uwaterloo.ca/abstract/document/8981757) by Zeynab Rzayeva and Emin Alasgarov
2. A ResNet based on the architecture proposed in the paper [Facial Sentiment Classification Based on Resnet-18 Model](https://ieeexplore-ieee-org.proxy.lib.uwaterloo.ca/stamp/stamp.jsp?tp=&arnumber=8990979&tag=1) by Yitao Zhou, Shun Nishide, Fuji Ren, and Xin Kang

## Features
- Preprocess FER-2013 and MSFDE datasets using histogram equalization, data augmentation, and face cropping/alignment (optional)
- Train various CNN models with different hyperparameters on FER-2013
- Train various ResNet models with different hyperparameters on FER-2013
- Finds optimal parameters through grid search in an optimal fashion
- Test CNN and ResNet models on FER-2013 test set and MSFDE

## Required libraries
- We **highly** recommend running the provided notebooks in Google Colab, as the default environment provides all required libraries

## Installation/Preprocessing
1. Download the FER-2013 dataset from https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data
2. (Optional) Request access to the MSFDE dataset and download once approved from http://www.psychophysiolab.com/msfde/terms.php
3. Upload all notebooks and data to Google Drive, or modify the notebooks to access the data locally
4. Run the [preprocessing](https://github.com/melanieren/FER-project/blob/main/preprocessing.ipynb) notebook to generate preprocessed data for the FER-2013 dataset. You may need to modify file load and save locations to fit your Google Drive layout

## Train and evaluate a Simple CNN model on FER-2013
1. Run the [simple_cnn](https://github.com/melanieren/FER-project/blob/main/simple_CNN.ipynb) notebook to train a variety of CNN models on the FER-2013 dataset.
2. The notebook will automatically find the best hyperparameters on the validation set and output the test set accuracy and prediction distribution as shown below.
![simple_cnn_output](simple_CNN_output.jpg)

## Train and evaluate a Residual Network model on FER-2013
1. Run the [resnet](https://github.com/melanieren/FER-project/blob/main/resnet.ipynb) notebook to train a residual network model on the FER-2013 dataset.
2. The notebook will automatically find the best hyperparameters on the validation set and output the test set accuracy and prediction distribution.

## Evaluate saved models on MSFDE
1. Run the [preprocess_msfde](https://github.com/melanieren/FER-project/blob/main/preprocess_msfde.ipynb) notebook to generate preprocessed data. You may need to modify file load and save locations to fit your Google Drive layout
2. Ensure the Simple CNN model and Residual Network model have already been saved to your drive
3. Run the [MSFDE_evaluate](https://github.com/melanieren/FER-project/blob/main/MSFDE_evaluate.ipynb) notebook to generate predictions from the best simple CNN and Residual Network models on the MSFDE dataset. For each race, the notebook will output the accuracy and prediction distribution as shown below.
![msfde_cnn_eval_output](MSFDE_eval_cnn_output.jpg)
![msfde_resnet_eval_output](MSFDE_eval_resnet_output.jpg)

## Datasets 
- [FER-2013](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data): The FER-2013 dataset was used to train and evaluate both types of models. 
- [MSFDE](http://www.psychophysiolab.com/en/download.php): The Montreal Set of Facial Displays of Emotion (MSFDE) dataset was used to evaluate both types of models, in order to investigate potential racial bias in the model predictions. 

