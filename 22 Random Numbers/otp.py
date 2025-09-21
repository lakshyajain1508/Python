import random
import string

def generate_otp(length=4):
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

num = int(input("Enter the length of the OTP (default is 4): ") or 4)

if __name__ == "__main__":
    otp_code_1 = generate_otp(length=num)
    print(f"Your {num}-digit OTP is: {otp_code_1}")