# main.py
import sys
from factors import ThreatAgent, Vulnerability, TechnicalImpact, BusinessImpact, RiskEnvironment
from utils import get_input

def main():
    print("Bienvenido al Sistema de Evaluación de Riesgos Automático\n")
    
    # Solicitar entradas del usuario para los factores de probabilidad
    print("\nFactores de Probabilidad")
    
    # Factores de probabilidad
    skill = get_input("Nivel de habilidad (1-9): ", [
        {'description': 'Experto en pruebas de penetración', 'value': 1},
        {'description': 'Redes y programación', 'value': 3},
        {'description': 'Usuario avanzado de computadores', 'value': 4},
        {'description': 'Alguna habilidad técnica', 'value': 6},
        {'description': 'Ninguna habilidad técnica', 'value': 9}
    ])
    
    motivation = get_input("Motivación (1, 4, 9): ", [
        {'description': 'Baja o ninguna recompensa', 'value': 1},
        {'description': 'Posible recompensa', 'value': 4},
        {'description': 'Alta recompensa', 'value': 9}
    ])
    
    opportunity = get_input("Oportunidad (0, 4, 7, 9): ", [
        {'description': 'Acceso completo o recursos caros requeridos', 'value': 0},
        {'description': 'Acceso o recursos especiales requeridos', 'value': 4},
        {'description': 'Algún acceso o recurso requerido', 'value': 7},
        {'description': 'Ningún acceso o recurso requerido', 'value': 9}
    ])
    
    size = get_input("Tamaño del grupo (2, 4, 5, 6, 9): ", [
        {'description': 'Desarrolladores', 'value': 2},
        {'description': 'Administradores de sistemas', 'value': 2},
        {'description': 'Usuarios de intranet', 'value': 4},
        {'description': 'Socios', 'value': 5},
        {'description': 'Usuarios autentificados', 'value': 6},
        {'description': 'Usuarios de internet anónimos', 'value': 9}
    ])
    
    # Promediar la probabilidad total
    probabilidad_total = (skill + motivation + opportunity + size) / 4
    
    # Solicitar entradas del usuario para los factores de vulnerabilidad
    print("\nFactores de Vulnerabilidad")
    
    # Factores de vulnerabilidad
    discoverability = get_input("Facilidad de descubrimiento (1, 3, 7, 9): ", [
        {'description': 'Prácticamente imposible', 'value': 1},
        {'description': 'Difícil', 'value': 3},
        {'description': 'Fácil', 'value': 7},
        {'description': 'Existen herramientas automatizadas para hacerlo', 'value': 9}
    ])
    
    exploitability = get_input("Facilidad de explotación (1, 3, 5, 9): ", [
        {'description': 'Teóricamente explotable', 'value': 1},
        {'description': 'Difícil', 'value': 3},
        {'description': 'Fácil', 'value': 5},
        {'description': 'Existen herramientas automatizadas para hacerlo', 'value': 9}
    ])
    
    knowledge = get_input("Conocimiento de la vulnerabilidad (1, 4, 6, 9): ", [
        {'description': 'Desconocido', 'value': 1},
        {'description': 'Escondido', 'value': 4},
        {'description': 'Obvio', 'value': 6},
        {'description': 'De conocimiento público', 'value': 9}
    ])
    
    intrusion_detection = get_input("Detección de intrusión (1, 3, 8, 9): ", [
        {'description': 'Detección activa en la aplicación', 'value': 1},
        {'description': 'Logueado y revisado', 'value': 3},
        {'description': 'Logueado pero sin ser revisado', 'value': 8},
        {'description': 'No logueado del todo', 'value': 9}
    ])
    
    # Promediar la vulnerabilidad total
    vulnerability_total = (discoverability + exploitability + knowledge + intrusion_detection) / 4
    
    # Solicitar entradas del usuario para los factores técnicos
    print("\nFactores Técnicos")
    
    # Factores técnicos
    confidentiality = get_input("Pérdida de confidencialidad (2, 6, 7, 9): ", [
        {'description': 'Filtración menor de datos no sensibles', 'value': 2},
        {'description': 'Filtración menor de datos críticos', 'value': 6},
        {'description': 'Filtración extensa de datos no sensibles', 'value': 7},
        {'description': 'Filtración extensa de datos críticos', 'value': 7},
        {'description': 'Filtración de todos los datos', 'value': 9}
    ])
    
    integrity = get_input("Pérdida de integridad (1, 3, 5, 7, 9): ", [
        {'description': 'Pocos datos dañados ligeramente', 'value': 1},
        {'description': 'Pocos datos dañados seriamente', 'value': 3},
        {'description': 'Muchos datos dañados ligeramente', 'value': 5},
        {'description': 'Muchos datos dañados seriamente', 'value': 7},
        {'description': 'Todos los datos dañados totalmente', 'value': 9}
    ])
    
    availability = get_input("Pérdida de disponibilidad (1, 5, 7, 9): ", [
        {'description': 'Pocos servicios secundarios interrumpidos', 'value': 1},
        {'description': 'Pocos servicios primarios interrumpidos', 'value': 5},
        {'description': 'Muchos servicios secundarios interrumpidos', 'value': 5},
        {'description': 'Muchos servicios primarios interrumpidos', 'value': 7},
        {'description': 'Todos los servicios completamente interrumpidos', 'value': 9}
    ])
    
    responsibility = get_input("Pérdida de responsabilidad (1, 7, 9): ", [
        {'description': 'Totalmente trazables', 'value': 1},
        {'description': 'Posiblemente trazables', 'value': 7},
        {'description': 'Completamente anónimos', 'value': 9}
    ])
    
    # Calcular el impacto técnico
    technical_impact = (confidentiality + integrity + availability + responsibility) / 4
    
    # Solicitar entradas del usuario para los factores de negocio
    print("\nFactores de Negocio")
    
    # Factores de negocio
    financial_damage = get_input("Daño financiero (1, 3, 7, 9): ", [
        {'description': 'Menor al costo de mitigar la vulnerabilidad', 'value': 1},
        {'description': 'Efecto menor en la ganancia monetaria del periodo', 'value': 3},
        {'description': 'Efecto significativo en la ganancia monetaria del periodo', 'value': 7},
        {'description': 'Bancarrota', 'value': 9}
    ])
    
    reputation_damage = get_input("Daño a la reputación (1, 4, 5, 9): ", [
        {'description': 'Daño mínimo', 'value': 1},
        {'description': 'Pérdida de clientes grandes', 'value': 4},
        {'description': 'Caída en la imagen pública', 'value': 5},
        {'description': 'Daño a la marca', 'value': 9}
    ])
    
    non_compliance = get_input("No cumplimiento (2, 5, 7): ", [
        {'description': 'Violación menor', 'value': 2},
        {'description': 'Violación clara', 'value': 5},
        {'description': 'Violación de alto perfil', 'value': 7}
    ])
    
    privacy_violation = get_input("Violación de privacidad (1, 3, 5, 7, 9): ", [
        {'description': 'Información no sensible expuesta', 'value': 1},
        {'description': 'Posible filtración de datos sensibles', 'value': 3},
        {'description': 'Filtración de datos sensibles', 'value': 5},
        {'description': 'Datos de clientes comprometidos', 'value': 7},
        {'description': 'Filtración de datos de la empresa entera', 'value': 9}
    ])
    
    # Calcular el impacto de negocio
    business_impact = (financial_damage + reputation_damage + non_compliance + privacy_violation) / 4
    
    # Promediar el impacto técnico y el impacto de negocio
    total_impact = (technical_impact + business_impact) / 2
    
    # Calcular severidad según el total de impacto
    if total_impact < 3:
        severidad = "Bajo"
    elif 3 <= total_impact < 6:
        severidad = "Medio"
    else:
        severidad = "Alto"
    
    # Mostrar el resultado final
    print(f"\nImpacto Técnico Promedio: {technical_impact}")
    print(f"Impacto de Negocio Promedio: {business_impact}")
    print(f"Total de Impacto Promedio: {total_impact}")
    print(f"Severidad Final: {severidad}")
    
    # Ajustar el riesgo según el ambiente
    environment = get_input("\nSelecciona el ambiente de la evaluación (producción, qa, desarrollo, dmz, drp): ", [
        {'description': 'Producción', 'value': 'producción'},
        {'description': 'QA', 'value': 'qa'},
        {'description': 'Desarrollo', 'value': 'desarrollo'},
        {'description': 'DMZ', 'value': 'dmz'},
        {'description': 'DRP', 'value': 'drp'}
    ])
    
    adjusted_risk = RiskEnvironment(environment).adjust_risk(total_impact)
    print(f"Riesgo ajustado para el ambiente '{environment}': {adjusted_risk}")

if __name__ == "__main__":
    main()
