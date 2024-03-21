def classify_number(n):
    # Tính tổng các ước số
    s = sum(i for i in range(1, n) if n % i == 0)
    
    # So sánh s với n
    if s < n:
        return "tổng các ước số của nó nhỏ hơn chính nó"
    elif s == n:
        return "tổng các ước số của nó bằng chính nó"
    else:
        return "tổng các ước số của nó lớn hơn chính nó"

def Number(x, y):
    for num in range(x, y + 1):
        classification = classify_number(num)
        print(f"Số {num} có {classification}.")

# Ví dụ sử dụng
Number(5, 20)

