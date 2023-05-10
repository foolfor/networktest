def cmd_contain(
        full_str,
        sub_str
):
    try:
        full_str.index(sub_str)
        return True
    except ValueError:
        return False
