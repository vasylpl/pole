cislo = int(1)
cislo_float = float(3.23)
text = str("string je sada znaku. napřiklad pro text")
boolean = True #boolenska hodnota, znači bud pravdu/nepravdu (true/false)

#Ddatovy typ - pole, kde mužeme mit vice prvku. Zavorku pišeme pravy alt + d/f
#v poli se začina na pozici 0. ačkoliv je delka pole 6, posledni prvek je na pozici 5
    
            #0        #1        #2     #3     #4
arrays = ["Ford", "porsche", "audi", "bmw", "mercedes"]

#tohle vypiše, uplně cele pole včetně hranatych závorek
#a uvozovek s čarkama
print(arrays)

# Výpis prvků pole pod sebou s indexy od 1 do délky pole
for i in range(1, len(arrays) + 1):
    print(f"{i}: {arrays[i - 1]}")
