import re

EMAIL_PATTERN = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)([\w\.]?)"


def check_email(email):
    is_real_email = re.search(EMAIL_PATTERN, email)
    if is_real_email:
        return True
    else:
        return False
