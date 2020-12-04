from aoc.helpers import io


tests = []
def read(line):
    if line == "":
        return

    line_input = line.replace("\n","").split(" ")

    policy_range = line_input[0].split("-")
    min_char_policy = policy_range[0].strip()
    max_char_policy = policy_range[1].strip()
    policy_letter = line_input[1].replace(":","").strip()
    password = line_input[2].strip()
    
    try:
        tests.append({
            'min_char_policy': int(min_char_policy),
            'max_char_policy': int(max_char_policy),
            'policy_letter': policy_letter,
            'password': password
        })
    except TypeError:
        return

io.read_file_by_newline('./day2.txt', read)

valid_pass_count = 0
for test in tests:
    char_count = test['password'].count(test['policy_letter'])
    if char_count >= test['min_char_policy'] and char_count <= test['max_char_policy']:
        valid_pass_count = valid_pass_count + 1

valid_pass_count = 0
for test in tests:
    start_idx = test['min_char_policy']-1
    end_idx = test['max_char_policy']-1
    password = test['password']
    test_char = test['policy_letter']

    if password[start_idx] == test_char and password[end_idx] != test_char:
        valid_pass_count = valid_pass_count + 1
    elif password[start_idx] != test_char and password[end_idx] == test_char:
        valid_pass_count = valid_pass_count + 1

print("Valid Password Count: ", valid_pass_count)