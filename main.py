# 1
l = []
for i in range(1, 31):
    l.append(i**2)
print(l)
# 2
exam_st_date = (11, 12, 2014)
print(f"Exam date is: {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}!")
# 3
s = input("Input some come separated numbers: ")
while "," in s:
    s = s.replace(",", " ")

s = s.split()
st = tuple(s)
print(s, st)
# 4
x = [1, 2, 3, 4]
y = [1, 5]

flag = False
for i in x:
    if flag is False:
        for j in y:
            if i == j:
                flag = True
                break
    else:
        break
if flag is True:
    print("There are same values")
else:
    print("There aren't any same values")
# 5
# tests
# [[10, 0], [3, 5], [5, 8]] Result is 5
# [[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]] Result is 17
# [[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]] Result is 21
l = [[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]
passengers = 0
for i in l:
    passengers += i[0]
    passengers -= i[1]
print(f"There is {passengers} sleepyheads")
