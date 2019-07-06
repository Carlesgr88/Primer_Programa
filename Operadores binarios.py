helado_input=(input("¿Quieres un helado? (si/no) ")).upper()

if helado_input == "SI":
    helado= True
elif helado_input=="NO":
    helado= False
else:
    print("si o no monger")
    helado= False

dinero_input=(input("¿Tienes dinero para un helado? (si/no) ")).upper()
esta_tu_tia_input= input("¿esta tu tia? (si/no) ").upper()

helado= helado_input == "SI"
dinero=dinero_input == "SI" or esta_tu_tia_input == "SI"


if helado and dinero:
    print("pues comete un helado")
else:
    print("pues entonces nada")
