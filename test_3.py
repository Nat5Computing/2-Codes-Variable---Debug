import subprocess

def test_debug3():
    try:
        result = subprocess.run(["python3", "3Debug.py"], capture_output=True, text=True)
        output = result.stdout.lower()  # make comparison case-insensitive

        checks = {
            "welcome to": "✅ Welcome message displayed.",
            "pupil name": "✅ Pupil name displayed.",
            "pupil age": "✅ Pupil age displayed."
        }

        success = True
        for phrase, message in checks.items():
            if phrase in output:
                print(message)
            else:
                print(f"❌ Missing or incorrect: {message[2:].replace('✅', '').strip()}")
                success = False

        if success:
            print("\n🎉 All key messages were printed correctly. Well done!")
        else:
            print("\n🔍 Check your print statements carefully and try again.")
    except Exception as e:
        print("❌ Your code crashed. Check for missing quotation marks, brackets, or typos.")
        print("Error:", e)

if __name__ == "__main__":
    test_debug3()
