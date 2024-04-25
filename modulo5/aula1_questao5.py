import emoji

print("Emojis disponíveis:")
print(":white_heart: - 🤍")
print(":loudly_crying_face: - 😭")
print(":face_with_raised_eyebrow: - 🤨")
print(":face_savoring_food: - 😋")
print(":smiling_face_with_hearts: - 🥰")
print("")

print("Digite um frase e ela será emojizada:")
msg = emoji.emojize(input())
print("Frase emojizada:")
print (msg)