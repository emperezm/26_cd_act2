import streamlit as st
import random

st.subheader ("Ejercicio 1: Saludo Simple")

nombre = st.text_input ("¿Cual es tu nombre?")

if nombre:
    st.write(f"¡Hola!, {nombre} ¡Bienvenido a streamlit!")
st.divider ()

st.subheader ("Ejercicio 2: Calculadora de Producto")

num1 = st.number_input("Ingrese el primer número:", value=0.0)
num2 = st.number_input("Ingrese el segundo número:", value=0.0)

resultado = num1 * num2
st.write(f"La multiplicación es: {resultado}")

if num1 > 100 or num2 > 100:
    st.warning("Números grandes")
st.divider ()

st.subheader ("Ejercicio 3: Convertidor de Temperatura")

opcion = st.radio(
    "Selecciona el tipo de conversión:",
    ("Celsius a Fahrenheit", "Fahrenheit a Celsius")
)

temperatura = st.number_input("Ingresa la temperatura:")

if opcion == "Celsius a Fahrenheit":
    resultado = (temperatura * 9/5) + 32
else:
    resultado = (temperatura - 32) * 5/9

st.success(f"Resultado: {resultado:.2f}")
st.divider ()

st.subheader ("Ejercicio 4: Galerí­a de Mascotas ")

tab1, tab2, tab3 = st.tabs(["Gatos", "Perros", "Aves"])

with tab1:
    st.image("https://cdn.pixabay.com/photo/2017/11/09/21/41/cat-2934720_1280.jpg")
    if st.button("Me gusta", key="gato"):
        st.toast("Te gusta esta mascota")

with tab2:
    st.image("https://th.bing.com/th/id/R.23d3c1447f55c3841c7ff2587afdc57f?rik=ro1IpJ4y16w9oQ&riu=http%3a%2f%2fwowmascota.com%2fwp-content%2fuploads%2f2019%2f05%2fpets-753464_640.jpg&ehk=IpnFAiS2WeuyIFLLROVoWkT0LdD%2fCV3bWApzNrtEwK8%3d&risl=&pid=ImgRaw&r=0")
    if st.button("Me gusta", key="perro"):
        st.toast("Te gusta esta mascota")

with tab3:
    st.image("https://farallonesdelcitara.bioexploradores.com/wp-content/uploads/2021/02/IMG_4051-4-1024x768.jpg")
    if st.button("Me gusta", key="ave"):
        st.toast("Te gusta esta mascota")
st.divider ()

st.subheader ("Ejercicio 5: Caja de Comentarios")

with st.form("form_comentarios"):
    asunto = st.text_input("Asunto")
    mensaje = st.text_area("Mensaje")
    enviar = st.form_submit_button("Enviar")

    if enviar:
        if mensaje.strip() != "":
            st.json({
                "Asunto": asunto,
                "Mensaje": mensaje
            })
        else:
            st.warning("El mensaje no puede estar vacío")
st.divider ()

st.subheader (" Ejercicio 6: Login Simulado")

if "logueado" not in st.session_state:
    st.session_state["logueado"] = False

if not st.session_state["logueado"]:
    usuario = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        if usuario == "admin" and password == "1234":
            st.session_state["logueado"] = True
            st.success("Login exitoso")
        else:
            st.error("Credenciales incorrectas")
else:
    st.success("Bienvenido, admin")

    if st.button("Cerrar Sesión"):
        st.session_state["logueado"] = False
        st.warning("Sesión cerrada")
st.divider ()

st.subheader ("Ejercicio 7: Lista de Compras")

if "lista_compras" not in st.session_state:
    st.session_state["lista_compras"] = []

producto = st.text_input("Ingresa un producto")

col1, col2 = st.columns(2)

with col1:
    if st.button("Agregar"):
        if producto.strip() != "":
            st.session_state["lista_compras"].append(producto)
            st.success("Producto agregado")

with col2:
    if st.button("Limpiar Lista"):
        st.session_state["lista_compras"] = []
        st.warning("Lista limpiada")

st.subheader("Productos:")
st.write(st.session_state["lista_compras"])
st.divider ()

st.subheader ("Ejercicio 8: Gráfico Interactivo")


N = st.slider("Selecciona cantidad de datos", 10, 100, 20)

if st.button("Regenerar"):
    pass  

datos = [random.randint(1, 100) for _ in range(N)]

st.line_chart(datos)
st.divider ()