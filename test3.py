try:
    filename = input("nama file: ")
    handle = open(filename)
    total = 0
    for line in handle:
        total += len(line.strip())
        print(f"{total/1000} KB")
except:
    print("File tidak ditemukan!")