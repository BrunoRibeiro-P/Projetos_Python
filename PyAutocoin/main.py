import yfinance as yf

class Converter:
    #how much is the currency worth in reais, and how much is the share worth in reais
    def __init__(self, costCurrencyReal=float, costActionsReal=float):
        self.costCurrencyReal = costCurrencyReal
        self.costActionsReal = costActionsReal

    def priceOneAction(self):
        return self.costActionsReal / self.costCurrencyReal 

if __name__ == '__main__':
    nameCurrency = input('Write the name of the currency: ')
    valueCurrency = float(input('Write the coin value: '))
    nameAction = input('Write the name of the action: ')
    #using ibovespa stock exchange
    #examples actions: PETR4.SA, VALE3.SA, AMZN
    ticker = yf.Ticker(nameAction)
    data = ticker.history(period='1d')
    current_price = data['Close'].iloc[-1]
    converter = Converter(valueCurrency, current_price)
    print('the share price is: ', converter.priceOneAction(), nameCurrency)
