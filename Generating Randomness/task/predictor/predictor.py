# Define the minimum required length for the binary string
MIN_LENGTH = 100


def filter_binary(binary_string):
    # Filter out characters that are not '0' or '1'
    return [x for x in binary_string if x in ["0", "1"]]


def fetch_user_input():
    # Get user input as a binary string
    return input("Print a random string containing 0 or 1:\n")


def main():
    # Initialize an empty list to store the binary digits
    binary_list = []

    # Continue fetching input until the list reaches the desired length
    while len(binary_list) < MIN_LENGTH:
        user_input = fetch_user_input()
        filtered_input = filter_binary(user_input)

        # Extend the binary list with the filtered input
        binary_list.extend(filtered_input)

        # Calculate and display the remaining symbols needed
        remaining_symbols = MIN_LENGTH - len(binary_list)
        print(f"Current data length is {len(binary_list)}, {remaining_symbols} symbols left")

    # Convert the binary list to a string and display the final result
    final_data_string = "".join(binary_list)
    print(f'Final data string:\n{final_data_string}')


if __name__ == "__main__":
    main()
