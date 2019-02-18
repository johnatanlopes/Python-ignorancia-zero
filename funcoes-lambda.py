# Função padrão no python
def soma(x, y, z):
    return x + y + z

print(soma(1,2,3))

# Função lambda é equivalente a função padrão acima
# A vantagem de usar uma lambda é mais vantajoso já que armazenamos em uma variável
f = (lambda x,y,z: x+y+z)
print(f(1,2,3))

# Podemos usar lambda dentro de lambdas
d = (lambda x: lambda y: x + y)
e = d(3)
print(e)
print(e(2))