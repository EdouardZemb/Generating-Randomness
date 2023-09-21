# Define the minimum required length for the binary string
MIN_LENGTH = 100


def filter_binary(binary_string):
    # Filter out characters that are not '0' or '1'
    return [x for x in binary_string if x in ["0", "1"]]


def fetch_user_input():
    # Get user input as a binary string
    return input("Print a random string containing 0 or 1:\n")


def calculate_triad_counts(binary_string):
    triad_dict = {}

    for i in range(len(binary_string) - 3):
        triad = binary_string[i:i + 3]
        if triad not in triad_dict:
            triad_dict[triad] = {"0": 0, "1": 0}

        triad_dict[triad][binary_string[i + 3]] += 1

    return triad_dict


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

    # Calculate and display the triad counts
    triad_dict = calculate_triad_counts(final_data_string)
    triad_dict = {k: v for k, v in sorted(triad_dict.items(), key=lambda item: item[0])}

    for k in triad_dict:
        zero_count = triad_dict[k]["0"]
        one_count = triad_dict[k]["1"]
        print(f"{k}: {zero_count},{one_count}")


if __name__ == "__main__":
    main()
