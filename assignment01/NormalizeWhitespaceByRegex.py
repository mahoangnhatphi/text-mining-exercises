import re

def normalize_whitespace_regex(input_string):
    # Use regular expression to remove whitespace at the beginning and end
    trimmed_string = re.sub(r'^\s+|\s+$', '', input_string)

    # Normalize whitespace between words using regular expression substitutions
    normalized_string = re.sub(r'\s+', ' ', trimmed_string)

    return normalized_string


# Example usage:
input_text = "   This    is   a  sample   text.   "
result = normalize_whitespace_regex(input_text)
print(result)
