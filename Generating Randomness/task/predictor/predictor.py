MIN_LENGTH = 100


def filter_binary(binary_string):
    return [x for x in binary_string if x in ["0", "1"]]


def fetch_user_input():
    return input("Print a random string containing 0 or 1:\n")


binary_list = filter_binary(fetch_user_input())

while len(binary_list) < MIN_LENGTH:
    print(f"Current data length is {str(len(binary_list))}, {str(MIN_LENGTH - len(binary_list))} symbols left")
    binary_list += filter_binary(fetch_user_input())

print(f'Final data string:\n{"".join(binary_list)}')
