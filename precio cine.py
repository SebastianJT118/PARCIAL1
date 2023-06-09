def calcular_precio_boletas(cantidad_boletas, tipo_sala, hora_pico, pago_tarjeta_cine, reserva):
    # Definir los precios básicos de las salas
    precios_basicos = {"Dinamix": 18800, "3D": 15500, "2D": 11300}
    
    # Obtener el precio básico de la sala seleccionada
    precio_base = precios_basicos[tipo_sala]
    
    # Aplicar descuentos por hora no pico y por cantidad de boletas compradas
    if not hora_pico:
        descuento = 0.1 * precio_base
        if cantidad_boletas >= 3:
            descuento += (cantidad_boletas - 2) * 500
        precio_base -= descuento
    
    # Aplicar descuento por pago con tarjeta del cinema
    if pago_tarjeta_cine:
        descuento = 0.05 * precio_base
        precio_base -= descuento
    
    # Aplicar recargo por reserva
    if reserva:
        recargo = cantidad_boletas * 2000
        precio_base += recargo
    
    # Aplicar aumento por hora pico
    if hora_pico:
        if tipo_sala == "Dinamix":
            aumento = 0.5 * precio_base
        else:
            aumento = 0.25 * precio_base
        precio_base += aumento
    
    # Redondear al número entero más cercano
    precio_total = round(precio_base * cantidad_boletas)
    
    return precio_total
