# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

X,Y,Z = False, False, False
print(not(X or Y or Z) == (not X and not Y and not Z))