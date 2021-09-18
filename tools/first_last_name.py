def check_first_last_name(name):
    name = (name.strip()).split()
    first_last = None

    if len(name) > 1:
        first = name[0]
        last = " ".join(name[-1:])
        if last == first or last == "":
            first_last = first
        else:
            first_last = first + " " + last

    return first_last
