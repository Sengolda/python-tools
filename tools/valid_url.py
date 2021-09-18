import re

def check_url(url):
    is_real_url = (re.search(r"https?://(?:www\.)?.+", url))
    if is_real_url:
        return True
    else:
        return False