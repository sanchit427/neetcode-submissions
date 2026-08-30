class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = {}

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        max_freq = max(freq.values())

        max_count = 0

        for count in freq.values():
            if count == max_freq:
                max_count += 1

        answer = (max_freq - 1) * (n + 1) + max_count

        return max(answer, len(tasks))