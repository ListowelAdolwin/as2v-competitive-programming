class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        
        operation = {
            '++X': 1,
            'X++': 1,
            '--X': -1,
            'X--': -1
        }

        for op in operations:
            print(op, operation[op])
            X += operation[op]

        return X