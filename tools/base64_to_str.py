import base64

def base64_to_string(byt):
    return (base64.b64decode(byt)).decode()