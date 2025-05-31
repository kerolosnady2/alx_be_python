size = int(input("Enter the size of the pattern: "))

print(f"\nDrawing a {size}x{size} pattern:\n")

row = 1

while row <= size:
    for col in range(1, size + 1):
        print("*", end="")
    print()
    
    row += 1
