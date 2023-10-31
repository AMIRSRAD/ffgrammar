def checklambda(lines):

    lambda_list= []

    for line in lines:
        for i, char in enumerate(line):
            if char == '>' and line[i+1] == '.':
                lambda_list.append(line[i - 1])

    return lambda_list


def findfirst(uniqechar, lines, lambdas):
    first_list = []

    def recursive_search(uniqechar, current_lines):
        for line in current_lines:
            for i, char in enumerate(line):
                if line[0] == uniqechar:
                    if char == '>' and line[i + 1].islower():
                        first_list.append(line[i + 1])
                    elif line[0] == line[2]:
                        if line[0] in lambdas and line[i].islower():
                            first_list.append(line[i])
                        else:
                            continue
                    elif char == '>' and line[i + 1].isupper():
                        j = i+1; #checks for lamda
                        if line[j] in lambdas:
                            for j, char2 in enumerate(line):
                                if line[j] in lambdas and line[j+1].islower():
                                    first_list.append(line[j+1])
                                    break
                        recursive_search(line[i + 1], lines)


    recursive_search(uniqechar, lines)

    return first_list


user_input = ""
while True:
    partial_input = input("Enter a line of grammar (use (>) instead of arrows, use(.) instaed of lambda) (press 'q' to quit): ")
    if partial_input.lower() == 'q':
        break  # Exit the loop when 'q' is entered
    user_input += partial_input + "\n"


print("You entered:")

lines = user_input.split('\n')  # Split the string into lines using the newline character as the separator

unique_first_characters_list = []
lines.pop()

for line in lines:
    if line:  # Check if the line is not empty
        first_character = line[0]
        unique_first_characters_list.append(first_character)


new_list = []

[new_list.append(item) for item in unique_first_characters_list if item not in new_list]

print(lines)

print(new_list)

first_list = []

for i, item in enumerate(new_list):
    print("First of ", item," is :")
    print(findfirst(new_list[i],lines,checklambda(lines)))



