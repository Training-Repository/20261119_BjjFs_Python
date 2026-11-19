def divide(a, b):
    # if b == 0:
    #     print("Error: Division by zero is not allowed.")
    #     raise Exception("Will NOT allow Division by zero")
    result = a / b
    print("Completed Calculation")
    return result


def main():
    try:
        print(divide(10, 2))  # Valid division
        # print(divide(10, 0))  # Division by zero
        # print(divide(10, 'a'))  # Invalid input type
    except (ZeroDivisionError, TypeError) as e:
        # print( f"An error occurred: {repr(e)}")
        print( f"An error occurred: {e!r}")
    except Exception as e:
        print(f"An unexpected error occurred: {e!r}")
    else:
        print("No exceptions occurred during division.")
    finally:
        print("Execution of divide function completed.")


main()