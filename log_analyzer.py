def analyze_log(file_name):
    failed_attempts = 0
    successful_logins = 0

    try:
        with open(file_name, "r") as file:
            for line in file:
                if "FAILED LOGIN" in line:
                    failed_attempts += 1
                elif "LOGIN SUCCESS" in line:
                    successful_logins += 1

        print("\n===== Log Analysis Report =====")
        print(f"Total Failed Login Attempts: {failed_attempts}")
        print(f"Total Successful Logins: {successful_logins}")

        if failed_attempts > 3:
            print("⚠ Warning: High number of failed login attempts detected!")

    except FileNotFoundError:
        print("Error: Log file not found.")


if __name__ == "__main__":
    log_file = input("Enter log file name: ")
    analyze_log(log_file)
