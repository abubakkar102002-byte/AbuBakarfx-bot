# strategy/fvg.py
import pandas as pd

class FVGAnalyzer:
    def find_fvgs(self, df: pd.DataFrame) -> list:
        fvgs = []
        for i in range(2, len(df)):
            # Bullish FVG: Candle 1 High < Candle 3 Low
            if df['high'].iloc[i-2] < df['low'].iloc[i]:
                fvgs.append({
                    "type": "BULLISH",
                    "top": df['low'].iloc[i],
                    "bottom": df['high'].iloc[i-2],
                    "index": i-1
                })
            # Bearish FVG: Candle 1 Low > Candle 3 High
            elif df['low'].iloc[i-2] > df['high'].iloc[i]:
                fvgs.append({
                    "type": "BEARISH",
                    "top": df['low'].iloc[i-2],
                    "bottom": df['high'].iloc[i],
                    "index": i-1
                })
        return fvgs

