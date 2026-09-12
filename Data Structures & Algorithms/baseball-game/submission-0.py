class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            if self.is_integer(operation):
                score = int(operation)
                record.append(score)
            elif operation == "+":
                prev_sum = record[-1] + record[-2]
                record.append(prev_sum)
            elif operation == "D":
                double = 2 * record[-1]
                record.append(double)
            elif operation == "C":
                record.pop()

        sum_of_scores = sum(record)

        return sum_of_scores

    def is_integer(self, val: str) -> bool:
        try:
            int(val)
            return True
        except ValueError:
            return False