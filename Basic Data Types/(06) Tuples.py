# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
int_list = map(int, input().split())
t = tuple(int_list)
print(hash(t))
