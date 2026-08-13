
# strategy/order_block.py
import pandas as pd

class OrderBlockAnalyzer:
    def find_order_blocks(self, df: pd.DataFrame) -> dict:
        bullish_ob = None
        bearish_ob = None

        for i in range(len(df) - 3, len(df) - 1):
            # Bullish Order Block (Last bearish candle before impulsive up move)
            if df['close'].iloc[i] < df['open'].iloc[i] and df['close'].iloc[i+1] > df['open'].iloc[i+1]:
                if (df['close'].iloc[i+1] - df['open'].iloc[i+1]) > (df['high'].iloc[i] - df['low'].iloc[i]) * 1.5:
                    bullish_ob = {
                        "high": df['high'].iloc[i],
                        "low": df['low'].iloc[i],
                        "index": i
                    }

            # Bearish Order Block (Last bullish candle before impulsive down move)
            if df['close'].iloc[i] > df['open'].iloc[i] and df['close'].iloc[i+1] < df['open'].iloc[i+1]:
                if (df['open'].iloc[i+1] - df['close'].iloc[i+1]) > (df['high'].iloc[i] - df['low'].iloc[i]) * 1.5:
                    bearish_ob = {
                        "high": df['high'].iloc[i],
                        "low": df['low'].iloc[i],
                        "index": i
                    }

        return {
            "bullish_ob": bullish_ob,
            "bearish_ob": bearish_ob
        }
