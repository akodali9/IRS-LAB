import random

# Sample search results (replace with actual YouTube API data)
search_results = [
    "Video 1: How to Bake a Cake",
    "Video 2: Python Programming Tutorial",
    "Video 3: Travel Vlog - Exploring Paris",
    "Video 4: Machine Learning Basics",
    "Video 5: Cooking Delicious Pasta"
]

while 1:

    user_query = input("Enter your search query\nenter 'end' to break:")
    if user_query == "end":
        exit()

    print("Search Results:")
    for i, result in enumerate(search_results, start=1):
        print(f"{i}. {result}")

    selected_video_index = int(input("Enter the number of the video you watched (0 to exit): "))
    if selected_video_index == 0:
        exit()

    user_feedback = input("Did you like the video? (y/n): ")

    if user_feedback.lower() == "y":
        relevance_increase = 0.1
    else:
        relevance_increase = -0.1

    relevance_scores = [random.uniform(0, 1) for _ in search_results]
    relevance_scores[selected_video_index - 1] += relevance_increase

    sorted_results = [result for _, result in sorted(zip(relevance_scores, search_results), reverse=True)]

    print("\nUpdated Search Results:")
    for i, result in enumerate(sorted_results, start=1):
        print(f"{i}. {result}")

    search_results = sorted_results