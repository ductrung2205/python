def fibonacci(n):
    if (n == 0 or n == 1):
        return n;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2);
 
n = -1 
while n <= 0:
    n = int(input("Nhập số tự nhiên n: "))
    if(n >= 0):
        break
result = fibonacci(n)
print(result)
#bài 1
input_str = '['
output = input_str[1, -1]
output = output.split(',')
output = [(int(s).strip()) for s in output]
print (output, type(output))


eval