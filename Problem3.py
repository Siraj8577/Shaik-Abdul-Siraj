def generate_series(a: int):
    count = a if a % 2 != 0 else a - 1
    return [2 * i + 1 for i in range(count)]


a = int(input())
print(", ".join(map(str, generate_series(a))))
