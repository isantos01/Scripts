class SplunkExpertSystem:
    def __init__(self):
        self.rules = [
            {"condition": "no_datos", "solution": "Verificar si el usuario usa Splunk Free, ya que tiene limitaciones."},
            {"condition": "indice_incorrecto", "solution": "Asegurar que se está buscando en el índice correcto."},
            {"condition": "sin_permisos", "solution": "Revisar permisos y acceso al índice de datos."},
            {"condition": "fuera_rango_tiempo", "solution": "Verificar el rango de tiempo y corregir marcas incorrectas."},
            {"condition": "no_indexa_eventos", "solution": "Ajustar el límite de throughput en limits.conf."},
            {"condition": "eventos_tarde", "solution": "Usar _indextime para medir retraso y revisar la red."},
            {"condition": "eventos_corruptos", "solution": "Revisar codificación y configurar CHARSET en props.conf."},
            {"condition": "archivo_binario", "solution": "Verificar y configurar CHARSET en props.conf."},
            {"condition": "buckets_llenos", "solution": "Ajustar política de retención y tamaño en indexes.conf."},
            {"condition": "sin_registros_windows", "solution": "Verificar que el servicio de eventos esté activo."},
            {"condition": "fallo_WMI", "solution": "Comprobar permisos de administrador y estado de WMI."},
            {"condition": "splunk_bloqueado_WMI", "solution": "Reducir entradas WMI o usar forwarders universales."},
            {"condition": "splunk_no_inicia", "solution": "Revisar servicios de Splunk y permisos de usuario."},
            {"condition": "forwarder_no_envia", "solution": "Verificar conectividad y puertos en el firewall."},
            {"condition": "uso_memoria_excesivo", "solution": "Revisar fugas de memoria en splunkd y reiniciar."},
            {"condition": "alertas_no_funcionan", "solution": "Revisar condición de activación y permisos."},
            {"condition": "datos_duplicados", "solution": "Revisar configuración de forwarders y evitar duplicados."},
            {"condition": "error_autenticacion", "solution": "Verificar configuración de autenticación y restablecer credenciales."}
        ]

    def diagnosticar(self, problema):
        for regla in self.rules:
            if regla["condition"] == problema:
                return f"Diagnóstico: {regla['solution']}"
        return "No se encontró una solución en la base de conocimientos."

# Simulación de pruebas con información dummy
sistema = SplunkExpertSystem()

# Lista de problemas simulados
problemas_prueba = [
    "no_datos",
    "sin_permisos",
    "uso_memoria_excesivo",
    "alertas_no_funcionan",
    "error_autenticacion"
]

# Ejecutar las pruebas
for problema in problemas_prueba:
    resultado = sistema.diagnosticar(problema)
    print(f"Entrada: {problema} -> {resultado}")
