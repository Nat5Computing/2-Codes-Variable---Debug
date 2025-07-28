import subprocess

def test_debug2():
    try:
        result = subprocess.run(["python3", "2Debug.py"], capture_output=True, text=True)
        output = result.stdout.strip().lower()

        if "disney movie" in output and "big hero 6" in output:
            print("✅ Message printed correctly about the Disney movie.")
        else:
            print("❌ Your output didn’t mention any Disney movie.")
            print("👉 Output was:", repr(output))
    except Exception as e:
        print("❌ Your code crashed. Check for typos or errors.")
        print("Error:", e)

if __name__ == "__main__":
    test_debug2()
