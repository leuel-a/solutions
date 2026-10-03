from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        def getHour(hours: List[bool]) -> int:
            return sum(hour for on, hour in zip(hours, [8, 4, 2, 1]) if on)

        def getMinute(minutes: List[bool]) -> int:
            return sum(hour for on, hour in zip(minutes, [32, 16, 8, 4, 2, 1]) if on)

        hour = [False, False, False, False]
        minute = [False, False, False, False, False, False]

        result = []

        # n -> the number of turned on LEDs
        # i -> the current index of hour LED
        # j -> the current index of minite LED
        def backtrack(n: int, i: int, j: int) -> None:
            if n > turnedOn:
                return

            if getHour(hour) >= 12 or getMinute(minute) >= 60:
                return

            if n == turnedOn:
                h, m = getHour(hour), getMinute(minute)
                result.append(f"{str(h)}:{str(m).zfill(2)}")
                return

            if i >= len(hour) or j >= len(minute):
                return

            hour[i] = True
            backtrack(n + 1, i + 1, j)
            hour[i] = False

            backtrack(n, i + 1, j)

            minute[j] = True
            backtrack(n + 1, i, j + 1)
            minute[j] = False

            backtrack(n, i, j + 1)

        backtrack(0, 0, 0)
        return list(set(result))

