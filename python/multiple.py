import math;
print('등비수열은 인접한 항의 비가 일정한 수열로, 인접한 항의 비를 공비라고 합니다. \n'
      '등비수열의 특정 항을 구하는 공식은 첫쨰항을 a_1, 공비를 r이라고 할 때 \n'
      'a_n = a_1 * r ** (n - 1) 입니다. \n'
      '또한 등차수열 n번째 항까지의 합 S_n은 다음과 같습니다. \n'
      'S_n = a_1 * (r ** n - 1) / r - 1');
a=int(input('등비수열의 첫번째 항을 입력해주세요. '));
r=int(input('등비수열의 공비를 입력해주세요. '));
n=int(input('등비수열의 알고 싶은 항의 순서를 입력해주세요(예: 10번째 항=10) '))
a_n=a*(r ** (n-1))
print(a_n)
S_n=a * ((r ** n) - 1) / (r - 1)
print(S_n)