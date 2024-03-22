import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression


def find_key_with_max_value(dictionary):
    max_value = max(dictionary.values())
    for key, value in dictionary.items():
        if value == max_value:
            return key
    return "Key not found"

scores = {}
model = LinearRegression()
X, y = load_diabetes(return_X_y=True, as_frame=True)
X.drop('sex', axis=1, inplace=True)

for feature1 in X.columns:
    for feature2 in X.columns:
        for feature3 in X.columns:
            selected_features = [feature1, feature2, feature3]
            X_subset = X[selected_features]
            model.fit(X_subset, y)
            score = model.score(X_subset, y)
            scores[f"{feature1}-{feature2}-{feature3}"] = score

best_feature_combination = find_key_with_max_value(scores)
print(f"The maximum score is {max(scores.values())} which is for the feature combination: {best_feature_combination}")

model.fit(X[best_feature_combination.split('-')], y)

plt.scatter(range(len(y)), y, label="True data")
plt.scatter(range(len(y)), model.predict(X[best_feature_combination.split('-')]), label="Predicted data")
plt.legend()
plt.show()
