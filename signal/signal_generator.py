class SignalGenerator:
    def generate_signal(self, sentiment_score):
        if sentiment_score > 0.4:
            return ("BUY", sentiment_score)
        elif sentiment_score < -0.4:
            return ("SELL", sentiment_score)
        return ("HOLD", sentiment_score)
