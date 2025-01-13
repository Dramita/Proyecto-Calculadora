# utils.py
def get_input(prompt, options):
    """Muestra las opciones al usuario y devuelve el valor asociado"""
    print(prompt)
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option['description']}")
    
    while True:
        try:
            choice = int(input("Selecciona una opción (número): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]['value']
            else:
                print("Selección inválida. Por favor elige un número dentro del rango.")
        except ValueError:
            print("Por favor ingresa un número válido.")

