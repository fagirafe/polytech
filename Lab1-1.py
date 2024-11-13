numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers.remove(None)
avg = round(sum(numbers) / (len(numbers)+1),2)
numbers.insert(4,avg)
print("Измененный список:", numbers)