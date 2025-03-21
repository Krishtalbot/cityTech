def inversion(arr):
    count = 0
    inversions = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
                inversions.append((arr[i], arr[j]))
    return count, inversions


arr = [1, 3, 2, 5, 7, 4, 9, 8]
count, inversions = inversion(arr)
print(f"The number of inversions is {count}")
print("The inversions are:")
for i in inversions:
    print(i)
