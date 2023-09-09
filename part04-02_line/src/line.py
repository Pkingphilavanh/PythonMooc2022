# Write your solution here

def line(size, string):
    if string == "":
        for x in range(size):
            print("*", end ="")
    elif len(string) > 0:
        print(string[0]*size, end = "")
    else:
        print("args invalid!")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")