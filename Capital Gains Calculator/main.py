# Press Shift+F10 to execute
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PortfolioConstructor import Portfolio


def main():
    port_a = Portfolio(cagr=3.49917,
                       std=0.635,
                       starting_capital=50000,
                       annual_withdrawals=0,
                       capacity=4250000
                       )

    port_b = Portfolio(cagr=2.47,
                       std=0.57,
                       starting_capital=97500,
                       annual_withdrawals=0,
                       capacity=4250000
                       )

    port_a.performance(years=4.0,
                       compound_frequency='Daily'
                       )

    port_b.performance(years=4.0,
                       compound_frequency='Daily'
                       )

    print(port_a.PortfolioValue, port_a.TaxLiability, port_a.RemovedFunds)
    print(port_b.PortfolioValue, port_b.TaxLiability, port_b.RemovedFunds)


if __name__ == '__main__':
    main()
