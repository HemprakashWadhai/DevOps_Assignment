from collections import Counter
import re

# Define the log file path
log_file_path = 'access.log'  # Ensure this path is correct

def parse_log_file(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()
    return logs

def count_404_errors(logs):
    return sum(1 for line in logs if '404' in line)

def most_requested_pages(logs):
    pattern = re.compile(r'\"GET (.+?) HTTP')
    pages = [pattern.search(line).group(1) for line in logs if pattern.search(line)]
    return Counter(pages).most_common()

def most_frequent_ips(logs):
    pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)')
    ips = [pattern.search(line).group(1) for line in logs if pattern.search(line)]
    return Counter(ips).most_common()

def analyze_logs(file_path):
    logs = parse_log_file(file_path)
    num_404_errors = count_404_errors(logs)
    requested_pages = most_requested_pages(logs)
    frequent_ips = most_frequent_ips(logs)

    print(f'Number of 404 Errors: {num_404_errors}')
    print('Most Requested Pages:')
    for page, count in requested_pages:
        print(f'{page}: {count}')
    print('Most Frequent IPs:')
    for ip, count in frequent_ips:
        print(f'{ip}: {count}')

if __name__ == "__main__":
    analyze_logs(log_file_path)
