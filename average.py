def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


data = []
result = calculate_average(data)
print(f"Среднее значение: {result}")