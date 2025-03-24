def calculate_monthly_interest(balance: float, years: int) -> float:
    """
    Calculate the monthly interest earned.

    :param balance: Initial savings balance
    :param years: Number of years (1-year: 3.8%, 2-year: 3.6%)
    :return: Monthly interest earned
    """
    rate = 0.038 if years == 1 else 0.036
    annual_interest = balance * rate
    return annual_interest / 12  # Monthly interest

# Example:
print(calculate_monthly_interest(1000, 1))  # For one-year
print(calculate_monthly_interest(1000, 2))  # For two-year


#Tax paid for annual income
def calculate_income_tax(income: float) -> float:
    tax = 0.0

    if income > 125140:
        tax += (income - 125140) * 0.45
        income = 125140

    if income > 50270:
        tax += (income - 50270) * 0.40
        income = 50270

    if income > 12570:
        tax += (income - 12570) * 0.20

    return tax


def degree_classification(marks: list, credits: list) -> str:
    """
    Determines the degree classification based on module marks and credits.

    :param marks: List of module marks
    :param credits: Corresponding list of module credits
    :return: Degree classification (First, Upper Second, Lower Second, Third)
    """
    if len(marks) != len(credits):
        raise ValueError("Marks and credits must have the same length")

    lowest_20_credit_index = credits.index(min(credits))
    marks.pop(lowest_20_credit_index)
    credits.pop(lowest_20_credit_index)

    weighted_avg = sum(m * c for m, c in zip(marks, credits)) / sum(credits)

    if weighted_avg >= 70:
        return "First Class"
    elif weighted_avg >= 60:
        return "Upper Second Class"
    elif weighted_avg >= 50:
        return "Lower Second Class"
    elif weighted_avg >= 40:
        return "Third Class"
    else:
        return "Fail"

