import numpy as np

web_graph = np.array([
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
])

num_pages = len(web_graph)
pagerank = np.ones(num_pages) / num_pages
print(pagerank)

damping_factor = 0.65
tolerance = 1e-6

while True:
    new_pagerank = np.zeros(num_pages)
    for i in range(num_pages):
        for j in range(num_pages):
            if web_graph[j, i] == 1:
                new_pagerank[i] += pagerank[j] / np.sum(web_graph[j, :])
    new_pagerank = (1 - damping_factor) / num_pages + damping_factor * new_pagerank

    if np.sum(np.abs(new_pagerank - pagerank)) < tolerance:
        break

    pagerank = new_pagerank

sorted_pages = np.argsort(pagerank)[::-1]
for i in sorted_pages:
    print(f"Page {i + 1}: PageRank = {pagerank[i]:.4f}")
