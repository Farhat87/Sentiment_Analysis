import matplotlib.pyplot as plt

class BacktestRunner:
    def run_backtest(self, signals, prices):
        portfolio = [100]  # Start with $100
        for i in range(1, len(signals)):
            if signals[i-1] == "BUY":
                portfolio.append(portfolio[-1] * (1 + prices[i] - prices[i-1]))
            elif signals[i-1] == "SELL":
                portfolio.append(portfolio[-1] * (1 - (prices[i] - prices[i-1])))
            else:
                portfolio.append(portfolio[-1])
        plt.plot(portfolio)
        plt.title("Portfolio Performance")
        plt.xlabel("Time")
        plt.ylabel("Portfolio Value")
        plt.grid()
        plt.show()
