import requests

sr = '''
=================================
   CURRENCY CONVERTER (INR)
=================================
      Convert INR to:
      1. USD (USA)
      2. CNY (China)         
      3. JPY (Japan)
      4. KRW (South Korea)
      5. AED (UAE)
      6. SAR (Saudi Arabia)
      7. SGD (Singapore)
      8. MYR (Malaysia)
      9. THB (Thailand)
      10. PKR (Pakistan)
      11. BDT (Bangladesh)
      12. LKR (Sri Lanka)
      13. EUR (Euro - Europe)
      14. GBP (United Kingdom)
      15. AUD (Australia)
      16. CAD (Canada)
      17. CHF (Switzerland)
      18. RUB (Russia)
      19. ZAR (South Africa)
      20. NZD (New Zealand
      21. HKD (Hong Kong)
      22. TRY (Turkey)
      23. NOK (Norway)
      24. SEK (Sweden)
      25. DKK (Denmark)
      26. QAR (Qatar)
      27. KWD (Kuwait)
      28. OMR (Oman)
      29. BHD (Bahrain)
      30. IDR (Indonesia)
      31. PHP (Philippines)


  =================================
'''
print(sr)

choice = int(input("\nEnter your choice (1-12): "))
amount = float(input("Enter amount in INR: "))

if choice < 1 or choice > 30 or amount < 0:
    print("Invalid Choice Or Amount. Try Again..")

else:
    print("\nFetching real-time exchange rates...\n")

    url = "https://api.exchangerate-api.com/v4/latest/INR" #This url is used for fetching  real time exchange rate
    data = requests.get(url).json()

    if choice == 1:
        rate = data['rates']['USD']
        print(f"{amount} INR = {amount * rate} USD - US Dollar")

    elif choice == 2:
        rate = data['rates']['CNY']
        print(f"{amount} INR = {amount * rate} CNY - Chinese Yuan")

    elif choice == 3:
        rate = data['rates']['JPY']
        print(f"{amount} INR = {amount * rate} JPY - Japanese Yen")

    elif choice == 4:
        rate = data['rates']['KRW']
        print(f"{amount} INR = {amount * rate} KRW - South Korean Won")

    elif choice == 5:
        rate = data['rates']['AED']
        print(f"{amount} INR = {amount * rate} AED - UAE Dirham")

    elif choice == 6:
        rate = data['rates']['SAR']
        print(f"{amount} INR = {amount * rate} SAR - Saudi Riyal")

    elif choice == 7:
        rate = data['rates']['SGD']
        print(f"{amount} INR = {amount * rate} SGD - Singapore Dollar")

    elif choice == 8:
        rate = data['rates']['MYR']
        print(f"{amount} INR = {amount * rate} MYR - Malaysian Ringgit")


    elif choice == 9:
        rate = data['rates']['THB']
        print(f"{amount} INR = {amount * rate} THB - Thailand Baht")

    elif choice == 10:
        rate = data['rates']['PKR']
        print(f"{amount} INR = {amount * rate} PKR - Pakistani Rupee")

    elif choice == 11:
        rate = data['rates']['BDT']
        print(f"{amount} INR = {amount * rate} BDT - Bangladeshi Taka")


    elif choice == 12:
        rate = data['rates']['LKR']
        print(f"{amount} INR = {amount * rate} LKR - Sri Lankan Rupee")

    elif choice == 13:
        rate = data['rates']['EUR']
        print(f"{amount} INR = {amount * rate} EUR - Euro (Europe)")

    elif choice == 14:
        rate = data['rates']['GBP']
        print(f"{amount} INR = {amount * rate} GBP - British Pound (United Kingdom)")

    elif choice == 15:
        rate = data['rates']['AUD']
        print(f"{amount} INR = {amount * rate} AUD - Australian Dollar (Australia)")

    elif choice == 16:
        rate = data['rates']['CAD']
        print(f"{amount} INR = {amount * rate} CAD - Canadian Dollar (Canada)")

    elif choice == 17:
        rate = data['rates']['CHF']
        print(f"{amount} INR = {amount * rate} CHF - Swiss Franc (Switzerland)")

    elif choice == 18:
        rate = data['rates']['RUB']
        print(f"{amount} INR = {amount * rate} RUB - Russian Ruble (Russia)")

    elif choice == 19:
        rate = data['rates']['ZAR']
        print(f"{amount} INR = {amount * rate} ZAR - South African Rand (South Africa)")

    elif choice == 20:
        rate = data['rates']['NZD']
        print(f"{amount} INR = {amount * rate} NZD - New Zealand Dollar (New Zealand)")
    elif choice == 21:
        rate = data['rates']['HKD']
        print(f"{amount} INR = {amount * rate} HKD - Hong Kong Dollar (Hong Kong)")
    elif choice == 22:
        rate = data['rates']['TRY']
        print(f"{amount} INR = {amount * rate} TRY - Turkish Lira (Turkey)")
    elif choice == 23:
        rate = data['rates']['NOK']
        print(f"{amount} INR = {amount * rate} NOK - Norwegian Krone (Norway)")

    elif choice == 24:
        rate = data['rates']['SEK']
        print(f"{amount} INR = {amount * rate} SEK - Swedish Krona (Sweden)")

    elif choice == 25:
        rate = data['rates']['DKK']
        print(f"{amount} INR = {amount * rate} DKK - Danish Krone (Denmark)")
    elif choice == 26:
        rate = data['rates']['QAR']
        print(f"{amount} INR = {amount * rate} QAR - Qatari Riyal (Qatar)")
    elif choice == 27:
        rate = data['rates']['KWD']
        print(f"{amount} INR = {amount * rate} KWD - Kuwaiti Dinar (Kuwait)")
    elif choice == 28:
        rate = data['rates']['OMR']
        print(f"{amount} INR = {amount * rate} OMR - Omani Rial (Oman)")
    elif choice == 29:
        rate = data['rates']['BHD']
        print(f"{amount} INR = {amount * rate} BHD - Bahraini Dinar (Bahrain)")
    elif choice == 30:
        rate = data['rates']['IDR']
        print(f"{amount} INR = {amount * rate} IDR - Indonesian Rupiah (Indonesia)")
    elif choice == 31:
        rate = data['rates']['PHP']
        print(f"{amount} INR = {amount * rate} PHP - Philippine Peso (Philippines)")