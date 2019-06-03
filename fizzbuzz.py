def fizzbuzz(num):
    output = []
    for i in range(1, num+1):
        element = ""
        if not i % 3:
            element += "fizz"
        if not i % 5:
            element += "buzz"
        if element == "":
            element = i
        output.append(element)
    return output

def fizzbuzz2(num):
    return ["fizzbuzz" if not i%3 and not i%5 else "fizz" if not i%3 else "buzz" if not i%5 else i for i in range(1,num+1)]

def fizzbuzz3(num):
    dic = {3: "fizz", 5: "buzz"}
    output = []
    for i in range(1, num+1):
        element = ""
        for key, value in dic.items():
            if i % key == 0:
                element += value
        if element == "":
            element = i
        output.append(element)
    return output

print(fizzbuzz(20))
print(fizzbuzz2(20))
print(fizzbuzz3(20))