import subprocess

def test_debug1():
    try:
        result = subprocess.run(["python3", "1Debug.py"], capture_output=True, text=True)
        output = result.stdout.strip().lower()

        if "most instagrammed food" in output and "pizza" in output:
            print("✅ Message printed correctly about the most Instagrammed food.")
        else:
            print("❌ The message about the most Instagrammed food wasn't printed.")
            print("👉 Output was:", repr(output))
    except Exception as e:
        print("❌ Your code crashed. Check for missing quotation marks or typos.")
        print("Error:", e)

if __name__ == "__main__":
    test_debug1()
