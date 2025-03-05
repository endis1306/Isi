def find_substring_indexes(string, substring):
    parts = string.split(substring)
    if len(parts) == 1:
        return -1

    indexes = []

    index = 0
    for part in parts[:-1]:
        index += len(part)
        indexes.append(index)
        index += len(substring)

    return indexes

string = "abcbabcaa5ttg3abcbcbabc"
substring = "abc"
result = find_substring_indexes(string, substring)

if result == -1:
    print("Substring nie występuje w łańcuchu.")
else:
    print("Indeksy wystąpień substringu:", result)
