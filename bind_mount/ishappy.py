def isHappy(n):
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)

        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10

        n = total

    return n == 1


if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)

    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")

    print("Results saved to /app/bind_mount/output.txt")
