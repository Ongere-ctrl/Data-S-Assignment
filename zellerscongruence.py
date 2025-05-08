class DateCalculator:
    def __init__(self, year, month, day):
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12.")
        if not (1 <= day <= 31):
            raise ValueError("Day must be between 1 and 31.")


        if month < 3:
            month += 12
            year -= 1

        self.q = day
        self.m = month
        self.K = year % 100
        self.J = year // 100

    def calculate_weekday(self):
        q = self.q
        m = self.m
        K = self.K
        J = self.J

        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7

        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]


if __name__ == "__main__":
    calculator = DateCalculator(1589, 9, 15)
    print("Day of the week:", calculator.calculate_weekday())
