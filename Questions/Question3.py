def sum_of_series(number):
    series = ""
    result = 0
    for i in range(number):
        series += "2"
        result += int(series)

    return result

print(sum_of_series(5))