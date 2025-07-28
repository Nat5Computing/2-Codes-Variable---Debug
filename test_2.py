import subprocess

def test_debug2():
    try:
        result = subprocess.run(["python3", "main.py"], capture_output=True, text=True)
        output = result.stdout.strip().lower()

        if "disney" in output:
            if "favourite" in output:
                print("✅ Your program printed something about your favourite Disney movie.")
            else:
                print("⚠️ Output found but check that you're using variables, not just text.")
        else:
            print("❌ Your output didn’t mention any Disney movie.")
    except Exception as e:
        print("❌ Your code crashed. Did you forget quotation marks or use the wrong variable name?")
        print("Error:", e)

if __name__ == "__main__":
    test_debug2()
