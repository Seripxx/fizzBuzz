class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        

        for i in range(1, n+1):
            divisibleby3 = (i % 3) == 0
            divisibleby5 = (i % 5) == 0

            current_str = ""

            if divisibleby3 and divisibleby5:
                current_str = "FizzBuzz"
            elif divisibleby3:
                current_str = "Fizz"
            elif divisibleby5:
                current_str = "Buzz"
            else:
                current_str = str(i)

            answer.append(current_str)

        return answer

