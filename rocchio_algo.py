# Task 6

import numpy as np

documents = np.array([
    [0.5, 0.4, 0.1, 0.3],
    [0.2, 0.3, 0.1, 0.3],
    [0.0, 0.5, 0.0, 0.1],
    [0.3, 0.1, 0.1, 0.4]
])

class_labels = np.array([0, 2, 0, 1])

query_vector = np.array([0.1, 0.3, 0.0, 0.2])

# Rocchio algorithm parameters
alpha = 1.0  # Weight for the original query
beta = 0.65  # Weight for relevant documents
gamma = 0.25  # Weight for non-relevant documents

relevant_indices = np.where(class_labels == 0)[0]
non_relevant_indices = np.where(class_labels == 1)[0]

relevant_centroid = np.mean(documents[relevant_indices], axis=0)
print(relevant_centroid)

non_relevant_centroid = np.mean(documents[non_relevant_indices], axis=0)
print(non_relevant_centroid)

# Rocchio formula
updated_query_vector = alpha * query_vector + beta * relevant_centroid - gamma * non_relevant_centroid

# Print the updated query vector    
print("\nUpdated Query Vector:")
print(updated_query_vector)
