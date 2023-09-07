# Task 5

import numpy as np

text_data = [
    "The world is thriving in social media.",
    "Social media has been the biggest platform for people to express themself.",
    "Some people still prefer to lead a private life.",
    "Many Problems throughout the world are expressed in the online platform.",
    "The amount of data the social media companies need to handle is more.",
    "Many compaines are worth billions as they succeed by the no of people using their platform giving them lots of data to generate ads.",
    "Online privacy is a doom nowadays"
]

# number of clusters (k)
k = 3

# Initialize cluster centroids randomly
np.random.seed(0)
centroids = np.random.choice(len(text_data), k, replace=False)
centroid_texts = [text_data[i] for i in centroids]

# Helper function to calculate the similarity between two texts
def similarity(text1, text2):
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    common_words = len(words1.intersection(words2))
    return common_words / (len(words1) + len(words2))

# Initialize cluster assignments
cluster_assignments = [-1] * len(text_data)

# Maximum number of iterations
max_iterations = 100

for _ in range(max_iterations):
    for i, text in enumerate(text_data):
        similarities = [similarity(text, centroid_texts[j]) for j in range(k)]
        cluster_assignments[i] = np.argmax(similarities)


clusters = {}
for i, cluster_id in enumerate(cluster_assignments):
    if cluster_id not in clusters:
        clusters[cluster_id] = []
    clusters[cluster_id].append(text_data[i])

for cluster_id, cluster_texts in clusters.items():
    print(f"Cluster {cluster_id + 1}:")
    for text in cluster_texts:
        print(f"- {text}")
    print()
