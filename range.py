print("What level of brightness is required?")
brightness_desired = int(input())

print("\nAdjusting brightness...\n")
for brightness in range(2, brightness_desired + 1, 2 ):
    print(f"beep's brightness level: {'*' * brightness}")
    print(f"bop's brightness level: {'*' * brightness}")


print("adjustments complete")
