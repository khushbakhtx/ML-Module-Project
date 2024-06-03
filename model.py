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

data = pd.read_csv("datasets/imon_international_dataset_cleaned.csv")
data = data.drop(['Unnamed: 0'], axis=1)
data['Просрочки за цикл (кумулятивный) [for classification]'] = (data['Просрочки за цикл (кумулятивный)'] < 30).astype(int)
X = data.drop(['Просрочки за цикл (кумулятивный) [for classification]', 'Просрочки за цикл (кумулятивный)'], axis=1)
y_classification = data['Просрочки за цикл (кумулятивный) [for classification]']
X_train, X_test, y_train, y_test = train_test_split(X, y_classification, test_size = 0.3, random_state = 0)

rfc_model = RandomForestClassifier(criterion='gini',
                                 n_estimators=41,
                                 random_state=None,
                                 n_jobs=None)
rfc_model.fit(X_train, y_train)
y_pred_rfc = rfc_model.predict(X_test)
score = rfc_model.score(X_test, y_test)
print(f"Accuracy: {round(score*100, 1)}%")

# import joblib
# joblib.dump(rfc_model, "imon_international_model.joblib")
print(X.columns)
