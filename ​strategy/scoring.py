
# strategy/scoring.py

class ConfluenceScorer:
    def calculate_score(self, structure: dict, liquidity: dict, ob: dict, fvgs: list) -> dict:
        score = 0
        reasons = []

        # 1. Structure Confluence (3 Points)
        if structure.get("BOS") or structure.get("CHoCH"):
            score += 3
            reasons.append("Structure BOS/CHoCH Confirmed (+3)")

        # 2. Liquidity Sweep Confluence (3 Points)
        if liquidity.get("bsl_swept") or liquidity.get("ssl_swept"):
            score += 3
            reasons.append("Liquidity Swept (+3)")

        # 3. Order Block Confluence (2 Points)
        if ob.get("bullish_ob") or ob.get("bearish_ob"):
            score += 2
            reasons.append("Order Block Identified (+2)")

        # 4. FVG Confluence (2 Points)
        if len(fvgs) > 0:
            score += 2
            reasons.append("Fair Value Gap Found (+2)")

        signal = "WAIT"
        if score >= 7:
            if structure.get("trend") == "BULLISH" or liquidity.get("ssl_swept"):
                signal = "BUY"
            elif structure.get("trend") == "BEARISH" or liquidity.get("bsl_swept"):
                signal = "SELL"

        return {
            "score": score,
            "max_score": 10,
            "signal": signal,
            "reasons": reasons
        }
