# evaluador_seguro.py

def evaluar_y_enviar(accuracy, precision, recall, f1):
    import requests

    print("\n🔍 Métricas detectadas:")
    print(f"✔️ Accuracy: {accuracy:.2f}")
    print(f"✔️ Precision: {precision:.2f}")
    print(f"✔️ Recall: {recall:.2f}")
    print(f"✔️ F1 Score: {f1:.2f}")

    # Sistema de notas basado en F1 y Accuracy
    if f1 >= 0.90 and accuracy >= 0.90:
        nota_final = 10
    elif f1 >= 0.85 and accuracy >= 0.85:
        nota_final = 9
    elif f1 >= 0.80 and accuracy >= 0.80:
        nota_final = 8
    elif f1 >= 0.70 and accuracy >= 0.75:
        nota_final = 7
    elif f1 >= 0.60 and accuracy >= 0.70:
        nota_final = 6
    else:
        nota_final = 4

    print(f"\n✅ Nota automática calculada: {nota_final}/10")

    nombre_estudiante = input("🔤 Ingresa tu nombre completo o correo (obligatorio para guardar tu nota): ")

    # ✅ ESTE es el URL correcto para enviar respuestas al formulario
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSd_SYwMyw0i5lrSsSkPM9p7GkJ8ZHVQBJOXdU7A6mkowvGKKw/formResponse"

    # 🔢 Estos campos debes ajustarlos a los entry reales del nuevo formulario
    ENTRY_NOMBRE = "entry.734737616"       # ← este valor puede que ya no sea válido
    ENTRY_NOTA = "entry.1759145663"         # ← este valor también puede haber cambiado

    # 💡 Para que esto funcione bien debes:
    # - Ir al formulario
    # - Ir a modo "ver"
    # - Abrir el formulario
    # - Inspeccionar el campo nombre → obtienes el valor de `entry.xxxxxxx`
    # - Inspeccionar el campo nota → igual

    form_data = {
        ENTRY_NOMBRE: nombre_estudiante,
        ENTRY_NOTA: str(nota_final)
    }

    response = requests.post(form_url, data=form_data)

    if response.status_code in [200, 302]:
        print("✅ Nota enviada correctamente al formulario.")
    else:
        print(f"⚠️ Error al enviar la nota. Código: {response.status_code}")
