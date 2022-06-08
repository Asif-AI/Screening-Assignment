# Open a file
with open("demo.txt", "r") as f:
    file = f.read()


# Replace string
file = file.replace("placement", "screening")

# write a file
with open("demo.txt", "w") as f:
    file = f.write(file)    

