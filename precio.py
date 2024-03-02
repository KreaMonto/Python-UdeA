# crear un programa que calcule descuentos.
# pedir al usuario un precio y si es mayor a 10000 entonces hacer un descuento del 20%
# si el precio está entre 5000 y 10k entones del 10%
# todo lo demas sin descuento...
# -----------------------------------------------------------------------------------------------

precio = [float(input('diga un precio mmg:\n ---> '))]
precios = [15000, 20000, 4000, 45222, 458138, 13875, 4353843]


def calcularDescuento(nums):
    for num in nums:
        if num > 5000:
            if num > 10000:
                num = num * 0.8
                print(f'El precio tendrá un 20% de descuento: {num: .2f}\n')
            else:
                num = num * 0.9
                print(f'El precio tendrá un 10% de descuento: {num: .2f}\n')
        else:
            print(f'El precio es: {num}\n')



calcularDescuento(precios)
calcularDescuento(precio)