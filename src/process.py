import sys
from bank import Ledger

def main():
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    ledger = Ledger()
    total_deposits = 0.0
    deposit_count = 0

    with open(input_path, "r") as f:
        lines = f.readlines()

    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue  # skip any blank lines
        account_id, transaction_type, amount_str = line.split(",")
        amount = float(amount_str)

        ledger.apply(account_id, transaction_type, amount)

        if transaction_type == "deposit":
            total_deposits += amount
            deposit_count += 1

    average_deposit = total_deposits / deposit_count if deposit_count > 0 else 0.0

    # Write the report
    with open(output_path, "w") as report:
        report.write("=== TartanBank Nightly Report ===\n\n")

        report.write("Final Account Balances:\n")
        for account_id, account in ledger.diff_accounts.items():
            report.write(f"  {account_id}: {account.balance:.2f}\n")

        total_transactions = sum(acc.transaction_count for acc in ledger.diff_accounts.values())
        report.write(f"\nTotal transactions processed: {total_transactions}\n")

        report.write("\nFlagged (declined) withdrawals:\n")
        if ledger.flagged:
            for item in ledger.flagged:
                report.write(f"  {item['account_id']}: attempted withdrawal of {item['amount']:.2f}\n")
        else:
            report.write("  None\n")

        report.write(f"\nTotal value of all deposits: {total_deposits:.2f}\n")
        report.write(f"Average deposit amount: {average_deposit:.2f}\n")

    print(f"Report written to {output_path}")

if __name__ == "__main__":
    main()