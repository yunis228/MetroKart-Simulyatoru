pin = "1979"
cehd = 0

balans = 0
borc = 0
gedis = 0
limit = 100
gunluk_artirma = 0

emeliyyatlar = []

# PIN giris
while cehd < 3:
    daxil = input("PIN daxil et: ")

    if daxil == pin:
        print("Giris ugurludur")
        break
    else:
        cehd += 1
        print("Sehv PIN")

if cehd == 3:
    print("Proqram dayandi")
    exit()
    # Esas menyu
while True:

    print("\n--- MENYU ---")
    print("1) Balansi goster")
    print("2) Balans artir")
    print("3) Gedis et")
    print("4) Son emeliyyatlar")
    print("5) Gunluk statistika")
    print("6) Parametrler")
    print("0) Cixis")

    secim = input("Secim et: ")
    # Balansi goster
    if secim == "1":
        print("Balans:", balans)
        print("Borc:", borc)
       
    # Balans artir
    elif secim == "2":

        mebleg = float(input("Artirilacaq mebleg: "))

        if mebleg <= 0:
            print("Yanlis mebleg")
            continue

        if gunluk_artirma + mebleg > limit:
            print("Gunluk limit kecildi")
            continue

        gunluk_artirma += mebleg

        # Evvelce borcu bagla
        if borc > 0:
            if mebleg >= borc:
                mebleg -= borc
                borc = 0
            else:
                borc -= mebleg
                mebleg = 0    
        balans += mebleg

        emeliyyatlar.append(("Artirma", mebleg))

        print("Yeni balans:", balans)
        
    elif secim == "3":
        # 1. Qiymətin təyini (Tapşırıqdakı qaydalar üzrə)
        if gedis == 0:
            qiymet = 0.40  # 1-ci gediş: tam qiymət
        elif 1 <= gedis <= 3:
            qiymet = 0.36  # 2-4-cü gedişlər: 10% endirim
        else:
            qiymet = 0.30  # 5-ci və daha çox: 25% endirim
    # Qiymətin rejimə görə təyin edilməsi
        if rejim == "t":
            qiymet = 0.20  # Tələbə üçün sabit qiymət
        elif rejim == "p":
            qiymet = 0.15  # Pensiyaçı üçün sabit qiymət
        else:
            # Normal rejim üçün endirim pillələri
            if gedis == 0:
                qiymet = 0.40
            elif 1 <= gedis <= 3:
                qiymet = 0.36
            else:
                qiymet = 0.30
        # 2. Keçid yoxlaması
        if balans >= qiymet:
            balans -= qiymet
            gedis += 1
            emeliyyatlar.append(("Gedis", qiymet))
            print(f"Keçid uğurludur! Balans: {balans}")
            
        elif 0.30 <= balans < qiymet:
            print("Balans kifayət deyil, lakin Təcili keçid edə bilərsiniz.")
            cavab = input("0.10 AZN borca girməyə razisiniz? (h/y): ")
            if cavab.lower() == 'h':
                borc += (qiymet - balans)
                balans = 0
                gedis += 1
                emeliyyatlar.append(f"Təcili Keçid: {qiymet} AZN, Borc: {borc}")
                print(f"Keçid edildi. Cari borc: {borc}")
        else:
            print("Balans 0.30-dan aşağıdır. Keçid rədd olundu.")
        # son emeliyyatlar
    elif secim == "4":
        if not emeliyyatlar:
            print("Hələ heç bir əməliyyat yoxdur.")
        else:
            n = int(input("Son neçə əməliyyata baxmaq istəyirsiniz? "))
            son_n = emeliyyatlar[-n:] 
            print("\n--- Son Əməliyyatlar ---")
            for em in son_n:
                print(f"Tip: {em[0]}, Məbləğ: {em[1]} AZN")
        # gunluk statistika
    elif secim == "5":
        print("\n--- Günlük Statistika ---")
        print(f"Gediş sayı: {gedis}")
        print(f"Ümumi artırılan: {gunluk_artirma} AZN")
        # parametrler
    elif secim == "6":
        print("1) Limiti dəyiş\n2) Rejimi dəyiş (Normal/Tələbə/Pensiyaçı)")
        p_secim = input("Seçim edin: ")
        if p_secim == "1":
            limit = float(input("Yeni günlük limit: "))
        elif p_secim == "2":
            rejim = input("Rejim (n/t/p): ").lower()

        # Gedis
    elif secim == "0":
     print("Proqram baglandi")
     break