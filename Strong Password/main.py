import random
import string


if __name__ == "__main__":
    print("Strong Password Generator by Shubhayu Majumdar for Clinify-Open-Sauce")
    len = int(input(
        "Enter the length of your password.\nMinimum Length for a stong password is 8 characters\n>"))
    if len > 7:
        # Adding a space " " makes any password times stronger.
        char_set = string.ascii_lowercase + string.ascii_uppercase + \
            string.punctuation + string.digits + " "

        password = "".join(random.sample(char_set, len))

        print(f"Your strong password is: \"{password}\"")
    else:
        print("Length too short to generate Strong Password.\nPlease try again.")
