def first_character_type(pw):
    """Classify the first character of pw as 'digit', 'letter' or 'symbol'.

    Fixes: None / non-string input (TypeError) -> 'invalid';
           empty string (IndexError)           -> 'empty'.
    """
    if not isinstance(pw, str):
        return 'invalid'
    if pw == '':
        return 'empty'
    ch = pw[0]
    if ch.isdigit():
        return 'digit'
    if ch.isalpha():
        return 'letter'
    return 'symbol'


def split_credentials(text):
    """Split 'user:password' into (user, password).

    Fixes: None / non-string input (AttributeError) -> (None, None);
           no ':' present (ValueError: not enough values) -> (None, None);
           extra ':' in the password (ValueError: too many values)
           -> split only on the FIRST ':' so the password is preserved.
    """
    if not isinstance(text, str) or ':' not in text:
        return None, None
    user, password = text.split(':', 1)
    return user.strip(), password.strip()


def digit_ratio(pw):
    """Fraction of characters in pw that are digits (0.0 - 1.0).

    Fixes: None / non-string input (TypeError) -> 0.0;
           empty string (ZeroDivisionError)    -> 0.0.
    """
    if not isinstance(pw, str) or len(pw) == 0:
        return 0.0
    return sum(c.isdigit() for c in pw) / len(pw)


def main():
    print("==== Running first_character_type ====")
    user_input = input("Enter a password: ")
    result = first_character_type(user_input)
    print("First Character Type:", result)

    print("\n==== Running split_credentials ====")
    user_input = input("Enter user:password (e.g. alice:Secret1): ")
    result = split_credentials(user_input)
    if result == (None, None):
        print("Invalid format - expected user:password")
    else:
        print("User and Password:", result)

    print("\n==== Running digit_ratio ====")
    user_input = input("Enter a password to measure: ")
    result = digit_ratio(user_input)
    print("Digit Ratio:", result)


if __name__ == "__main__":
    main()
