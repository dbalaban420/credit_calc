def def_credit(credit_sum, total_months, interest):

    debt_remainder = credit_sum
    payments = []
    total_payments = 0

    for _ in range (total_months):
        monthly_payment = float((credit_sum / total_months) + (debt_remainder * interest / 12 / 100))
        payments.append([debt_remainder, credit_sum / total_months, debt_remainder * interest / 12 / 100, monthly_payment])
        debt_remainder -= float(credit_sum / total_months)
        total_payments += float(monthly_payment)
        
    overpayment = float(total_payments - credit_sum)
    summary = (payments, overpayment)

    return summary, total_payments

def anu_credit(credit_sum, total_months, interest):

    debt_remainder = credit_sum
    payments = []
    total_payments = 0
    i = interest / 100 / total_months
    koef = (i * pow((1 + i), total_months)) / (pow((1 + i), total_months) - 1)

    for _ in range(total_months):
        monthly_payment = float(koef * credit_sum)
        month_sum = float(monthly_payment - debt_remainder * i)
        total_payments += float(monthly_payment)
        payments.append([debt_remainder, month_sum, float(monthly_payment - month_sum), float(monthly_payment)])
        debt_remainder -= float(month_sum)

    summary = (payments, float(total_payments - credit_sum))

    return summary, total_payments