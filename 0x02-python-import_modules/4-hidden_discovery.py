#!/usr/bin/python3
if __name__ == "__main__":

    """print all defined hidden_4 module names"""
    import hidden_4

    names = dir(hidden_4)

    for name in names:
        if name[:2] is not "__":
            print(name)
