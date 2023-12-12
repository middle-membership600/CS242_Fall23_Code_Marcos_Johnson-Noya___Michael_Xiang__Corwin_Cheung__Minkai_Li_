import pandas as pd

# Creating the Food DataFrame
data = {
    "Class": ["Apple Pie", "Bibimbap", "Cannoli", "Edamame", "Falafel", "French Toast",
              "Ice Cream", "Ramen", "Sushi", "Tiramisu"],
    "Accuracy1": [0.86, 1.00, 0.96, 1.00, 1.00, 0.98, 0.90, 0.94, 0.96, 0.98],
    "Accuracy2": [0.50, 0.984, 0.778, 0.918, 0.946, 0.862, 0.566, 0.922, 0.754, 0.94]
}

df = pd.DataFrame(data)

# Calculating the correlation between Accuracy1 and Accuracy2
correlation = df[["Accuracy1", "Accuracy2"]].corr()
print(correlation)

# Creating the STL-10 DataFrame
data_2 = {
    "Class": ["Airplane", "Bird", "Car", "Cat", "Deer", "Dog",
              "Horse", "Monkey", "Ship", "Truck"],
    "Accuracy1": [0.98375, 0.9975, 0.97125, 0.89625, 0.9725, 0.9675,
                  0.9925, 0.97, 0.99875, 0.98625],
    "Accuracy2": [0.9747, 0.9646, 0.8395, 0.6167, 0.9729, 0.8416,
                  0.941, 0.8222, 0.9895, 0.9579]
}

df_2 = pd.DataFrame(data_2)

# Calculating the correlation between Accuracy1 and Accuracy2 for the new dataset
correlation_2 = df_2[["Accuracy1", "Accuracy2"]].corr()
print(correlation_2)
