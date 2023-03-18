class taxuser:
    def __init__(self,name,ID,income):
        self.name = name
        self.ID = ID
        self.income = income     

    def information(self):
      print(f'ชื่อผู้เสียภาษี : {self.name}')
      print(f'เลขประจำตัวผู้เสียภาษี : {self.ID}')
      print(f'รายได้ก่อนหักภาษี : {self.income}')  

    def rate(self):
        if self.income <= 150000:
            Tax = 0
            netIncome = self.income-Tax
            print(f'ยอดภาษี : {Tax} บาท')
            print(f'รายได้หลังหักภาษี : {netIncome}')
        elif self.income <= 300000:
            Tax = (self.income-150000)*0.05
            netIncome = self.income-Tax
            print(f'ยอดภาษี : {Tax} บาท')
            print(f'รายได้หลังหักภาษี : {netIncome}')
        elif self.income <= 500000:
            Tax = 7500+((self.income-300000)*0.1)
            netIncome = self.income-Tax
            print(f'ยอดภาษี : {Tax} บาท')
            print(f'รายได้หลังหักภาษี : {netIncome}')
        elif self.income <= 750000:
            Tax = 7500+20000+((self.income-500000)*0.15)
            netIncome = self.income-Tax
            print(f'ยอดภาษี : {Tax} บาท')
            print(f'รายได้หลังหักภาษี : {netIncome}')
        elif self.income <= 1000000:
            Tax = 7500+20000+37500+((self.income-750000)*0.2)
            netIncome = self.income-Tax
            print(f'ยอดภาษี : {Tax} บาท')
            print(f'รายได้หลังหักภาษี : {netIncome}')
        elif self.income <= 2000000:
            Tax = 7500+20000+37500+50000+((self.income-1000000)*0.25)
            netIncome = self.income-Tax
            print(f'ยอดภาษี : {Tax} บาท')
            print(f'รายได้หลังหักภาษี : {netIncome}')
        elif self.income <= 5000000:
            Tax = 7500+20000+37500+50000+250000+((self.income-2000000)*0.3)
            netIncome = self.income-Tax
            print(f'ยอดภาษี : {Tax} บาท')
            print(f'รายได้หลังหักภาษี : {netIncome}')
        else:
            Tax = 7500+20000+37500+50000+250000+600000+((self.income-5000000)*0.35)
            netIncome = self.income-Tax
            print(f'ยอดภาษี : {Tax} บาท')
            print(f'รายได้หลังหักภาษี : {netIncome}')
    def timerecord(self):
        from datetime import datetime
        t = datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
        print(f'ยื่นภาษีเมื่อ : {t}')


class workplace(taxuser):
    def __init__(self,name_workplace,ID_workplace ,name,ID,income):
        super().__init__(name,ID,income)
        self.name_workplace = name_workplace
        self.ID_workplace = ID_workplace
    

    def information_workplace(self):
        print(f'สถานที่ทำงาน : {self.name_workplace}')
        print(f'เลขประจำตัวผู้เสียภาษีนิติบุคคล : {self.ID_workplace}')



print('**********************************************')
User01 = taxuser('AAA',1234,90000)
User01.information()
User01.rate()
User01.timerecord()
print('**********************************************')
workplace01 = workplace('A การช่าง',1669,'BBB',12344,7650000)
workplace01.information_workplace()
workplace01.information()
workplace01.rate()
workplace01.timerecord()
print('**********************************************')






