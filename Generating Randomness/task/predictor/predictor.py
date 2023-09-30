import random
from collections import defaultdict, Counter

# Define the minimum required length for the binary string
MIN_LENGTH = 100


def filter_binary_characters(data):
    # Filter out characters that are not '0' or '1'
    return [char for char in data if char in ["0", "1"]]


def calculate_triad_frequencies(data):
    # Initialize a dictionary to store the triad frequencies
    triad_freq = defaultdict(Counter)
    # Iterate over the data string and count the frequencies of each triad
    for i in range(len(data) - 3):
        triad = data[i:i + 3]
        next_char = data[i + 3]
        triad_freq[triad][next_char] += 1
    # Sort the triad frequencies in alphabetical order
    return dict(sorted(triad_freq.items()))


def calculate_probabilities(triad, triad_freq):
    if triad in triad_freq:
        # Calculate probabilities once
        total_count = triad_freq[triad]['0'] + triad_freq[triad]['1']
        probability_0 = triad_freq[triad]['0'] / total_count
        probability_1 = triad_freq[triad]['1'] / total_count
        return probability_0, probability_1
    else:
        # Handle triads not in the frequencies dictionary
        return None, None


def predict_next_characters(test_string, triad_freq):
    predictions = []
    for i in range(3, len(test_string)):
        triad = "".join(test_string[i - 3:i])
        probability_0, probability_1 = calculate_probabilities(triad, triad_freq)

        if probability_0 is not None and probability_1 is not None:
            if probability_0 > probability_1:
                predictions.append('0')
            elif probability_0 < probability_1:
                predictions.append('1')
            else:
                # In case of a tie, choose at random
                predictions.append(random.choice(['0', '1']))
        else:
            # Handle triads not in the frequencies dictionary
            predictions.append(random.choice(['0', '1']))

    return ''.join(predictions)


def evaluate_accuracy(test_string, predictions):
    correct = sum([1 for i in range(len(predictions)) if test_string[i+3] == predictions[i]])
    total = len(predictions)
    accuracy = (correct / total) * 100
    return correct, total, accuracy


def main():
    final_data_string = fetch_random_data()
    print(f'Final data string:\n{final_data_string}')

    # Calculate and display the triad counts
    triad_freq = calculate_triad_frequencies(final_data_string)

    test_input = fetch_test_data()

    predictions = predict_next_characters(test_input, triad_freq)

    correct, total, accuracy = evaluate_accuracy(test_input, predictions)

    print(f"predictions:\n{predictions}")
    print(f"Computer guessed right {correct} out of {total} symbols ({accuracy:.2f} %)")


def fetch_random_data():
    # Initialize an empty list to store the binary digits
    binary_list = []
    # Continue fetching input until the list reaches the desired length
    while len(binary_list) < MIN_LENGTH:
        user_input = input("Print a random string containing 0 or 1:\n")
        filtered_input = filter_binary_characters(user_input)

        # Extend the binary list with the filtered input
        binary_list.extend(filtered_input)

        # Calculate and display the remaining symbols needed
        remaining_symbols = MIN_LENGTH - len(binary_list)
        print(f"Current data length is {len(binary_list)}, {remaining_symbols} symbols left")
    # Convert the binary list to a string and display the final result
    final_data_string = "".join(binary_list)
    return final_data_string


def fetch_test_data():
    test_input = ""
    while len(test_input) < 4:
        test_input = input("Please enter a test string containing 0 or 1:\n")
    return filter_binary_characters(test_input)


if __name__ == "__main__":
    main()
