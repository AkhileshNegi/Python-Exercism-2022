def is_valid(isbn):
    clean_isbn = isbn.replace("-", "")
    multiplier = 10
    total = 0
    if len(clean_isbn) != 10:
        return False
    for char in clean_isbn:
        if char.isdigit():
            total += int(char) * multiplier
            multiplier = multiplier - 1
        elif char == 'X' and multiplier == 1:
            total += 10
    if total % 11 == 0:
        return True
    else:
        return False
