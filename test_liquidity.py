# test_liquidity.py
import pandas as pd
from strategy.liquidity import LiquidityAnalyzer

def test():
    data = {
        'open': [100, 102, 101, 105],
        'high': [105, 105, 103, 107],
        'low': [98, 99, 97, 96],
        'close': [102, 101, 105, 106]
    }
    df = pd.DataFrame(data)
    analyzer = LiquidityAnalyzer()
    res = analyzer.find_liquidity_pools(df)
    print("Liquidity Test Result:", res)

if __name__ == "__main__":
    test()

