def letters():
    phrase= 'I love Costa Rica'

    lower_count= sum(char.islower()for char in phrase)
    upper_count= sum(char.isupper()for char in phrase)
    print(phrase)
    print(f"Number of lower {lower_count}")
    print(f"Number of upper {upper_count}")

letters()