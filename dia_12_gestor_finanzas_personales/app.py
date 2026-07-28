import streamlit as st
import pandas as pd
from datetime import date
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_DATOS = os.path.join(BASE_DIR, "transacciones.csv")
categorias = ["Comidas", "Transporte", "Entretenimiento", "Servicios", "Otros"]


class Transaccion:
    def __init__(self, descripcion: str, monto: float, fecha: date, categoria: str, tipo: str):
        self.descripcion = str(descripcion)
        self.monto = float(monto)
        self.fecha = fecha if isinstance(fecha, date) else date.fromisoformat(str(fecha).strip())
        self.categoria = str(categoria)
        self.tipo = str(tipo)

    def es_gasto(self) -> bool:
        return self.tipo == "Gasto"

    def es_ingreso(self) -> bool:
        return self.tipo == "Ingreso"

    def a_diccionario(self) -> dict:
        return {
            "descripcion": self.descripcion,
            "monto": self.monto,
            "fecha": self.fecha,
            "categoria": self.categoria,
            "tipo": self.tipo
        }


class Cartera:
    def __init__(self, transacciones: list[Transaccion] = None):
        self.transacciones = list(transacciones) if transacciones is not None else []

    def agregar_transaccion(self, transaccion: Transaccion):
        self.transacciones.append(transaccion)

    def total_ingresos(self) -> float:
        return sum(t.monto for t in self.transacciones if t.es_ingreso())

    def total_gastos(self) -> float:
        return sum(t.monto for t in self.transacciones if t.es_gasto())

    def balance(self) -> float:
        return self.total_ingresos() - self.total_gastos()

    def gasto_promedio(self) -> float:
        gastos = [t.monto for t in self.transacciones if t.es_gasto()]
        return sum(gastos) / len(gastos) if gastos else 0.0

    def filtrar(self, categorias_sel: list[str], fecha_desde: date, fecha_hasta: date) -> "Cartera":
        filtradas = [
            t for t in self.transacciones
            if t.categoria in categorias_sel and fecha_desde <= t.fecha <= fecha_hasta
        ]
        return Cartera(filtradas)

    def gastos_por_categoria_df(self) -> pd.DataFrame:
        gastos = [t for t in self.transacciones if t.es_gasto()]
        gastos_por_categoria = {}
        for t in gastos:
            gastos_por_categoria[t.categoria] = gastos_por_categoria.get(t.categoria, 0.0) + t.monto
        return pd.DataFrame(list(gastos_por_categoria.items()), columns=["Categoría", "Total"])

    def gastos_por_fecha_df(self) -> pd.DataFrame:
        gastos = [t for t in self.transacciones if t.es_gasto()]
        gastos_por_fecha = {}
        for t in gastos:
            gastos_por_fecha[t.fecha] = gastos_por_fecha.get(t.fecha, 0.0) + t.monto
        return pd.DataFrame(list(gastos_por_fecha.items()), columns=["Fecha", "Total"])

    def tiene_gastos(self) -> bool:
        return any(t.es_gasto() for t in self.transacciones)

    def esta_vacia(self) -> bool:
        return len(self.transacciones) == 0

    def rango_fechas(self) -> tuple[date, date]:
        if self.transacciones:
            fechas = [t.fecha for t in self.transacciones]
            return min(fechas), max(fechas)
        hoy = date.today()
        return hoy, hoy

    def a_dataframe(self) -> pd.DataFrame:
        if not self.transacciones:
            return pd.DataFrame(columns=["descripcion", "monto", "fecha", "categoria", "tipo"])
        return pd.DataFrame([t.a_diccionario() for t in self.transacciones])

    @classmethod
    def cargar_csv(cls, filepath: str) -> "Cartera":
        try:
            df = pd.read_csv(filepath)
            transacciones = []
            for _, row in df.iterrows():
                monto_val = float(row["monto"])
                fecha_val = date.fromisoformat(str(row["fecha"]).strip())
                t = Transaccion(
                    descripcion=str(row["descripcion"]),
                    monto=monto_val,
                    fecha=fecha_val,
                    categoria=str(row["categoria"]),
                    tipo=str(row["tipo"])
                )
                transacciones.append(t)
            return cls(transacciones)
        except Exception:
            return cls([])

    def guardar_csv(self, filepath: str):
        df = self.a_dataframe()
        df.to_csv(filepath, index=False)

    def importar_desde_dataframe(self, df: pd.DataFrame) -> int:
        contador = 0
        for _, row in df.iterrows():
            monto_val = float(row["monto"])
            fecha_val = date.fromisoformat(str(row["fecha"]).strip())
            t = Transaccion(
                descripcion=str(row["descripcion"]),
                monto=monto_val,
                fecha=fecha_val,
                categoria=str(row["categoria"]),
                tipo=str(row["tipo"])
            )
            self.agregar_transaccion(t)
            contador += 1
        return contador


def mostrar_titulo():
    st.title("Gestor de Finanzas Personales")
    st.write("Aplicación para gestionar tus finanzas personales")
    st.caption("Versión 1.0")


def guardar_transacciones():
    if "cartera" in st.session_state:
        st.session_state.cartera.guardar_csv(ARCHIVO_DATOS)


def inicializar_estado():
    if "cartera" not in st.session_state:
        st.session_state.cartera = Cartera.cargar_csv(ARCHIVO_DATOS)


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
                transaccion = Transaccion(descripcion, importe, fecha, categoria, tipo)
                st.session_state.cartera.agregar_transaccion(transaccion)
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

                contador = st.session_state.cartera.importar_desde_dataframe(df)
                st.success(f"Se importaron {contador} transacciones correctamente.")


def mostrar_filtros():
    categorias_sel = st.multiselect("Categorías", options=categorias, default=categorias)

    min_fecha, max_fecha = st.session_state.cartera.rango_fechas()

    fecha_desde = st.date_input("Desde", value=min_fecha)
    fecha_hasta = st.date_input("Hasta", value=max_fecha)

    return categorias_sel, fecha_desde, fecha_hasta


def mostrar_transacciones(cartera: Cartera):
    st.subheader("Transacciones acumuladas:")

    if not cartera.esta_vacia():
        df = cartera.a_dataframe()
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


def mostrar_resumen(cartera: Cartera):
    if cartera.esta_vacia():
        st.info("No hay transacciones registradas")
        return

    ingresos = cartera.total_ingresos()
    gastos = cartera.total_gastos()
    balance = cartera.balance()
    gasto_promedio = cartera.gasto_promedio()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Ingresos", f"{ingresos:.2f} €")
    col2.metric("Gastos", f"{gastos:.2f} €")
    col3.metric("Balance", f"{balance:.2f} €")
    col4.metric("Gasto promedio", f"{gasto_promedio:.2f} €")


def mostrar_analisis(cartera: Cartera):
    if not cartera.tiene_gastos():
        st.info("No hay transacciones de tipo Gasto registradas")
        return

    df_categoria = cartera.gastos_por_categoria_df()
    df_fecha = cartera.gastos_por_fecha_df()

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

cartera_filtrada = st.session_state.cartera.filtrar(categorias_sel, fecha_desde, fecha_hasta)

tab_resumen, tab_movimientos, tab_analisis = st.tabs(["Resumen", "Movimientos", "Análisis"])

with tab_resumen:
    mostrar_resumen(cartera_filtrada)

with tab_movimientos:
    mostrar_transacciones(cartera_filtrada)

with tab_analisis:
    mostrar_analisis(cartera_filtrada)

guardar_transacciones()