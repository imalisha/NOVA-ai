import psutil
import platform


class SystemMonitorService:

    def get_system_info(self):

        # CPU Usage
        cpu = psutil.cpu_percent(interval=None)

        # RAM Usage
        memory = psutil.virtual_memory()
        ram = memory.percent

        # Disk Usage
        disk = psutil.disk_usage("C:\\")
        disk_percent = disk.percent

        # Battery
        battery = psutil.sensors_battery()

        if battery is not None:

            battery_percent = int(battery.percent)

            if battery.power_plugged:
                power_status = "Charging"
            else:
                power_status = "On Battery"

        else:

            battery_percent = 0
            power_status = "Not Available"

        # Windows
        windows = platform.system()

        return {
            "cpu": cpu,
            "ram": ram,
            "disk": disk_percent,
            "battery": battery_percent,
            "power": power_status,
            "windows": windows
        }