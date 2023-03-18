dekdee = {'Nid':100,'Nut':133,'Not':112,'Natacha':89,'Nim':111,'Noo':90,'Now':99,'Nod':122,'Nai':88,'Nan':95}

def kidtang(dekdee):
    for name, age in dekdee.items():
        if age > 120:
            print(f'{name}: จ่ายเต็มนะจ๊ะ')
        elif age > 90:
            print(f'{name}: ลด 50%')
        else:
            print(f'{name}: เข้าฟรีจ้า')
