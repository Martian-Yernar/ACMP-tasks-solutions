n = int(input())
c1, c2, c3, c4 = 0, 0, 0, 0 # 1 2 3 4 5 n=5

chars = []
l = list(map(int, input().strip().split()))[:n]

# l.append('d')
# print(l)
for i in range(len(l)-1):
  if l[i] > l[i+1]:
    chars.append(">")
  elif l[i] < l[i+1]:
    chars.append("<")

for i in range(0, len(chars)-2, 2):
    if chars[i] == '>' and chars[i+1] == '<':
        c4 += 1
    

if chars[-2] == '>' and chars[-1] == '<':
   c4 += 1

# print(chars)

# if chars:
#     for i in range(len(chars)):
#         if chars[i] == ">":
#             c4 += 1
#             chars.remove(chars[i])
#             if chars:
#                 for j in range(i+1, len(chars)):
#                     if chars[j] == "<":
#                         c4 += 1
#                         chars.remove(chars[j])
#                         if chars:
#                             for k in range(j+1, len(chars)):
#                                 if chars[k] == ">":
#                                     c4 += 1
#                                     chars.remove(chars[k])
#                                     if chars:
#                                         for m in range(k+1, len(chars)):
#                                             if chars[m] == "<":
#                                                 c4 += 1
#                                                 chars.remove(chars[m])
               
# if chars:
#     for i in range(len(chars)):
#         if chars[i] == ">":


    

print(c4+1) # 1 -2 3 -4 5
                  
                
                


        
    


    


# for i in range(1, len(l)-4, 2):
#   if l[i] > l[i-1] and l[i] > l[i+1]:
#     c1 += 1
#     c2 += 1
#   elif l[i] < l[i-1] and l[i] < l[i+1]:
#     c3 += 1
#     c4 += 1

# if l[-1] > l[-2] and l[-2] < l[-3]:
#   c1 += 1
#   c4 += 1
# elif l[-1] < l[-2] and l[-2] > l[-3]:
#   c2 += 1
#   c3 += 1

# print(max(c1, max(c2, max(c3, c4))))
  