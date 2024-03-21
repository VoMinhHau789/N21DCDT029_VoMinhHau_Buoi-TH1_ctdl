def gcd_recursive(m, n):
    """
    Tính ước số chung lớn nhất (GCD) của hai số nguyên dương m và n bằng giải thuật đệ qui.
     Số nguyên dương m
     Số nguyên dương n
    :return: GCD của m và n
    """
    if n == 0:
        return m
    else:
        return gcd_recursive(n, m % n)

def gcd_iterative(m, n):
    """
    Tính ước số chung lớn nhất (GCD) của hai số nguyên dương m và n bằng giải thuật không đệ qui.
     Số nguyên dương m
     Số nguyên dương n
    :return: GCD của m và n
    """
    while n != 0:
        m, n = n, m % n
    return m

# Nhập hai số nguyên dương m và n
m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))

# Tính GCD bằng cả hai cách và in kết quả
result_recursive = gcd_recursive(m, n)
result_iterative = gcd_iterative(m, n)
print(f"Ước số chung lớn nhất của {m} và {n} (đệ qui): {result_recursive}")
print(f"Ước số chung lớn nhất của {m} và {n} (không đệ qui): {result_iterative}")


