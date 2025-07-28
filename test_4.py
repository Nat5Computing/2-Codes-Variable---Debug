# test_4.py

import subprocess

expected_lines = [
    "Welcome to Hawkins High School",
    "Pupil name: Max Myles",
    "Pupil age: 15"
]

try:
    output = subprocess.check_output(["python3", "4Debug.py"], stderr=subprocess.STDOUT)
    output = output.decode("utf-8").strip().splitlines()
except subprocess.CalledProcessError as e:
    print("❌ Your program crashed. Check your code carefully.")
    print(e.output.decode("utf-8"))
    exit()

# Clean up the output (remove blank lines)
cleaned_output = [line.strip() for line in output if line.strip() != ""]

# Check for each expected message
results = []
for line in expected_lines:
    if any(line in actual for actual in cleaned_output):
        results.append(f"✅ {line}")
    else:
        results.append(f"❌ Missing or incorrect: {line}")

# Print results
print("\n".join(results))

if all(r.startswith("✅") for r in results):
    print("🎉 All key messages were printed correctly. Well done!")
else:
    print("🔍 Check your print statements carefully and try again.")
