import json

with open("benchmark.json") as f:
    benchmarks = json.load(f)


def evaluate_report(parsed_data):
    final_report = []

    for item in parsed_data:
        test = item["test"]
        value = item["value"]

        if test not in benchmarks:
            continue

        low = benchmarks[test]["low"]
        high = benchmarks[test]["high"]

        if value < low:
            status = "Low"
        elif value > high:
            status = "High"
        else:
            status = "Normal"

        final_report.append({
            "test": test,
            "value": value,
            "status": status
        })

    return final_report
#...