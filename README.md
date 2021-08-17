# Loi Binomiale
Ce module permet de faire des calculs sur **la loi binomiale** et la **loi binomiale négative**
<br>
à savoir
<h5>Les Moments</h5>
<ul>
    <li>Son esperance : E(X)</li>
    <li>Sa variance : Var(X)</li>
</ul>

<h5>Les probabilités</h5>
<ul>
    <li>La fonction de densité</li>
    <li>La fonction de répartition</li>
</ul>

## Fonctions / Methodes
Ce mondule a 8 fonctions pour le moment
<br>
<ol>
    <li><b>densiteBinomiale()</b> : qui permet de calculer la probalité d'une fonction de densité d'une loi binomiale</li>
    <li><b>densiteBinomialeNegative()</b> : qui permet de calculer la probalité d'une fonction de densité d'une loi binomiale négative</li>
    <li><b>repartitionBinomiale()</b> : qui permet de calculer la probalité d'une fonction de répartition d'une loi binomiale</li>
    <li><b>repartitionBinomialeNegative()</b> : qui permet de calculer la probalité d'une fonction de répartition d'une loi binomiale negative</li>
    <li><b>esperanceBinomiale()</b> : qui permet de calculer l'esperance' d'une loi binomiale</li>
    <li><b>varianceBinomiale()</b> : qui permet de calculer la variance d'une loi binomiale</li>
    <li><b>esperanceBinomialeNegative()</b> : qui permet de calculer l'esperance' d'une loi binomiale negative</li>
    <li><b>varianceBinomialeNegative()</b> : qui permet de calculer la variance d'une loi binomiale négative</li>
</ol>

### Exemple
from main import Binomial

B = Binomial()


print('Les Moments')
print("NORMALE")
print('E(X) = ', B.esperanceBinomial(5, 1/6))
print('V(X) = ', B.varianceBinomial(5, 1/6))
print("NEGATIVE")
print('E(X) = ', B.esperanceBinomialeNegative(5, 1/6))
print('V(X) = ', B.varianceBinomialeNegative(5, 1/6))
print('-'*50)

print('Fonction de densité')
sum = 0
for i in range(6):
    print(f'P(X={i}) = ', B.densiteBinomiale(5, 1/6, i))
    sum = sum + B.densiteBinomiale(5, 1/6, i)
print('La somme des probabilité est : ', sum)
print('-'*50)

print('Fonction de repartition')
print("NORMALE")
print(f'P(X<={5}) = ', B.repartitionBinomiale(5, 1/6, 5))
print("NEGATIVE")
print(f'P(X<={1}) = ', B.repartitionBinomialeNegative(5, 1/6, 1))
print('-'*50)
