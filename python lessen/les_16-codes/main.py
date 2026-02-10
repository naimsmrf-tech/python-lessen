import caesar_code
import persoonlijke_code
import geheimen

caesar_sleutel = 17
eigen_sleutel = "secretkey"

berichten = [
    geheimen.tekst, geheimen.locatie, geheimen.wachtwoord, geheimen.stuk_tekst
]

for bericht in berichten:
    encrypted = caesar_code.encrypt(bericht, caesar_sleutel)
    print(f"Caesar encrypted message: {encrypted}")

    decrypted = caesar_code.decrypt(encrypted, caesar_sleutel)
    print(f"Caesar decrypted message: {decrypted}\n")

    encrypted = persoonlijke_code.encrypt(bericht, eigen_sleutel)
    print(f"Custom encrypted message: {encrypted}")

    decrypted = persoonlijke_code.decrypt(encrypted, eigen_sleutel)
    print(f"Custom decrypted message: {decrypted}\n")
