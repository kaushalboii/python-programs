def lsd(number):
    return number % 10
def msd(number):
    while number >= 10:
        number //= 10
    return number
num = 12345
print("Number:", num)
print("LSD:", lsd(num))
print("MSD:", msd(num))
