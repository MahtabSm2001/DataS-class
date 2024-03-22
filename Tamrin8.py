from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.datasets import make_blobs
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

results_list = []
execution_times = []
accuracy_scores = []
num_samples = []
num_features = []
random_seeds = []

for sample_count in [100, 300, 500, 700, 1000, 2000, 5000, 10000]:
    for feature_count in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        for seed in range(10):
            X, y = make_blobs(
                n_samples=sample_count,
                n_features=feature_count,
                centers=3,
                random_state=10
            )
            start_time = time.time()
            model = LogisticRegression()
            model.fit(X, y)
            y_pred = model.predict(X)
            accuracy = model.score(X, y) * 100
            end_time = time.time()
            execution_times.append(end_time - start_time)
            accuracy_scores.append(accuracy)
            num_samples.append(sample_count)
            num_features.append(feature_count)
            random_seeds.append(seed)

data = {
    "Execution Time (s)": execution_times,
    "Accuracy Score (%)": accuracy_scores,
    "Number of Samples": num_samples,
    "Number of Features": num_features,
    "Random Seeds": random_seeds
}

result_df = pd.DataFrame(data)
plt.plot(result_df["Execution Time (s)"], result_df["Accuracy Score (%)"])
plt.xlabel("Execution Time (s)")
plt.ylabel("Accuracy Score (%)")
plt.title("Accuracy vs. Execution Time")
plt.show()
