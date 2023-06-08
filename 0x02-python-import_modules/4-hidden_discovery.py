#!/usr/bin/python3
if __name__ == "__main__":

    """print all defined hidden_4 module names"""
    import hidden_4

    all_names = dir(hidden_4)
    for name in all_names:
        """if name[:2] != "__": is another way to write it"""
        if name[i][0] != "_" and name[i][1] != "_":
            print(name)
