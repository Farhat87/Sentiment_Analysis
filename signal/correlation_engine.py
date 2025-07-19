from scipy.stats import pearsonr

class CorrelationEngine:
    def correlate(self, sentiment_series, price_series):
        return pearsonr(sentiment_series, price_series)

