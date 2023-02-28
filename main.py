import csv
import datetime
import os
import mylib


def create_file(path="./",file_name = "menu.txt",):
    content = "* Lütfen Bir Pizza Tabanı Seçiniz:\n1: Klasik\n2: Margarita\n3: TürkPizza\n4: Sade Pizza\n* ve seçeceğiniz sos:\n11: Zeytin\n12: Mantarlar\n13: Keçi Peyniri\n14: Et\n15: Soğan\n16: Mısır\n* Teşekkür ederiz!"
    if os.path.exists(path + file_name):
        print("Dosya mevcut.")

    else:
        dosya = open(path+file_name, "w", encoding="Utf-8")
        dosya.write(content)

        dosya.close()

create_file()



def main():
    # Menüyü ekrana yazdırma
    print("Menü:")
    print("1. Klasik Pizza")
    print("2. Margherita Pizza")
    print("3. Türk Pizza")
    print("4. Dominos Pizza")
    print("5. Çıkış")

    # Seçimlerin alınması
    pizza_choice = input("Lütfen bir pizza seçin (1-5): ")
    while pizza_choice not in ["1", "2", "3", "4", "5"]:
        print("Lütfen geçerli bir seçim yapın.")
        pizza_choice = input("Lütfen bir pizza seçin (1-5): ")

    if pizza_choice == "5":
        print("Programdan çıkılıyor...")
        return

    sauce_choices = []
    while True:
        sauce_choice = input("Lütfen bir sos seçin (q ile çıkış): ")
        if sauce_choice.lower() == "q":
            break
        elif sauce_choice not in ["Zeytin", "Mantar", "Keçi Peyniri", "Et", "Soğan", "Mısır"]:
            print("Lütfen geçerli bir sos seçin.")
        else:
            sauce_choices.append(sauce_choice)

    # Pizza nesnesinin oluşturulması
    if pizza_choice == "1":
        pizza = mylib.KlasikPizza()
    elif pizza_choice == "2":
        pizza = mylib.MargaritaPizza()
    elif pizza_choice == "3":
        pizza = mylib.TurkPizza()
    else:
        pizza = mylib.SadePizza()

    # Sosların eklenmesi
    for sauce_choice in sauce_choices:
        if sauce_choice == "Zeytin":
            pizza = mylib.Zeytin(pizza)
        elif sauce_choice == "Mantar":
            pizza = mylib.Mantar(pizza)
        elif sauce_choice == "Keçi Peyniri":
            pizza = mylib.KeciPeyniri(pizza)
        elif sauce_choice == "Et":
            pizza = mylib.Et(pizza)
        elif sauce_choice == "Soğan":
            pizza = mylib.Sogan(pizza)
        elif sauce_choice == "Mısır":
            pizza = mylib.Misir(pizza)

    # Toplam fiyatın hesaplanması
    total_cost = pizza.get_cost()
    print("Toplam fiyat:", total_cost)

    # Kullanıcı bilgilerinin alınması ve veritabanına kaydedilmesi
    name = input("Adınız: ")
    id_number = input("TC Kimlik Numaranız: ")
    credit_card_number = input("Kredi Kartı Numaranız: ")
    credit_card_cvv = input("Kredi Kartı CVV: ")
    order_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    order_description = pizza.get_description()
    for sauce_choice in sauce_choices:
        order_description += " + " + sauce_choice

    with open("Orders_Database.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, id_number, credit_card_number, credit_card_cvv, order_description, order_time])

    print("Siparişiniz başarıyla kaydedildi. Teşekkür ederiz!")

if __name__ == "__main__":
    main()