info_count = 0
error_count = 0

with open("sample.log", "r") as file:
    for line in file:

        if "INFO" in line:
            info_count += 1

        elif "ERROR" in line:
            error_count += 1

print("=" * 40)
print("ADVANCED LOG ANALYZER")
print("=" * 40)

print(f"INFO Entries : {info_count}")
print(f"ERROR Entries: {error_count}")

print("=" * 40)
