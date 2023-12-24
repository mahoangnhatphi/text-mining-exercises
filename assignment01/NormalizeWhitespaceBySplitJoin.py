def normalize_whitespace_split_join(input_string):
    # Remove leading and trailing whitespaces
    trimmed_string = input_string.strip()

    # Normalize whitespace between words using split() and join()
    normalized_string = ' '.join(trimmed_string.split())

    return normalized_string


# Example usage:
input_text = "   This    is   a  sample   text.   "
result = normalize_whitespace_split_join(input_text)
print(result)
