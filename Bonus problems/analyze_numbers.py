def analyze_numbers(numbers: list[int | float]) -> dict:
    """
    Takes a list of numbers and returns basic stats about them.
    """
    if not numbers:
        return {"error": "Empty list provided"}

    sorted_nums = sorted(numbers)
    total = sum(numbers)
    count = len(numbers)
    mean = total / count

    mid = count // 2
    if count % 2 == 0:
        median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        median = sorted_nums[mid]

    return {
        "count": count,
        "sum": total,
        "mean": round(mean, 2),
        "median": median,
        "min": sorted_nums[0],
        "max": sorted_nums[-1],
        "range": sorted_nums[-1] - sorted_nums[0],
    }


# Example usage
data = [4, 7, 2, 19, 3, 8, 15, 1]
result = analyze_numbers(data)
print(result)
# {'count': 8, 'sum': 59, 'mean': 7.38, 'median': 5.5, 'min': 1, 'max': 19, 'range': 18}
