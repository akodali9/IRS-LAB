# Task 2

def calculate_precision_recall(y_true, y_pred):
    TP = sum((y_pred[i] == 1) and (y_true[i] == 1) for i in range(len(y_pred)))
    FP = sum((y_pred[i] == 1) and (y_true[i] == 0) for i in range(len(y_pred)))
    FN = sum((y_pred[i] == 0) and (y_true[i] == 1) for i in range(len(y_pred)))
    print(f"TP: {TP}\nFP: {FP}\nFN: {FN}\n")
    
    precision = TP / (TP + FP) #Quality
    recall = TP / (TP + FN) #Quantity
    return precision, recall

# Values of a book
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1] 
y_pred = [1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1] 

print(f"y_true: {y_true}\ny_pred: {y_pred}\n")

pre, rec = calculate_precision_recall(y_true, y_pred)
print(f"Precesion: {pre}\nRecall: {rec}")