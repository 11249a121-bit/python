S = input("Enter the digit")
for d in ("0123456789"):
    C = S.count(d)
    if C:
        print(d,":",C)
