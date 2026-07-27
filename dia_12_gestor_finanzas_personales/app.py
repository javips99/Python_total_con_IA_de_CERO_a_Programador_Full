import streamlit as st
import pandas as pd
from datetime import date
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_DATOS = os.path.join(BASE_DIR, "transacciones.csv")
categorias = ["Comidas", "Transporte", "Entretenimiento", "Servicios", "Otros"]


def mostrar_titulo():
    st.title("Gestor de Finanzas Personales")
    st.write("Aplicación para gestionar tus finanzas personales")
    st.caption("Versión 1.0")


def cargar_transacciones():
    try:
        df = pd.read_csv(ARCHIVO_DATOS)
        transacciones = []
        for _, row in df.iterrows():
            monto_val = float(row["monto"])
            fecha_val = date.fromisoformat(str(row["fecha"]).strip())
            transacciones.append({
                "descripcion": str(row["descripcion"]),
                "monto": monto_val,
                "importe": monto_val,
                "fecha": fecha_val,
                "categoria": str(row["categoria"]),
                "tipo": str(row["tipo"])
            })
        return transacciones
    except Exception:
        return []


def guardar_transacciones():
    if "transacciones" in st.session_state:
        df = pd.DataFrame(st.session_state.transacciones)
        df.to_csv(ARCHIVO_DATOS, index=False)


def inicializar_estado():
    if "transacciones" not in st.session_state:
        st.session_state.transacciones = cargar_transacciones()


def mostrar_formulario():
    with st.form("nueva_transaccion"):
        descripcion = st.text_input("Descripción del gasto o ingreso: ", placeholder="Escribe la descripción de la operación ")
        importe = st.number_input("Importe: ", min_value=0.0, step=1.0, format="%0.2f")
        fecha = st.date_input("Fecha: ")
        categoria = st.selectbox("Categoría: ", categorias)
        tipo = st.radio("Tipo: ", ["Ingreso", "Gasto"], horizontal=True)
        enviado = st.form_submit_button("Enviar")

        if enviado:
            if descripcion and importe > 0:
                st.session_state.transacciones.append({
                    "descripcion": descripcion,
                    "monto": importe,
                    "importe": importe,
                    "fecha": fecha,
                    "categoria": categoria,
                    "tipo": tipo
                })
                st.success("Transacción agregada correctamente")
            else:
                st.error("Debes completar todos los campos")


def importar_csv():
    with st.expander("Importar desde CSV"):
        archivo = st.file_uploader("Subir archivo CSV", type=["csv"])
        boton = st.button("Importar transacciones")

        if boton:
            if archivo is None:
                st.warning("Por favor, selecciona un archivo CSV primero.")
            else:
                try:
                    df = pd.read_csv(archivo)
                except Exception:
                    st.error("El archivo no es un CSV válido.")
                    return

                columnas_esperadas = ["descripcion", "monto", "fecha", "categoria", "tipo"]
                if not all(col in df.columns for col in columnas_esperadas):
                    st.error("El archivo CSV no contiene las columnas esperadas: descripcion, monto, fecha, categoria, tipo")
                    return

                contador = 0
                for _, row in df.iterrows():
                    monto_val = float(row["monto"])
                    fecha_val = date.fromisoformat(str(row["fecha"]).strip())
                    st.session_state.transacciones.append({
                        "descripcion": str(row["descripcion"]),
                        "monto": monto_val,
                        "importe": monto_val,
                        "fecha": fecha_val,
                        "categoria": str(row["categoria"]),
                        "tipo": str(row["tipo"])
                    })
                    contador += 1

                st.success(f"Se importaron {contador} transacciones correctamente.")


def mostrar_filtros():
    categorias_sel = st.multiselect("Categorías", options=categorias, default=categorias)

    if st.session_state.transacciones:
        fechas = [t["fecha"] for t in st.session_state.transacciones]
        min_fecha = min(fechas)
        max_fecha = max(fechas)
    else:
        min_fecha = date.today()
        max_fecha = date.today()

    fecha_desde = st.date_input("Desde", value=min_fecha)
    fecha_hasta = st.date_input("Hasta", value=max_fecha)

    return categorias_sel, fecha_desde, fecha_hasta


def filtrar_transacciones(transacciones, categorias_sel, fecha_desde, fecha_hasta):
    return [
        t for t in transacciones
        if t["categoria"] in categorias_sel and fecha_desde <= t["fecha"] <= fecha_hasta
    ]


def mostrar_transacciones(transacciones):
    st.subheader("Transacciones acumuladas:")

    if transacciones:
        df = pd.DataFrame(transacciones)
        st.dataframe(df)

        csv_data = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Descargar transacciones",
            data=csv_data,
            file_name="mis_transacciones.csv",
            mime="text/csv"
        )
    else:
        st.info("No hay transacciones registradas")


def mostrar_resumen(transacciones):
    if not transacciones:
        st.info("No hay transacciones registradas")
        return

    ingresos = sum(t.get("monto", t.get("importe", 0.0)) for t in transacciones if t["tipo"] == "Ingreso")
    gastos = sum(t.get("monto", t.get("importe", 0.0)) for t in transacciones if t["tipo"] == "Gasto")
    balance = ingresos - gastos

    gastos_list = [t.get("monto", t.get("importe", 0.0)) for t in transacciones if t["tipo"] == "Gasto"]
    gasto_promedio = sum(gastos_list) / len(gastos_list) if gastos_list else 0.0

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Ingresos", f"{ingresos:.2f} €")
    col2.metric("Gastos", f"{gastos:.2f} €")
    col3.metric("Balance", f"{balance:.2f} €")
    col4.metric("Gasto promedio", f"{gasto_promedio:.2f} €")


def mostrar_analisis(transacciones):
    gastos = [t for t in transacciones if t["tipo"] == "Gasto"]

    if not gastos:
        st.info("No hay transacciones de tipo Gasto registradas")
        return

    # Agregación por categoría usando diccionarios y bucle for
    gastos_por_categoria = {}
    for t in gastos:
        cat = t["categoria"]
        val = t.get("monto", t.get("importe", 0.0))
        gastos_por_categoria[cat] = gastos_por_categoria.get(cat, 0.0) + val

    # Agregación por fecha usando diccionarios y bucle for
    gastos_por_fecha = {}
    for t in gastos:
        fec = t["fecha"]
        val = t.get("monto", t.get("importe", 0.0))
        gastos_por_fecha[fec] = gastos_por_fecha.get(fec, 0.0) + val

    # DataFrames de 2 columnas construidos al final únicamente para la visualización
    df_categoria = pd.DataFrame(list(gastos_por_categoria.items()), columns=["Categoría", "Total"])
    df_fecha = pd.DataFrame(list(gastos_por_fecha.items()), columns=["Fecha", "Total"])

    st.subheader("Gastos por categoría")
    st.bar_chart(df_categoria, x="Categoría", y="Total")

    st.subheader("Gastos por fecha")
    st.line_chart(df_fecha, x="Fecha", y="Total")


mostrar_titulo()
inicializar_estado()

with st.sidebar:
    mostrar_formulario()
    importar_csv()
    categorias_sel, fecha_desde, fecha_hasta = mostrar_filtros()

transacciones_filtradas = filtrar_transacciones(st.session_state.transacciones, categorias_sel, fecha_desde, fecha_hasta)

tab_resumen, tab_movimientos, tab_analisis = st.tabs(["Resumen", "Movimientos", "Análisis"])

with tab_resumen:
    mostrar_resumen(transacciones_filtradas)

with tab_movimientos:
    mostrar_transacciones(transacciones_filtradas)

with tab_analisis:
    mostrar_analisis(transacciones_filtradas)

guardar_transacciones()