secret_word="reloj"

print("Tengo agujas y no se coser,\n"
      "Tengo numeros y no se leer,\n"
      "        ¿Que soy?           \n\n"
)
user_word=""



while (secret_word!=user_word):
    user_word=input("Ingrese su palabra: ")

print("Felicitaciones, ganaste!")