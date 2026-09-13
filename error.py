try:
    num = int(input("Enter number: "))
    result = 100 / num
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting gracefully.")