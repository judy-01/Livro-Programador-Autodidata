pergunta = input("Qual é sua cor favorita ?")
with open("fav_color.txt", "w") as f:
    f.write(pergunta)