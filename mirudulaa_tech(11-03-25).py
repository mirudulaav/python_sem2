def look_and_say(n):
    result = ["1"]
    for _ in range(n - 1):
        previous = result[-1]
        new_sequence = ""
        count = 1
        for j in range(1, len(previous)):
            if previous[j] == previous[j - 1]:
                count += 1
            else:
                new_sequence += str(count) + previous[j - 1]
                count = 1
        new_sequence += str(count) + previous[-1]
        result.append(new_sequence)
    return result
n = int(input("Enter the number of rows: "))
output = look_and_say(n)
for line in output:
    print(line)
