"""Demonstration of Strategy design pattern. AKA "Policy". Category: behavioral.

Useful for encapsulating a family of algorithms into objects that share a common interface.
This means the algorithms share the same inputs and function signature, and produce 
similar output.

Makes algorithms interchangeable, and leaves open for extension. Caller does not need to 
have knowledge of the algorithms or how they're chosen, but allows behavior to be adjusted
at runtime thanks to the shared interface. The word *interchangeable* is a key difference
from the Template pattern.

This example uses a simplified idea of an income tax, using a different strategy to
calculate an income tax in TX versus NY.

The TaxCalculator object is instantiated with a strategy, then no matter which strategy
was needed, calling the tax_amount method will produce the appropriate tax.
"""
from abc import ABC, abstractmethod


class AbstractTaxStrategy(ABC):
    
    @abstractmethod
    def calculate(self, object):
        """Calculate tax"""


class NYTaxStrategy(AbstractTaxStrategy):
    
    def calculate(self, income):
        return income * 0.1


class TXTaxStrategy(AbstractTaxStrategy):
    
    def calculate(self, _):
        return 0


class TaxCalculator:
    
    def __init__(self, strategy):
        self._strategy = strategy
    
    def tax_amount(self, income):
        return self._strategy.calculate(income)


def main():
    income = 60_000
    
    strategy = NYTaxStrategy()
    calculator = TaxCalculator(strategy)
    assert calculator.tax_amount(income) == 6000
    
    strategy = TXTaxStrategy()
    calculator = TaxCalculator(strategy)
    assert calculator.tax_amount(income) == 0


if __name__ == "__main__":
    main()
