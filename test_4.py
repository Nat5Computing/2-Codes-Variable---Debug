import subprocess

def test_debug4():
    try:
        result = subprocess.run(["python3", "main.py"], capture_output=True, text=True)
        output = result.stdout.lower()

        if "welcome to" in output and "hawkins" not in output:
            print("❌ Welcome message is using the wrong variable (age instead of school).")
        else:
            print("✅ Welcome message is correct.")

        if "pupil name" in output and "max" not in output:
            print("❌ Pupil name is incorrect (check variables used).")
        else:
            print("✅ Pupil name is correct.")

    except Exception as e:
        print("❌ Your code crashed. Check you’re using variables correctly.")
        print("Error:", e)

if __name__ == "__main__":
    test_debug4()
