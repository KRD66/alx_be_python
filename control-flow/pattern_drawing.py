user_input = int(input("Enter the size of the pattern: "))
row = 0
while row < user_input:
    for col in range(user_input):
        print("*" , end = "")
    print()
    row += 1



def greet(name):
  """Prints a greeting message."""
print(f"Hello, {name}!")
