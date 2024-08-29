#Write a function that checks if a given string is a valid email address.


def is_valid_email(email):

    if "@" not in email:
        return False

    local_part, domain_part = email.split("@", 1)

    if not local_part or not domain_part:
        return False

    if "." not in domain_part:
        return False

    return True

email1 = "example@example.com"
email2 = "invalid-email"

print(f"{email1} is valid: {is_valid_email(email1)}")
print(f"{email2} is valid: {is_valid_email(email2)}")
