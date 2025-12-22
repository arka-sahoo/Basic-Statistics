import statistics

def find_mean(data):
    return statistics.mean(data)

def find_median(data):
    return statistics.median(data)

def find_mode(data):
    try:
        return statistics.mode(data)
    except statistics.StatisticsError:
        return "No unique mode found"

def find_variance(data):
    return statistics.variance(data)

def find_standard_deviation(data):
    return statistics.stdev(data)