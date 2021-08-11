from math import *

class Binomial:
    def __init__(self):
        pass

    def densiteBinomiale(self, n, p, k):
        """
        args : 
            - k : nombre de succes allant de 1 à n
            - n : nombre d'epreuves
            - p : probabilité
        """
        c = factorial(n) / (factorial(k) * factorial(n-k))
        x = c * p ** k * (1-p) **(n-k)
        return x

    def repartitionBinomiale(self, n, p, k):
        """
        args : 
            - k : nombre de succes allant de 1 à n
            - n : nombre d'epreuves
            - p : probabilité

        entrées :
            - densiteBinomiale(self, n, p, 0)
        """
        S = self.densiteBinomiale(n, p, 0)
        for i in range(k):
            S = S + self.densiteBinomiale(n, p, i+1)
        return S

    def repartitionBinomialeNegative(self, n, p, k):
        """
        args : 
            - k : nombre de succes allant de 1 à n
            - n : nombre d'epreuves
            - p : probabilité

        entrées :
            - densiteBinomiale(self, n, p, 0)
        """
        S = self.densiteBinomialeNegative(n, p, 0)
        for i in range(k):
            S = S + self.densiteBinomialeNegative(n, p, i+1)
        return S

    def densiteBinomialeNegative(self, n, p, k):
        """
        args : 
            - k : nombre de succes allant de 1 à n
            - n : nombre d'epreuves
            - p : probabilité
        """
        c = factorial(k+n-1) / (factorial(k) * factorial(n-1))
        x = c * p ** k * (1-p) **(n-k)
        return x

    def esperanceBinomial(self, n, p):
        """
        args : 
            - n : nombre d'epreuves
            - p : probabilité
        """
        esp = n * p
        return esp

    def varianceBinomial(self, n, p):
        """
        args : 
            - n : nombre d'epreuves
            - p : probabilité
        """
        var = n * p * (1 - p)
        return var

    def esperanceBinomialeNegative(self, n, p):
        """
        args : 
            - n : nombre d'epreuves
            - p : probabilité
        """
        esp = (n * (p - 1)) / p
        return esp

    def varianceBinomialeNegative(self, n, p):
        """
        args : 
            - n : nombre d'epreuves
            - p : probabilité
        """
        var = (n * (p - 1)) / p**2
        return var