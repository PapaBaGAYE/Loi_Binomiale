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
