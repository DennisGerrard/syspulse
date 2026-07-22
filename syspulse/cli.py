import json
import argparse
from syspulse.collector import SystemCollector
from syspulse.formatter import display_dashboard

def main():
    parser = argparse.ArgumentParser(description="SysPulse - System & Network Extractor")
    parser.add_argument("--json", action="store_true", help="Print raw JSON output")
    parser.add_argument("--export", type=str, help="Save report to JSON file path")
    args = parser.parse_args()

    local = SystemCollector.get_local_info()
    network = SystemCollector.get_network_info()
    combined = {"local": local, "network": network}

    if args.export:
        with open(args.export, "w") as f:
            json.dump(combined, f, indent=2)
        print(f"[+] System report exported successfully to: {args.export}")
        return

    if args.json:
        print(json.dumps(combined, indent=2))
    else:
        display_dashboard(local, network)

if __name__ == "__main__":
    main()
