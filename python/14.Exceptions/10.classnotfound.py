#Python does not have ClassNotFoundException but we can write as
try:
    import sample
except ModuleNotFoundError:
    print("===class or module not found===")
