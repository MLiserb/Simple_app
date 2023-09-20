from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    chain = request.args.get('Chain', 'Ethereum')
    token = request.args.get('Token', 'ETH')
    from_date = request.args.get('From', '2018-11-01') 
    to_date = request.args.get('To', '2019-02-01')
    tx_value = request.args.get('Transaction size in USD', '5000')  
    action = request.args.get('Action', 'In')
    
    # In a real application, query a database or API here
    sample_wallets = ["0x1234567890...", "0x0987654321..."]
    
    return f"Wallets that match criteria for chain={chain}, token={token}, from={from_date}, to={to_date}, value={tx_value}, action={action}: {sample_wallets}"

@app.route('/docs')
def docs():
    return """
    <h1>API Documentation</h1>
    
    <p>/?Chain=[CHAIN]&Token=[TOKEN]&From=[FROM_DATE]&To=[TO_DATE]&Transaction size in USD=[TX_VALUE]&Action=[ACTION]</p>
    
    <p>Returns wallets matching the given criteria</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
