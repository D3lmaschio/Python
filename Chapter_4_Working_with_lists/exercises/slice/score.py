scores = [235, 220, 100, 400, 59, 46, 126]
scores.sort(reverse=True)

for score in scores[:3]:
    if scores.index(score) == 0:
        print(f"Primeiro lugar com {score} de pontos!")

    elif scores.index(score) == 1:
        print(f"Segundo lugar com {score} de pontos!")

    else:
        print(f"Terceiro lugar com {score} de pontos!")

print(scores[:3])
