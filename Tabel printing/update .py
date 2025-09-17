
# print welcome to my Tabel printing program
print("Welcome to my Tabel printing progrma")


# Write a logic  program
while True:
    try:
        #input Tabel number name
        tabel_name = input("Enter your Tabel name Stop for S :")
        if tabel_name =="s":
            print("Program is Break")
            break
        else:
            for tabel in range(1,11):
                print(f"{tabel_name} X {tabel } = {tabel * int(tabel_name)} ")
    except ValueError as t:
        print("Enter number not string and others...")

