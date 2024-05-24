Pitaj_cenu=True
zbir_cena=0
while Pitaj_cenu:
    cena= int (input("Koliko si platio to?"))
    if cena==0:
        Pitaj_cenu=False
    else:
        zbir_cena=zbir_cena+cena
PAREEE=int(input("koliko je dato novca"))
print("Kusur je",PAREEE - zbir_cena,".")
