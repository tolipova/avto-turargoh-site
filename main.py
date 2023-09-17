class Avto:
    def __init__(self,mashina_raqami,hour,tulov_narxi):
        self.mashina_raqami = mashina_raqami
        self.hour = hour 
        self.tulov_narxi = tulov_narxi
class Mashina:
    def __init__(self):
        self.car_number = []

    def add_number(self,mashina_raqami):
        self.car_number.append(mashina_raqami) 

    def find_car_number(self,mashina_raqami):
        for number in self.car_number:
            if number.mashina_raqami == mashina_raqami:
                return number
        return None
    
    def kirish(self,mashina_raqami):
        hour = float(input("kirgan vaqtingizni kiriting: "))
        number = self.find_car_number(mashina_raqami)
        if number is not None:
            number.hour = hour
            print(f"{number.mashina_raqami} raqamli mashina {number.hour} da turargohga kirgan")
        else:
            print("kirishda xatolik")    
    
    def chiqish(self,mashina_raqami):
        hour = float(input("chiqayotgan vaqtingiznii kiriting: "))
        number = self.find_car_number(mashina_raqami)
        if number is not None :
            number.hour = hour
            print=(f"{number.mashina_raqami} raqamli mashina {number.hour} da turargohdan chiqgan")
        else:
            print("Chiqishda xatolik")    

    def tulovi(self,mashina_raqami):
        number = self.find_car_number(mashina_raqami)  
        number.tulov_narxi = "qolgan vaqti"    
        if number.hour<= '1':
            print("Siz avto turargohda 1soat davomida qoldingiz va chiqishdan oldin 5000 so'm to'lang")
        elif number.hour >= '2':
            print("Siz avto turargohda 1soatdan ko'p qoldingiz va chiqishdan oldin 10.000 so'm to'lang")
        else:
            print("tulovda xatolik")    
        

    def display_number(self):
        print("Avto turargohda bor jami Mashinalar")
        for number in self.car_number:
            print(f"{number.mashina_raqami}:{number.hour}:{number.tulov_narxi}")

mashina = Mashina()
avto = Avto("85x244", "kirgan","qolgan vaqti")
mashina.add_number(avto)
avto = Avto("01x005","kirgan","qolgan vaqti")
mashina.add_number(avto)
avto = Avto("85x051","chiqgan","qolgan vaqti")
mashina.add_number(avto)
avto = Avto("85x279","kirgan","qolgan vaqti")
mashina.add_number(avto)
avto = Avto("85x445","chiqgan","qolgan vaqti")
mashina.add_number(avto)
avto = Avto("80x327","chiqgan","qolgan vaqti")
mashina.add_number(avto)
avto = Avto("01x606","kirgan","qolgan vaqti")
mashina.add_number(avto)
mashina.display_number()

while True :
    choice=input("Avto turargoh servisiga xush kelibsiz.Agar siz tanlasangiz (1)kirish , (2)chiqih , (3)qolgan vaqti uchun pul (4)dasturdan chiqasz")

    if choice == '4':
        print("Xayr , salomat bo'ling")
        break
   
    if choice not in ['1','2','3','4']:
        print("Xato raqam yoki belgi tanladiz")
        continue
    mashina_raqami= input("Mashinaning raqamini kiriting: ")

    if choice == '1':
        mashina.kirish(mashina_raqami)
    elif choice == '2' :
        mashina.chiqish(mashina_raqami)
    elif choice == '3':
        mashina.tulovi(mashina_raqami)    
    mashina.display_number()        






