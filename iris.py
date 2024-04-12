import pandas as pd
from klearn tel selection impot rain test split
iris = load iris()
X = iris.data
y = iris.target
X train,
X_test, Y_train, Y_test = train_test.
split(X, y, test_size=0.2, random_state=42)
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
model fit (X_train, Y_train) from sklearn.metrics import accuracy_score, classification_report
y_pred = model. predict (X_test)
accuracy = accuracy_score (y_test, y_pred)
report = classification_report(y_test, y_pred, target _names=iris. target_names)
print ("Accuracy:", accuracy)
print ("Classification Report: \n", report)
