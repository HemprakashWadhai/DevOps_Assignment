import psutil
import time

# Define thresholds
CPU_THRESHOLD = 80  # Percent
MEMORY_THRESHOLD = 80  # Percent
DISK_THRESHOLD = 80  # Percent

# Function to check system health
def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    alerts = []

    # Check CPU usage
    if cpu_usage > CPU_THRESHOLD:
        alerts.append(f"High CPU usage: {cpu_usage}%")

    # Check memory usage
    if memory_info.percent > MEMORY_THRESHOLD:
        alerts.append(f"High memory usage: {memory_info.percent}%")

    # Check disk usage
    if disk_info.percent > DISK_THRESHOLD:
        alerts.append(f"High disk usage: {disk_info.percent}%")

    # Detailed status
    alerts.append(f"CPU Usage: {cpu_usage}%")
    alerts.append(f"Memory Usage: {memory_info.percent}%")
    alerts.append(f"Disk Usage: {disk_info.percent}%")

    return alerts

# Main function to log system health
def main():
    while True:
        alerts = check_system_health()
        if alerts:
            for alert in alerts:
                print(alert)  # Print alerts to console
                with open('system_health_log.txt', 'a') as log_file:
                    log_file.write(f"{time.ctime()}: {alert}\n")
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
