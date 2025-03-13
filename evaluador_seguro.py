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

    form_url = "https://docs.google.com/forms/d/e/1sWBNmNKN9f9F4nhLGFF57M8JH_pWWz_hl5fkwKhQJWo/formResponse"
    ENTRY_NOMBRE = "entry.734737616"
    ENTRY_NOTA = "entry.1759145663"

    form_data = {
        ENTRY_NOMBRE: nombre_estudiante,
        ENTRY_NOTA: str(nota_final)
    }

    response = requests.post(form_url, data=form_data)

    if response.status_code in [200, 302]:
        print("✅ Nota enviada correctamente al formulario.")
    else:
        print(f"⚠️ Error al enviar la nota. Código: {response.status_code}")
