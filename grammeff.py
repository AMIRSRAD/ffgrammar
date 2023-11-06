def checklambda(lines): #checks lines and finds chars which contain lambdas

    lambda_list= []

    for line in lines:
        for i, char in enumerate(line):
            if char == '>' and line[i+1] == '.':
                lambda_list.append(line[i - 1])

    return lambda_list

def findfirst(uniqechar, lines, lambdas):
    first_list = []
    first_list_r = [] #non repeated

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


    [first_list_r.append(item) for item in first_list if item not in first_list_r] #remove repeated
    return first_list_r

def findfollow(uniqechar, lines, lambdas):
    follow_list = []
    follow_list_r = [] #non repeated

    for line in lines:
        for i, char in enumerate(line):
                if i + 1 < len(line) and line[i] == uniqechar and i>=2:
                    if i + 1 < len(line) and line[i+1].isupper():
                        follow_list.append(findfirst(line[i+1], lines, lambdas))
                    elif i + 1 < len(line) and line[i+1].islower():
                        follow_list.append(line[i+1])
                    else:
                        follow_list.append(findfollow(line[0], lines, lambdas))

    [follow_list_r.append(item) for item in follow_list if item not in follow_list_r] #remove repeated
    return follow_list_r

def main():
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

    for line in lines:              #find every beginning character of grammar
        if line:  # Checks if the line is not empty
            first_character = line[0]
            unique_first_characters_list.append(first_character)


    new_list = []

    [new_list.append(item) for item in unique_first_characters_list if item not in new_list] # removes dup of  beginning characters

    print(lines) # every grammar line

    print(new_list) # beginning characters

    print("\n")

    for i, item in enumerate(new_list):
        print("First of ", item," is :")
        first=findfirst(new_list[i],lines,checklambda(lines))
        if item in checklambda(lines):
            first.append('λ') # adds λ's to first's if any
        print(first)

    print("\n")

    for j, item1 in enumerate(new_list):
        print("Follow of ", item1," is :")
        follow=findfollow(new_list[j],lines,checklambda(lines))
        follow.append("$")     # adds $ to follow's
        print(follow)


main()