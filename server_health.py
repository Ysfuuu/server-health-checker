import psutil

print ("================================\n\tSERVER HEALTH CHECK\n================================")

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage("C:\\").percent

def check_status(value):
    if value >= 80:
        return "WARNING"
    else:
        return "OK"

cpu_status = check_status(cpu)
memory_status = check_status(memory)
disk_status = check_status(disk)


print(f"CPU Usage: {cpu}% - {cpu_status}")
print(f"Memory Usage: {memory}% - {memory_status}")
print(f"Disk Usage: {disk}% - {disk_status}")

if cpu_status=="WARNING" or memory_status=="WARNING" or disk_status=="WARNING":
    print("Overall Status: WARNING")
else:
    print("Overall Status: OK")



