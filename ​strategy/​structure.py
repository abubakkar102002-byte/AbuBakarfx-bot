
# strategy/structure.py
import pandas as pd

class StructureAnalyzer:
    def __init__(self, swing_window=5):
        self.swing_window = swing_window

    def detect_swings(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df['swing_high'] = False
        df['swing_low'] = False

        for i in range(self.swing_window, len(df) - self.swing_window):
            is_high = all(df['high'].iloc[i] > df['high'].iloc[i - j] for j in range(1, self.swing_window + 1)) and \
                      all(df['high'].iloc[i] > df['high'].iloc[i + j] for j in range(1, self.swing_window + 1))
            
            is_low = all(df['low'].iloc[i] < df['low'].iloc[i - j] for j in range(1, self.swing_window + 1)) and \
                     all(df['low'].iloc[i] < df['low'].iloc[i + j] for j in range(1, self.swing_window + 1))

            df.iloc[i, df.columns.get_loc('swing_high')] = is_high
            df.iloc[i, df.columns.get_loc('swing_low')] = is_low

        return df

    def analyze_structure(self, df: pd.DataFrame) -> dict:
        df = self.detect_swings(df)
        highs = df[df['swing_high']]
        lows = df[df['swing_low']]

        trend = "NEUTRAL"
        bos = False
        choch = False

        if len(highs) >= 2 and len(lows) >= 2:
            last_high = highs['high'].iloc[-1]
            prev_high = highs['high'].iloc[-2]
            last_low = lows['low'].iloc[-1]
            prev_low = lows['low'].iloc[-2]

            curr_close = df['close'].iloc[-1]

            if last_high > prev_high and last_low > prev_low:
                trend = "BULLISH"
                if curr_close > last_high:
                    bos = True
            elif last_high < prev_high and last_low < prev_low:
                trend = "BEARISH"
                if curr_close < last_low:
                    bos = True

            # CHoCH Detection
            if trend == "BULLISH" and curr_close < last_low:
                choch = True
            elif trend == "BEARISH" and curr_close > last_high:
                choch = True

        return {
            "trend": trend,
            "BOS": bos,
            "CHoCH": choch,
            "last_swing_high": highs['high'].iloc[-1] if len(highs) > 0 else None,
            "last_swing_low": lows['low'].iloc[-1] if len(lows) > 0 else None
        }
