import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, log_loss
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import roc_auc_score, roc_curve, auc, accuracy_score, mean_squared_error

data = pd.read_csv("datasets/obesity_final.csv")
X = data.drop(['NObeyesdad', 'Unnamed: 0', 'BMI'], axis=1)
y = data['NObeyesdad']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

rfc_model = RandomForestClassifier(criterion='entropy', 
                                   n_estimators=111, 
                                   max_depth=16,
                                   min_samples_split=3,
                                   min_samples_leaf=2,
                                   random_state=1)
rfc_model.fit(X_train, y_train)
y_pred_rfc = rfc_model.predict(X_test)
score = rfc_model.score(X_test, y_test)
print(f"Accuracy: {round(score*100, 1)}%")


import joblib
accuracy = accuracy_score(y_test, y_pred_rfc)
model_info = {'model': rfc_model, 'accuracy': accuracy}
joblib.dump(model_info, "obesity_package.joblib")

# Load the model and accuracy score
# model_info = joblib.load("model_info.joblib")
# model = model_info['model']
# accuracy = model_info['accuracy']