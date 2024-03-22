import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, LeaveOneOut, LeavePOut, KFold
import pandas as pd
import random


def evaluate_model(X_train, X_test, y_train, y_test, model):
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    return score


rand1 = random.randint(0, 50)
rand2 = random.randint(0, 50)

X, y = load_diabetes(return_X_y=True, as_frame=True)
y = pd.DataFrame(y)
X = pd.DataFrame(X)
X.drop('sex', axis=1, inplace=True)

model = LinearRegression()

feature_combinations = [(i1, i2, i3) for i1 in X.columns for i2 in X.columns for i3 in X.columns]

best_score = -1
best_case = None

# Iterate over feature combinations
for i1, i2, i3 in feature_combinations:
    features = [i1, i2, i3]
    X_subset = X[features]

    for train_size in [0.7, 0.8]:
        X_train, X_test, y_train, y_test = train_test_split(X_subset, y, train_size=train_size, random_state=rand1)
        score = evaluate_model(X_train, X_test, y_train, y_test, model)
        if score > best_score:
            best_score = score
            best_case = f"{i1}-{i2}-{i3}-train_test_split {int(train_size * 100)}%"

    X_arr = X_subset.to_numpy()
    y_arr = y.to_numpy()
    loo = LeaveOneOut()
    for _, test_index in list(loo.split(X_arr)):
        X_train, X_test = X_arr[test_index == 0], X_arr[test_index == 1]
        y_train, y_test = y_arr[test_index == 0], y_arr[test_index == 1]
        score = evaluate_model(X_train, X_test, y_train, y_test, model)
        if score > best_score:
            best_score = score
            best_case = f"{i1}-{i2}-{i3}-LOO"

    for p_value in [2, 4]:
        leave_p_out = LeavePOut(p=p_value)
        for train_indices, test_indices in list(leave_p_out.split(X_subset)):
            X_train, X_test = X_subset.iloc[train_indices], X_subset.iloc[test_indices]
            y_train, y_test = y.iloc[train_indices], y.iloc[test_indices]
            score = evaluate_model(X_train, X_test, y_train, y_test, model)
            if score > best_score:
                best_score = score
                best_case = f"{i1}-{i2}-{i3}-LPO{p_value}"

    for n_splits in [5, 8]:
        kf = KFold(n_splits=n_splits, shuffle=True, random_state=rand1)
        for train_indices, test_indices in list(kf.split(X_subset)):
            X_train, X_test = X_subset.iloc[train_indices], X_subset.iloc[test_indices]
            y_train, y_test = y.iloc[train_indices], y.iloc[test_indices]
            score = evaluate_model(X_train, X_test, y_train, y_test, model)
            if score > best_score:
                best_score = score
                best_case = f"{i1}-{i2}-{i3}-KFold{n_splits}"

print(best_case)
print(best_score)
