i = 1

while i <= 7:
    print(i)
    i += 1
print("끝!")


s = "programming"
count = 0
for ch in s:
if ch in "aeiou":
count += 1
print(count) # 3


for i in range(2, 21, 2):
print(i)
    또는 if 사용
for i in range(1, 21):
    if i % 2 == 0:
        print(i)