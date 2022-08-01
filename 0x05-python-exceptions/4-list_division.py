#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nlist = list()
    i = 0
    for num in range(list_length):
        try:
            j = my_list_1[i] / my_list_2[i]
            nlist.append(j)
        except ZeroDivisionError:
            print("division by 0")
            nlist.append(0)
        except (TypeError, NameError):
            print("wrong type")
            nlist.append(0)
        except IndexError:
            print("out of range")
            nlist.append(0)
        finally:
            i += 1
    return nlist
