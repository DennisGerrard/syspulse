import os
import platform
import uuid
import requests


class SystemCollector:
    """Gathers native Linux system details and remote network metadata."""

    @staticmethod
    def get_mac_address():
        """Reads active network interface MAC address from /sys/class/net/."""
        try:
            for interface in os.listdir("/sys/class/net/"):
                if interface != "lo":  # Skip loopback interface
                    addr_path = f"/sys/class/net/{interface}/address"
                    if os.path.exists(addr_path):
                        with open(addr_path, "r") as f:
                            mac = f.read().strip()
                            if mac and mac != "00:00:00:00:00:00":
                                return f"{interface} ({mac})"
        except Exception:
            pass
        return "Unavailable"

    @staticmethod
    def get_distro_info():
        """Reads /etc/os-release and cleanly strips all surrounding quotes."""
        if os.path.exists("/etc/os-release"):
            try:
                with open("/etc/os-release", "r") as f:
                    for line in f:
                        if line.startswith("PRETTY_NAME="):
                            # Extract value after '=' and remove quotes/whitespace
                            raw_val = line.split("=", 1)[1].strip()
                            return raw_val.strip('"\'')
            except Exception:
                pass
        return "Linux"

    @staticmethod
    def get_machine_id():
        """Extracts native Linux machine ID or falls back to system UUID node."""
        for path in ["/etc/machine-id", "/var/lib/dbus/machine-id"]:
            if os.path.exists(path):
                try:
                    with open(path, "r") as f:
                        mid = f.read().strip()
                        if mid:
                            return mid
                except Exception:
                    pass
        return str(uuid.getnode())

    @classmethod
    def get_local_info(cls):
        """Returns structured dictionary of local system metrics."""
        return {
            "OS Distro": cls.get_distro_info(),
            "Kernel": platform.release(),
            "Architecture": platform.machine(),
            "Hostname": platform.node(),
            "MAC Interface": cls.get_mac_address(),
            "Machine ID": cls.get_machine_id(),
        }

    @staticmethod
    def get_network_info():
        """Fetches external network details and IP geolocation metadata."""
        try:
            res = requests.get("http://ip-api.com/json/", timeout=5)
            if res.status_code == 200:
                data = res.json()
                if data.get("status") == "success":
                    return {
                        "Public IP": data.get("query"),
                        "ISP": data.get("isp"),
                        "Organization": data.get("org"),
                        "City": data.get("city"),
                        "Region": data.get("regionName"),
                        "Country": data.get("country"),
                        "Coordinates": f"{data.get('lat')}, {data.get('lon')}",
                    }
        except requests.RequestException:
            pass
        return {"Error": "Geolocation service unreachable"}