def del_implement(dictt, key):
    if key in dictt:
        del dictt[key]
        print(f"da xoa {key} khoi dict.")
    else:
        print(f"{key} khong ton tai trong dict.")


my_dict = {"a": 1, "b": 2, "c": 3}
key_to_delete = "b"
del_implement(my_dict, key_to_delete)
print("Dict sau khi xoa:", my_dict)
