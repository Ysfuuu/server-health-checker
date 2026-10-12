import psutil

print ("================================\n\tSERVER HEALTH CHECK\n================================")

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage("C:\\").percent

resources = {
    "CPU": cpu,
    "Memory": memory,
    "Disk": disk
}


def check_status(value):
    if value >= 90:
        return "CRITICAL"
    elif 80 <= value < 90:
        return "WARNING"
    else:
        return "OK"


resource_status = [check_status(value) for value in resources.values()]


for name, value in resources.items():
    print(f"{name}: {value:.1f}% {check_status(value)}")
    


if "CRITICAL" in resource_status:
    print("Overall Status: CRITICAL")
elif "WARNING" in resource_status:
    print ("Overall Status: WARNING")
else:
    print("Overall Status: OK")



