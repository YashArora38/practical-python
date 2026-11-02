# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

start = int(input("extra_payment_start_month = "))
end = int(input("extra_payment_end_month = "))
amount = int(input("extra_payment = "))

month = 0

while principal > 0:
    month = month + 1

    # Check karo agar extra payment ka month chal raha hai
    if start <= month <= end:
        current_payment = payment + amount
    else:
        current_payment = payment

    # Jo payment bani, wahi principal se ghategi aur total me judegi
    principal = principal * (1 + rate / 12) - current_payment
    total_paid = total_paid + current_payment

print('Total paid', total_paid)