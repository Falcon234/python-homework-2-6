s = input("Введи рядок з дужками: ")

stack = []
pairs = {')': '(', ']': '[', '}': '{'}

valid = True
for ch in s:
    if ch in '([{':
        stack.append(ch)
    elif ch in ')]}':
        if not stack or stack[-1] != pairs[ch]:
            valid = False
            break
        stack.pop()

if valid and not stack:
    print("Рядок валідний ✅")
else:
    print("Рядок невалідний ❌")
