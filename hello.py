# NAME:         Giovanni Rosati
# ASSIGNMENT:   Project 1

# Example
def hello_world():
    return "Hello World!"

# 1
def squared_sum(array):
    sum = 0
    for int in array:
        sum += int * int
    return sum

# 2
def mix(a, b):
    combined_list = []
    if len(a) >= len(b):
        for i in range(len(a)):
            combined_list.append(a[i])
            if i < len(b):
                combined_list.append(b[i])
    else:
        for i in range(len(b)):
            if i < len(a):
                combined_list.append(a[i])
            combined_list.append(b[i])
    combined_string = "".join(combined_list) 
    return combined_string

def main():
    print("squared sum: ", squared_sum([-3, 4]))
    print("mix:         ", mix("1234", "abcd") == "1a2b3c4d")

main()
