cat > README.md << 'EOF'
# 🏦 Axizulo African Bank - Full Stack Banking Application

A complete full-stack banking application built with Python Flask backend and modern frontend technologies. Demonstrates professional software development practices with Object-Oriented Programming principles.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.1.2-green.svg)
![HTML5](https://img.shields.io/badge/HTML5-E34F26.svg)
![CSS3](https://img.shields.io/badge/CSS3-1572B6.svg)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow.svg)

## 📋 Features

### Banking Operations
- ✅ **Account Management** - Create savings & current accounts
- ✅ **Transactions** - Deposits, withdrawals, and transfers
- ✅ **Real-time Balance** - Instant balance updates
- ✅ **Transaction History** - Complete audit trail
- ✅ **Interest Calculation** - Automated interest for savings accounts
- ✅ **Overdraft Facility** - R1000 overdraft for current accounts

### Technical Features
- 🔐 **Session Management** - Secure user sessions
- 📱 **Responsive Design** - Works on desktop and mobile
- ⚡ **Real-time Updates** - AJAX-powered interactions
- 🧪 **Unit Testing** - Comprehensive test coverage
- 🏗️ **OOP Design** - Clean, maintainable architecture

## 🛠 Tech Stack

### Backend
- **Python 3.10+** - Core programming language
- **Flask** - Lightweight web framework
- **OOP Principles** - Classes, Inheritance, Encapsulation
- **RESTful API** - Clean API design

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with Flexbox/Grid
- **JavaScript ES6+** - Vanilla JS with Fetch API
- **Responsive Design** - Mobile-first approach

### Architecture
- **MVC Pattern** - Model-View-Controller separation
- **Session Management** - Flask sessions for state
- **AJAX Communication** - Async frontend-backend interaction

## 📁 Project Structure

\`\`\`
banking-app/
├── src/                    # Core business logic
│   ├── bank.py            # Main banking system
│   ├── account.py         # Account classes (OOP core)
│   └── transaction.py     # Transaction handling
├── templates/             # Frontend views
│   ├── index.html         # Homepage
│   ├── create_account.html # Account creation
│   └── dashboard.html     # Main banking interface
├── tests/                 # Test suite
│   └── test_bank.py       # Unit tests
├── app.py                # Flask web application
├── main.py               # Command-line interface
└── requirements.txt      # Python dependencies
\`\`\`

## 🏃‍♂️ Quick Start

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   \`\`\`bash
   git clone https://github.com/thabangmotsoahae/banking-app.git
   cd banking-app
   \`\`\`

2. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. **Run the web application**
   \`\`\`bash
   python app.py
   \`\`\`

4. **Access the application**
   Open your browser and navigate to \`http://localhost:5000\`

### Alternative: Command Line Version
\`\`\`bash
python main.py
\`\`\`

## 🧪 Testing

Run the test suite to verify all functionality:
\`\`\`bash
python -m unittest tests/test_bank.py
\`\`\`

## 💡 OOP Concepts Demonstrated

### 1. Classes & Objects
\`\`\`python
class Account:
class SavingsAccount(Account):
class CurrentAccount(Account):
\`\`\`

### 2. Inheritance
- \`SavingsAccount\` and \`CurrentAccount\` inherit from base \`Account\` class
- Method overriding for specialized behavior

### 3. Encapsulation
- Private attributes with \`_prefix\`
- Property decorators for controlled access
- Data validation in setter methods

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | \`/\` | Homepage |
| GET/POST | \`/create_account\` | Account creation |
| GET | \`/dashboard\` | User dashboard |
| POST | \`/deposit\` | Deposit funds |
| POST | \`/withdraw\` | Withdraw funds |
| POST | \`/transfer\` | Transfer between accounts |
| GET | \`/balance\` | Check balance |
| GET | \`/transaction_history\` | Get transaction history |

## 🎯 Key Features Code Examples

### Account Creation
\`\`\`python
# Create savings account with interest
account = bank.create_account("John Doe", "savings", 1000.0, interest_rate=2.5)

# Create current account with overdraft
account = bank.create_account("Jane Smith", "current", 500.0, overdraft_limit=1000.0)
\`\`\`

### Transaction Processing
\`\`\`python
# Deposit with description
account.deposit(500.0, "Salary deposit")

# Withdraw with validation
account.withdraw(200.0, "ATM withdrawal")

# Transfer between accounts
bank.transfer_funds("ACC123", "ACC456", 300.0)
\`\`\`

## 🔧 Customization

### Adding New Account Types
Extend the \`Account\` class:
\`\`\`python
class BusinessAccount(Account):
    def __init__(self, account_holder, initial_deposit, business_type):
        super().__init__(account_holder, initial_deposit)
        self._business_type = business_type
\`\`\`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (\`git checkout -b feature/AmazingFeature\`)
3. Commit your changes (\`git commit -m 'Add some AmazingFeature'\`)
4. Push to the branch (\`git push origin feature/AmazingFeature\`)
5. Open a Pull Request

## 👨‍💻 Author

**Thabang Motsoahae**
- GitHub: [@Axulo-Inc](https://github.com/Axulo-Inc)
- LinkedIn: [Thabang Motsoahae](https://linkedin.com/in/thabangmotsoahae)

## 🙏 Acknowledgments

- Flask documentation and community
- Python software foundation
- Banking concept inspired by real-world financial systems
EOF
