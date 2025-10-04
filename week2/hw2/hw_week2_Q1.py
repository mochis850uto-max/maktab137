import re
import csv
import json

log_path = "server.log"
try:
    lines = []

    def read_log(log_path):
        with open(log_path, "r") as file:
            for line in file:
                print(line.strip())

    with open(log_path, "r") as file:
        for line in file:
            lines.append(line)

    read_log(log_path)

    pattern = re.compile(r"\[(.*?)\] \[(.*?)\] (.*)")

    with open('critical_errors.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Message"])

    counter = 1
    error_counter = 0
    notice_counter = 0
    for line in lines:
        try:
            match = pattern.match(line)
            timestamp, level, message = match.groups()

            if level == "error":
                with open('critical_errors.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([timestamp, message])
                error_counter += 1
            elif level == "notice":
                notice_counter += 1
                
        except AttributeError:
            with open('errors.log', 'a') as file:
                file.write(f"{counter}: {line}")
        counter += 1

    summary = {
        "Notice": notice_counter,
        "Error": error_counter,
    }

    with open('summary.json', 'w') as file:
        json.dump(summary, file, ensure_ascii=False, indent=4)

except FileNotFoundError:
    print("File not found.")