
# strategy/liquidity.py
import pandas as pd

class LiquidityAnalyzer:
    def __init__(self, tolerance=0.0005):
        self.tolerance = tolerance

    def find_liquidity_pools(self, df: pd.DataFrame) -> dict:
        df = df.copy()
        equal_highs = []
        equal_lows = []

        for i in range(len(df) - 10, len(df) - 1):
            for j in range(i + 1, len(df)):
                # Equal Highs (BSL)
                if abs(df['high'].iloc[i] - df['high'].iloc[j]) <= self.tolerance:
                    equal_highs.append(df['high'].iloc[i])
                # Equal Lows (SSL)
                if abs(df['low'].iloc[i] - df['low'].iloc[j]) <= self.tolerance:
                    equal_lows.append(df['low'].iloc[i])

        curr_high = df['high'].iloc[-1]
        curr_low = df['low'].iloc[-1]

        bsL_swept = any(curr_high > h for h in equal_highs)
        ssl_swept = any(curr_low < l for l in equal_lows)

        return {
            "buy_side_liquidity": equal_highs[-1] if equal_highs else None,
            "sell_side_liquidity": equal_lows[-1] if equal_lows else None,
            "bsl_swept": bsL_swept,
            "ssl_swept": ssl_swept
        }
