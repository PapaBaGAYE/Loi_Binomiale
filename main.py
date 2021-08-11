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
        if (n >= k) :#or (p >= 0 and p <= 1)
            if (p >= 0 and p <= 1):
                c = factorial(n) / (factorial(k) * factorial(n-k))
                x = c * p ** k * (1-p) **(n-k)
                return x
            else:
                return 'p doit etre compris entre 0 et 1'
        elif (n < k) :#or (p < 0 and p >= 1)
            return 'Erreur : k doit etre inferieur à n'

    def repartitionBinomiale(self, n, p, k):
        """
        args : 
            - k : nombre de succes allant de 1 à n
            - n : nombre d'epreuves
            - p : probabilité

        entrées :
            - densiteBinomiale(self, n, p, 0)
        """
        if (n >= k) :#or (p >= 0 and p <= 1)
            if (p >= 0 and p <= 1):
                S = self.densiteBinomiale(n, p, 0)
                for i in range(k):
                    S = S + self.densiteBinomiale(n, p, i+1)
                return S
            else:
                return 'p doit etre compris entre 0 et 1'
        elif (n < k) :#or (p < 0 and p >= 1)
            return 'Erreur : k doit etre inferieur à n'

    def repartitionBinomialeNegative(self, n, p, k):
        """
        args : 
            - k : nombre de succes allant de 1 à n
            - n : nombre d'epreuves
            - p : probabilité

        entrées :
            - densiteBinomiale(self, n, p, 0)
        """
        if (n >= k) :#or (p >= 0 and p <= 1)
            if (p >= 0 and p <= 1):
                S = self.densiteBinomialeNegative(n, p, 0)
                for i in range(k):
                    S = S + self.densiteBinomialeNegative(n, p, i+1)
                return S
            else:
                return 'p doit etre compris entre 0 et 1'

        elif (n < k) :#or (p < 0 and p >= 1)
            return 'Erreur : k doit etre inferieur à n'

    def densiteBinomialeNegative(self, n, p, k):
        """
        args : 
            - k : nombre de succes allant de 1 à n
            - n : nombre d'epreuves
            - p : probabilité
        """
        if (n >= k) :#or (p >= 0 and p <= 1)
            if (p >= 0 and p <= 1):
                c = factorial(k+n-1) / (factorial(k) * factorial(n-1))
                x = c * p ** k * (1-p) **(n-k)
                return x
            else:
                return 'p doit etre compris entre 0 et 1'
        elif (n < k) :#or (p < 0 and p >= 1)
            return 'Erreur : k doit etre inferieur à n'

    def esperanceBinomial(self, n, p):
        """
        args : 
            - n : nombre d'epreuves
            - p : probabilité
        """
        if (p >= 0 and p <= 1):
            esp = n * p
            return esp
        else:
            return 'p doit etre compris entre 0 et 1'

    def varianceBinomial(self, n, p):
        """
        args : 
            - n : nombre d'epreuves
            - p : probabilité
        """
        if (p >= 0 and p <= 1):
            var = n * p * (1 - p)
            return var
        else:
            return 'p doit etre compris entre 0 et 1'

    def esperanceBinomialeNegative(self, n, p):
        """
        args : 
            - n : nombre d'epreuves
            - p : probabilité
        """
        if (p >= 0 and p <= 1):
            esp = (n * (1 - p)) / p
            return esp
        else:
            return 'p doit etre compris entre 0 et 1'

    def varianceBinomialeNegative(self, n, p):
        """
        args : 
            - n : nombre d'epreuves
            - p : probabilité
        """
        if (p >= 0 and p <= 1):
            var = (n * (1 - p)) / p**2
            return var
        else:
            return 'p doit etre compris entre 0 et 1'

    