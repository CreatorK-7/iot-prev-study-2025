# for 문 : 프로그래밍의 꽃!

# range(9) => 0,1,2,3,4,5,6,7,8 배열: 0부터 시작해 9-1까지 배열
print(range(9))

for i in range(1,9): # for문 흐름제어로 들어간다
    print(i, end='\t') # \n 한줄 내림 end 인자로 출력 끝을 조정

# 1부터 10까지의 합 : 55
sum = 0
for i in range(1,10):
    sum = sum + i

print(sum)

sum = 0
for i in range(1, 10, 2):
    print(i)