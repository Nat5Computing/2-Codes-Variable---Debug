# test_4.py

import ast

# Load student's code
filename = "4Debug.py"
try:
    with open(filename, "r") as f:
        tree = ast.parse(f.read(), filename=filename)
except FileNotFoundError:
    print("❌ Could not find 4Debug.py file.")
    exit()

used_pupil_name_correctly = False
used_age_correctly = False

# Scan the AST for print() usage with correct variable names
for node in ast.walk(tree):
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'print':
        for arg in node.args:
            if isinstance(arg, ast.BinOp) and isinstance(arg.op, ast.Add):
                right = arg.right
                if isinstance(right, ast.Name) and right.id == "pupilName":
                    used_pupil_name_correctly = True
                elif (
                    isinstance(right, ast.Call)
                    and isinstance(right.func, ast.Name)
                    and right.func.id == "str"
                    and isinstance(right.args[0], ast.Name)
                    and right.args[0].id == "age"
                ):
                    used_age_correctly = True

# Feedback
if used_pupil_name_correctly:
    print("✅ You used the correct variable: pupilName")
else:
    print("❌ You didn't use the variable pupilName")

if used_age_correctly:
    print("✅ You used the correct variable: age")
else:
    print("❌ You didn't use the variable age")

if used_pupil_name_correctly and used_age_correctly:
    print("🎉 All key variables used correctly! Well done.")
else:
    print("🔍 Double-check that you are using the correct variable names.")
