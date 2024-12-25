def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide_exact(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "خطأ: لا يمكن القسمة على صفر"
        result /= num
    return result

def divide_with_remainder(numbers):
    if len(numbers) < 2:
        return "يجب إدخال رقمين على الأقل للقسمة."
    
    quotient = numbers[0]
    remainder = 0
    for num in numbers[1:]:
        if num == 0:
            return "خطأ: لا يمكن القسمة على صفر"
        quotient, remainder = divmod(quotient, num)
    return quotient, remainder

def power(base, exponent):
    return base ** exponent

while True:
    print("اختر العملية:")
    print("1. الجمع")
    print("2. الطرح")
    print("3. الضرب")
    print("4. القسمة الدقيقة")
    print("5. القسمة مع باقي")
    print("6. رفع أسي")

    choice = input("أدخل خيارك (1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        numbers = []
        if choice == '6':
            base = float(input("أدخل قاعدة الرفع الأسي: "))
            exponent = float(input("أدخل الأس: "))
            print(f"نتيجة رفع {base} إلى القوة {exponent}: {power(base, exponent)}")
        else:
            num_count = int(input("كم عدد الأرقام التي تريد إدخالها؟ "))

            for i in range(num_count):
                num = float(input(f"أدخل الرقم {i + 1}: "))
                numbers.append(num)

            if choice == '1':
                print(f"نتيجة الجمع: {add(numbers)}")

            elif choice == '2':
                print(f"نتيجة الطرح: {subtract(numbers)}")

            elif choice == '3':
                print(f"نتيجة الضرب: {multiply(numbers)}")

            elif choice == '4':
                print(f"نتيجة القسمة الدقيقة: {divide_exact(numbers)}")

            elif choice == '5':
                quotient, remainder = divide_with_remainder(numbers)
                print(f"نتيجة القسمة: {quotient} والباقي: {remainder}")

        # سؤال المستخدم إذا كان يريد إجراء عملية أخرى
        next_calculation = input("هل تريد إجراء عملية أخرى؟ (نعم/لا): ")
        if next_calculation.lower() != 'نعم':
            break
    else:
        print("خيار غير صالح، يرجى اختيار خيار صحيح.")
