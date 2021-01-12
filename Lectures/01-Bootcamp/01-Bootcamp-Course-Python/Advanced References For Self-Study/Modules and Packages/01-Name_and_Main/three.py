import two

print("top-level in three.py")

two.one.func()

if __name__ == "__main__":
    print("three.py is being run directly")
else:
    print("three.py is being imported into another module")
