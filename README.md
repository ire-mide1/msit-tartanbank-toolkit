# TartanBank Nightly Toolkit

## Quiz Result
My quiz result screenshot is included as `quiz_result.png`. This shows all my 4 answers correctly
(10 total transactions, 5 deposits, 5 withdrawals, 3 distinct accounts). It was verified against
my Andrew ID.

## Bash vs Python: Why Each Tool Was Used
I used Bash and Python in this project.
Bash handles the file plumbing. `setup.sh` creates the folder structure and checks that
the transactions file exists, `secure_creds.sh` hashes the operator passphrase (for security), and
`run.sh` ties the whole nightly job together. Python is called to read the report
back to print a short summary. Bash is a good fit because it is built to automate files, folders, and other command-line tools like `sha256sum`, `grep`, and `wc`.

Python, on the other hand, handles the business logic. The `Account` and `Ledger`
classes in `bank.py` model how transactions are applied to individual accounts while
`process.py` reads the CSV, applies each transaction, and writes the report. Python is
the better choice here because object-oriented classes make it easy to keep each
account's balance and transaction count self-contained, while the Ledger coordinates
across all of them. This is not easy to achieve with Bash.

## The Hardest Part
The hardest part for me was setting up the WSL/Ubuntu environment and getting used to
the fact that scripts must actually be saved in the editor before running them in the
terminal. I ran into an issue where `setup.sh` and `secure_creds.sh` appeared to save
but were actually empty, because I had not saved the file in VS Code first. I also
accidentally created a nested duplicate project folder early on. I fixed both by
carefully checking file contents with `cat` before running anything, and by using
`mv` to consolidate my folder structure back into one clean directory.

## How to Run This Toolkit From a Fresh Clone

## The Hardest Part
The hardest part for me was setting up the WSL/Ubuntu environment and getting used to the fact that scripts must actually be saved in the editor before running them in the terminal — I ran into an issue where `setup.sh` and `secure_creds.sh` appeared to save but were actually empty, because I hadn't saved the file in VS Code first. I also accidentally created a nested duplicate project folder early on. I fixed both by carefully checking file contents with `cat` before running anything, and by using `mv` to consolidate my folder structure back into one clean directory.

## How to Run This Toolkit From a Fresh Clone

1. Clone the repository:
```
git clone https://github.com/ire-mide1/msit-tartanbank-toolkit.git
cd msit-tartanbank-toolkit
```

2. Make the scripts executable:
```
chmod +x setup.sh secure_creds.sh quiz.sh run.sh
```

3. Run the setup script to prepare folders:
```
./setup.sh
```

4. Add the provided `transactions.csv` file into the `data/` folder if it isn't already there.

5. Run the full nightly job:
```
./run.sh
```
This generates a dated report inside `reports/` and prints a short summary to the screen.

6. (Optional) Run the quiz to verify your understanding of the data:
```
./quiz.sh <include your_andrew_id>
```