class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(1, 1 + n):
            if i % 5 ==0 and i % 3 == 0:
                answer.append('FizzBuzz')
            elif i % 5 == 0:
                answer.append('Buzz')
            elif i % 3 == 0:
                answer.append('Fizz')
            else:
                answer.append(str(i))

        return answer