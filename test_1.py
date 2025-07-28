import subprocess

def test_debug1():
    try:
        result = subprocess.run(["python3", "main.py"], capture_output=True, text=True)
        output = result.stdout.strip().lower()

        if "instagrammed food" in output:
            print("✅ Message printed. Check for correct use of quotation marks and variable.")
        else:
            print("❌ The message about the most Instagrammed food wasn't printed.")
    except Exception as e:
        print("❌ Your code crashed. Did you spell print correctly and use quotes?")
        print("Error:", e)

if __name__ == "__main__":
    test_debug1()
