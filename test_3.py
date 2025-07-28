import subprocess

def test_debug3():
    try:
        result = subprocess.run(["python3", "3Debug.py"], capture_output=True, text=True)
        output = result.stdout

        checks = {
            "Welcome to": "✅ Welcome message displayed.",
            "Pupil name:": "✅ Pupil name displayed.",
            "Pupil age:": "✅ Pupil age displayed."
        }

        failed_messages = {
            "Welcome to": "❌ Missing or incorrect: Welcome message not found.",
            "Pupil name:": "❌ Missing or incorrect: Pupil name not found in output.",
            "Pupil age:": "❌ Missing or incorrect: Pupil age not found in output."
        }

        print()
        passed = 0

        for phrase in checks:
            if phrase in output:
                print(checks[phrase])
                passed += 1
            else:
                print(failed_messages[phrase])

        print()

        if passed == len(checks):
            print("🎉 All key messages were printed correctly. Well done!")
        elif passed == 0:
            print("🔍 None of the key outputs were correct. Review all print statements.")
        else:
            print(f"🔧 {passed} out of {len(checks)} messages printed correctly. Keep going!")

    except Exception as e:
        print("💥 Your program crashed before finishing.")
        print("🔎 Tip: Check for missing brackets, quotes, or typos.")
        print("Error:", e)

if __name__ == "__main__":
    test_debug3()
