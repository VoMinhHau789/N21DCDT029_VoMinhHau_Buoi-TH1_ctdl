def Neper(n):
    """
    Tính tổng của n số hạng đầu tiên trong dãy Neper.
    :param n: Một số nguyên (n >= 0)
    :return: Tổng của a0 + a1 + ... + an
    """
    e_sum = 0  # Khởi tạo tổng
    a_k = 1.0  # Khởi tạo số hạng đầu tiên (a0)

    for k in range(n + 1):
        e_sum += a_k  # Cộng số hạng hiện tại vào tổng
        a_k /= (k + 1)  # Tính số hạng tiếp theo (a_k+1)

    return e_sum

# Ví dụ sử dụng
n = int(input("Nhập một số nguyên n (n >= 0): "))
result = Neper(n)
print(f"Tổng của {n} số hạng đầu tiên trong dãy Neper là: {result:.6f}")
