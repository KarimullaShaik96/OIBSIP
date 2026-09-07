import json


class Firewall:

    def __init__(self, rules_file):
        self.rules = self.load_rules(rules_file)

    # Load firewall rules from JSON file
    def load_rules(self, rules_file):
        try:
            with open(rules_file, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            print("Error: Firewall rules file not found.")
            return []

        except json.JSONDecodeError:
            print("Error: Invalid JSON format.")
            return []

    # Check whether a packet should be ALLOWED or BLOCKED
    def check_packet(self, ip, port, protocol):

        protocol = protocol.upper()

        for rule in self.rules:

            ip_match = (
                rule["ip"] == "*"
                or rule["ip"] == ip
            )

            port_match = (
                rule["port"] == "*"
                or rule["port"] == port
            )

            protocol_match = (
                rule["protocol"] == "*"
                or rule["protocol"].upper() == protocol
            )

            if ip_match and port_match and protocol_match:
                return rule["action"].upper()

        # Default firewall policy
        return "BLOCK"

    # Save packet decision to log file
    def log_packet(self, ip, port, protocol, action):

        with open("firewall_log.txt", "a") as log_file:

            log_file.write(
                f"IP: {ip} | "
                f"Port: {port} | "
                f"Protocol: {protocol.upper()} | "
                f"Action: {action}\n"
            )


def main():

    firewall = Firewall("firewall_rules.json")

    print("=" * 60)
    print("              OIBSIP FIREWALL SIMULATOR")
    print("=" * 60)

    while True:

        print("\nEnter network packet details")
        print("Type 'exit' as the IP address to stop.")

        # Get IP address
        ip = input("IP Address: ").strip()

        # Exit option
        if ip.lower() == "exit":

            print("\nFirewall simulator stopped.")
            break

        # Get port
        port_input = input("Port: ").strip()

        # Get protocol
        protocol = input("Protocol (TCP/UDP): ").strip()

        # Validate port
        try:
            port = int(port_input)

        except ValueError:

            print("Invalid port. Please enter a number.")
            continue

        # Validate port range
        if port < 1 or port > 65535:

            print("Invalid port. Port must be between 1 and 65535.")
            continue

        # Validate protocol
        if protocol.upper() not in ["TCP", "UDP"]:

            print("Invalid protocol. Please enter TCP or UDP.")
            continue

        # Check firewall rule
        result = firewall.check_packet(
            ip,
            port,
            protocol
        )

        # Log packet
        firewall.log_packet(
            ip,
            port,
            protocol,
            result
        )

        # Display result
        print("\n" + "-" * 60)
        print(f"IP Address : {ip}")
        print(f"Port       : {port}")
        print(f"Protocol   : {protocol.upper()}")
        print(f"Firewall   : {result}")
        print("-" * 60)


if __name__ == "__main__":
    main()
