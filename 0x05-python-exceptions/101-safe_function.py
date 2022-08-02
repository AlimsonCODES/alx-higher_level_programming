#!/usr/bin/python3
def safe_function(fct, *args):
    ans = None
    try:
        ans = fct(*args)
        return ans
    except Exception:
        sys.stderr.write("Exception: ")
        sys.stderr.write(err.args[0])
        sys.stderr.write("\n")
        return ans

