test = "/foo.txt"

if "foo.txt" in test:
    print("Yes")

if "poo.txt" in test:
    print("No it shouldnt be")
else:
    print("no")

value_split = test.rsplit('/', 1)[-1]
print(value_split)