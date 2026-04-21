import secrets
import string

def otp_generator(length=6):
    """Otp generatsiya"""
    characters = string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

def otp_verifier(otp, user_otp):
    """Otp verifikatsiya"""
    return otp == user_otp

# Misol
otp = otp_generator()
print(f"Otp: {otp}")

user_otp = input("Iltimos, OTPni kiriting: ")
if otp_verifier(otp, user_otp):
    print("OTP to'g'ri!")
else:
    print("OTP xato!")
```

Kodda quyidagi funksiyalar mavjud:

1. `otp_generator(length=6)`: Bu funksiya 6 ta raqamdan iborat OTPni generatsiya qiladi. `length` parametriga 6 ni o'zgartirib, boshqa uzunlikdagi OTPni generatsiya qilish mumkin.

2. `otp_verifier(otp, user_otp)`: Bu funksiya generatsiyalangan OTP bilan foydalanuvchi tomonidan kiritilgan OTPni solishtiradi. Agar ular bir xil bo'lsa, funksiya `True` qiymatini qaytaradi, aks holda `False` qiymatini qaytaradi.

Misolni ko'rish uchun, OTP generatsiya qilingan va foydalanuvchi tomonidan kiritilgan OTPni verifikatsiya qilish uchun funksiyalarni ishlatiladi.
