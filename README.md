<h1 align="center"> Posyandu-Line </h1>

![image](https://github.com/rendychristiann/posyandu-line-AI/assets/78911479/e60acddf-c8eb-4112-b31d-d8b2ba2a440a)

<p align="center"> 
Posyandu-Line is a digital posyandu platform that provides access to monitoring children's posyandu records, detailed posyandu information, health worker information, articles, along with AI features for early stunting detection.
</p>

<div align="center">
    <!-- Your badges here -->
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
    <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white">
    <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white">
    <img src="https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white">
    <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white">
    <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white">
    <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white">
    <img src="https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB">
    <img src="https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white">
</div>

## Teams

- Luthfi Ainiya Putri - Hustler (Web)
- Syaniarti - Hipster (Web)
- Adisty Pramudita P. R. - Hipster (Web)
- Riska Amelia - Hacker (Web)
- Rangga Aditya Pratama - Hacker (Web)
- Muhamad Satria - Hacker (Web)
- Ahmad Wildan A. N. - Scrum Master (AAI)
- Rendy Christian - Hacker (AAI)
- Henry Evandra - Hacker (AAI)
- Galang Prasanjaya - Hacker (AAI)

## Idea Background

### 1. Theme
Theme : Health & Education

### 2. Problem
Problem : Problems include limited posyandu information, the posyandu administrative system which is still manual, and parents' lack of understanding regarding children's growth and development.

### 3. Solution
Solution: We present this Posyandu schedule information website as a solution to the experience problems of users who experience problems in finding out information regarding the Posyandu activity schedule. The features we provide include digital access to the Posyandu schedule so that schedule information can be accessed online, a Child Monitoring Page to easily find out the child's growth and development, a discussion forum available so that parents can ask questions and discuss children's problems and so on with health workers. existing ones, as well as stunting detection to detect stunting from an early age in children. The features above were created as a collection of solutions to provide convenience and affordability to Posyandu facility users.

## Dataset and Algorithm

### 1. Dataset
- Data Collection <br />
The dataset we use is Stunting Toddler Detections data fron Kaggle with a usability score of 10.0, containing 121 thousand rows, consisting of age, gender, height and nutritional status. (https://www.kaggle.com/datasets/rendiputra/stunting-balita-detection-121k-rows)
- Data Cleaning <br />
The data provided from Kaggle is relatively clean and has no problematic or corrupt values. We perform EDA on the dataset to find data patterns and trends before carrying out data processing.
![image](https://github.com/rendychristiann/posyandu-line-AI/assets/78911479/bf45607f-f530-4dfb-8db1-e4f28a8ec2f8)
![image](https://github.com/rendychristiann/posyandu-line-AI/assets/78911479/e714c6de-6100-4e01-bc8a-b6019ca059ad)
![image](https://github.com/rendychristiann/posyandu-line-AI/assets/78911479/d2501c75-f203-478e-8a02-d05d5aa59971)

### 2. Algorithm

- Framework <br />
We use the K-Nearest Neighbor (KNN) algorithm to detect stunting based on input values ​​in the form of the baby's age and height. The model detection result is the baby's nutritional status. We encode the input and output values ​​into numerical form so that they can be processed by the model properly.

- Pembangunan Model <br />
Model building was carried out by dividing train data and test data with a ratio of 80:20. Model training was carried out using the KNeighborsClassifier function with 1 classifier.

- Model Evaluation <br />
Model evaluation is carried out by looking at the confusion matrix and classification report, in the form of precision, recall and f-1 scores, as well as accuracy.

## Prototype
https://www.figma.com/proto/K9mgnWsdbsTxbvqxnnlnna/Cut-Nyak-Dien---Design?node-id=3454-1728&t=1Zgt0cvBPcugDGjr-1&scaling=min-zoom&content-scaling=fixed&page-id=3014%3A810&starting-point-node-id=3454%3A1728

## Integration
Model integration is carried out by exporting the model and integrating it with a server program using Flask which can receive input for the baby's age and height, then produces a numerical output in the form of the baby's nutritional status categories.

## Deployment
Deployment of the model is carried out on an external platform, namely Render, with a program that is contained in this repository. The model API Endpoint is: posyandu-line-flask.onrender.com/predict. This API endpoint is integrated with the stunting detection web page using the JavaScript fetch feature.

## Result and Conclusion
Thus, the AI ​​model was successfully developed, trained, deployed and integrated with the web page, providing early stunting detection features for users in a good and responsive manner.
