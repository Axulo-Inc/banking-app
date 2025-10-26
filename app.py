from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from src.bank import AxizuloAfricanBank
import uuid

app = Flask(__name__)
app.secret_key = 'axizulo-bank-secret-key-2024'

# Initialize bank
bank = AxizuloAfricanBank()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        account_holder = request.form['account_holder']
        account_type = request.form['account_type']
        initial_deposit = float(request.form['initial_deposit'])
        
        account = bank.create_account(account_holder, account_type, initial_deposit)
        
        if account:
            # Store account number in session
            session['account_number'] = account.account_number
            return redirect(url_for('dashboard'))
    
    return render_template('create_account.html')

@app.route('/dashboard')
def dashboard():
    account_number = session.get('account_number')
    if not account_number:
        return redirect(url_for('index'))
    
    account = bank.get_account(account_number)
    if not account:
        return redirect(url_for('index'))
    
    return render_template('dashboard.html', 
                         account=account, 
                         bank=bank,
                         transactions=account.get_transaction_history()[-5:])  # Last 5 transactions

@app.route('/deposit', methods=['POST'])
def deposit():
    account_number = session.get('account_number')
    if not account_number:
        return jsonify({'success': False, 'message': 'No account selected'})
    
    account = bank.get_account(account_number)
    if not account:
        return jsonify({'success': False, 'message': 'Account not found'})
    
    amount = float(request.form['amount'])
    description = request.form.get('description', 'Deposit')
    
    success = account.deposit(amount, description)
    
    if success:
        return jsonify({'success': True, 'message': f'Successfully deposited R{amount:.2f}', 'balance': account.balance})
    else:
        return jsonify({'success': False, 'message': 'Deposit failed'})

@app.route('/withdraw', methods=['POST'])
def withdraw():
    account_number = session.get('account_number')
    if not account_number:
        return jsonify({'success': False, 'message': 'No account selected'})
    
    account = bank.get_account(account_number)
    if not account:
        return jsonify({'success': False, 'message': 'Account not found'})
    
    amount = float(request.form['amount'])
    description = request.form.get('description', 'Withdrawal')
    
    success = account.withdraw(amount, description)
    
    if success:
        return jsonify({'success': True, 'message': f'Successfully withdrew R{amount:.2f}', 'balance': account.balance})
    else:
        return jsonify({'success': False, 'message': 'Withdrawal failed'})

@app.route('/balance')
def balance():
    account_number = session.get('account_number')
    if not account_number:
        return jsonify({'success': False, 'message': 'No account selected'})
    
    account = bank.get_account(account_number)
    if not account:
        return jsonify({'success': False, 'message': 'Account not found'})
    
    return jsonify({'success': True, 'balance': account.balance})

@app.route('/transaction_history')
def transaction_history():
    account_number = session.get('account_number')
    if not account_number:
        return jsonify({'success': False, 'message': 'No account selected'})
    
    account = bank.get_account(account_number)
    if not account:
        return jsonify({'success': False, 'message': 'Account not found'})
    
    transactions = [t.to_dict() for t in account.get_transaction_history()]
    return jsonify({'success': True, 'transactions': transactions})

@app.route('/transfer', methods=['POST'])
def transfer():
    from_account_num = session.get('account_number')
    if not from_account_num:
        return jsonify({'success': False, 'message': 'No account selected'})
    
    to_account_num = request.form['to_account']
    amount = float(request.form['amount'])
    
    success = bank.transfer_funds(from_account_num, to_account_num, amount)
    
    if success:
        return jsonify({'success': True, 'message': f'Successfully transferred R{amount:.2f}'})
    else:
        return jsonify({'success': False, 'message': 'Transfer failed'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
