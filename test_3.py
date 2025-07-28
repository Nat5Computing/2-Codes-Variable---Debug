import subprocess

def test_debug3():
    try:
        result = subprocess.run(["python3", "main.py"], capture_output=True, text=True)
        output = result.stdout.lower()

        checks = {
            "welcome to": "✅ Welcome message displayed.",
            "pupil name": "✅ Pupil name displayed.",
            "pupil age": "✅ Pupil age displayed."
        }

        for keyword, message in checks.items():
            if keyword in output:
                print(message)
            else:
                print(f"❌ Missing or incorrect: {keyword} not found in output.")

    except Exception as e:
        print("❌ Your program crashed. Check spelling of variable names and print statements.")
        print("Error:", e)

if __name__ == "__main__":
    test_debug3()
