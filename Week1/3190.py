n = int(input())
k = int(input())
apple_point = []
for i in range(k):
    apple_point.append(input().split())

l = int(input())
move_command = []
for i in range(l):
    move_command.append(input().split())


print( n ,'= n')
print( k ,'= k')
print( apple_point ,'= apple_point')
print(l, '= l')
print( move_command ,'= move_command')