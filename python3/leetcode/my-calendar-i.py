class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> int:
        left, right, idx = 0, len(self.calendar) - 1, len(self.calendar)
        while left <= right:
            mid = (left + right) // 2
            if self.calendar[mid][0] > start:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1

        if (idx > 0 and self.calendar[idx - 1][1] > start) or (
                idx < len(self.calendar) and self.calendar[idx][0] < end):
            return False
        self.calendar.insert(idx, (start, end))
        return True


cal = MyCalendar()
print(cal.book(10, 20))
print(cal.book(15, 25))
print(cal.book(20, 30))
print(cal.calendar)
