list_Treatment = ['Skincare', 'Bodycare', 'Haircare']
list_Skincare = ["Facial", "Peeling", "Injeksi"]
list_Bodycare = ["Spa", "Lulur", "Body Massage"]
list_Haircare = ["Creambath", "Cutting", "Bleaching"]

nota = []
while True:
    print('=' * 50)
    for Treatment in range(0, len(list_Treatment)):
        print(f'{Treatment + 1}. {list_Treatment[Treatment]} ')
    Treatment = input('Masukkan Treatment yang Anda Pilih: ')
    if Treatment == '1':
        for Treatment_Treatment in range(0, len(list_Skincare)):
            print(f'{Treatment_Treatment + 1}. {list_Skincare[Treatment_Treatment]} ')
        ulangi = True
        while ulangi : 
            Skincare = int(input(f'Silahkan Pilih Treatmen 1-{len(list_Skincare)}: '))
            if Skincare <= 0 or Skincare > len(list_Skincare):
                print("====================")
                for Treatment_Skincare in range(0, len(list_Skincare)):
                    print(f'{Treatment_Skincare + 1}. {list_Skincare[Treatment_Skincare]} ')
                continue
            else:
                nota.append(list_Skincare[Skincare - 1])
                print('==Treatment Anda==')
                for list_nota in range(0, len(nota)):
                    print(f'{list_nota + 1}. {nota[list_nota]}')
                    ulangi = False
                continue
    elif Treatment == '2' :
        for Treatment_Bodycare in range(0, len(list_Bodycare)): 
            print(f'{Treatment_Bodycare + 1}. {list_Bodycare[Treatment_Bodycare]} ')
            ulangi = True
            while ulangi :
                Bodycare = int(input(f'Silahkan Pilih Treatment 1-{len(list_Bodycare)} '))
                if Bodycare <= 0 or Bodycare > len(list_Bodycare) :
                    print("====================")
                    for Treatment_Bodycare in range(0, len(list_Bodycare)) :
                        print(f'{Treatment_Bodycare + 1}. {list_Bodycare[Treatment_Bodycare]} ')
                    continue
                else:
                    nota.append(list_Bodycare[Bodycare - 1])
                    print('==Treatment Anda')
                    for list_nota in range(0, len(nota)):
                        print(f'{list_nota + 1}. {nota[list_nota]}')
                    ulangi = False
                continue
    elif Treatment == '3' :
        for Haircare in range(0, len(list_Haircare)) :
            print(f'{Treatment_Haircare + 1}. {list_Haircare[Treatment_Haircare]}')
        ulangi = True
        while ulangi :
            Haircare = int(input(f'Silahkan Pilih Treatment 1-{len(list_Haircare)}: '))
            if Haircare <= 0 or Haircare > len(list_Haircare) :
                print("====================")
                for Treatment_Haircare in range(0, len(list_Haircare)) :
                    print(f'{Treatment_Haircare + 1}. {list_Haircare[Treatment_Haircare]}')
                    ulangi = False
                continue
    else:
        print
        ('Treatment tidak terdaftar')
        continue
    lanjut = input('Apakah Ada Tambahan Treatment?')
    if lanjut == 'y' :
        continue
    else:
        Customer = input('Masukkan Nama Customer : ')
        print(f'Atas Nama {Customer}')
        print('=====List Treatment=====')
        for list_nota in range(0, len(nota)):
            print(f'{list_nota + 1}. {nota[list_nota]}')
        print('Terimakasih Atas Kunjungan Anda')
        break