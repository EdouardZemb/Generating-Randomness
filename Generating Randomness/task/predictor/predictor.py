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

    print("""You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!\n""")
    remaining_cash = 1000

    while remaining_cash > 0:
        test_input = fetch_test_data()
        if test_input == "enough":
            break
        else:
            test_input = filter_binary_characters(test_input)

        predictions = predict_next_characters(test_input, triad_freq)

        correct, total, accuracy = evaluate_accuracy(test_input, predictions)

        computer_wins = correct
        player_wins = total - correct
        if computer_wins > player_wins:
            remaining_cash -= computer_wins - player_wins
        elif computer_wins < player_wins:
            remaining_cash += player_wins - computer_wins

        print(f"predictions:\n{predictions}")
        print(f"Computer guessed {correct} out of {total} symbols right ({accuracy:.2f} %)")
        print(f"Your balance is now ${remaining_cash}")
        print()

    print("Game over!")


def fetch_random_data():
    # Initialize an empty list to store the binary digits
    binary_list = []
    # Continue fetching input until the list reaches the desired length
    print("Please provide AI some data to learn...\nThe current data length is 0, 100 symbols left")
    while len(binary_list) < MIN_LENGTH:
        user_input = input("Print a random string containing 0 or 1:\n")
        filtered_input = filter_binary_characters(user_input)

        # Extend the binary list with the filtered input
        binary_list.extend(filtered_input)

        # Calculate and display the remaining symbols needed
        remaining_symbols = MIN_LENGTH - len(binary_list)
        print(f"The current data length is {len(binary_list)}, {remaining_symbols} symbols left")
    # Convert the binary list to a string and display the final result
    final_data_string = "".join(binary_list)
    return final_data_string


def fetch_test_data():
    test_input = ""
    while len(test_input) < 4:
        test_input = input("Print a random string containing 0 or 1:\n")
    return test_input


if __name__ == "__main__":
    main()
