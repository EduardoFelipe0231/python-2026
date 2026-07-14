medida = float(input("Digite um valor em metros:"))

cm = medida * 100
mm = medida * 1000

print('A medida {}m - corresponde em {:.0f}cm e {:.0f}mm '.format(medida, cm, mm))