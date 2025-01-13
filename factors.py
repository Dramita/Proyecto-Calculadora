# factors.py

class ThreatAgent:
    def __init__(self, skill, motivation, opportunity, size):
        self.skill = skill
        self.motivation = motivation
        self.opportunity = opportunity
        self.size = size

    def evaluate(self):
        # Evaluar los factores de agente amenazante
        return self.skill + self.motivation + self.opportunity + self.size


class Vulnerability:
    def __init__(self, discoverability, exploitability, knowledge, intrusion_detection):
        self.discoverability = discoverability
        self.exploitability = exploitability
        self.knowledge = knowledge
        self.intrusion_detection = intrusion_detection

    def evaluate(self):
        # Evaluar los factores de vulnerabilidad
        return self.discoverability + self.exploitability + self.knowledge + self.intrusion_detection


class TechnicalImpact:
    def __init__(self, confidentiality, integrity, availability, responsibility):
        self.confidentiality = confidentiality
        self.integrity = integrity
        self.availability = availability
        self.responsibility = responsibility

    def evaluate(self):
        # Evaluar los factores técnicos
        return self.confidentiality + self.integrity + self.availability + self.responsibility


class BusinessImpact:
    def __init__(self, financial_damage, reputation_damage, non_compliance, privacy_violation):
        self.financial_damage = financial_damage
        self.reputation_damage = reputation_damage
        self.non_compliance = non_compliance
        self.privacy_violation = privacy_violation

    def evaluate(self):
        # Evaluar los factores de negocio
        return self.financial_damage + self.reputation_damage + self.non_compliance + self.privacy_violation

class RiskEnvironment:
    def __init__(self, environment):
        self.environment = environment

    def adjust_risk(self, total_risk):
        """
        Ajusta el riesgo total basado en el entorno en el que ocurre el riesgo.
        Los factores de ajuste son: 
        - QA: 0.5 (Riesgo Bajo)
        - Desarrollo: 1 (Riesgo Medio)
        - Producción: 1.5 (Riesgo Alto)
        - DMZ: 1.5 (Riesgo Alto)
        - DRP: 1.0 (Riesgo Medio)
        """
        if self.environment == "QA":
            adjustment_factor = 0.5
        elif self.environment == "Desarrollo":
            adjustment_factor = 1
        elif self.environment == "Producción":
            adjustment_factor = 1.5
        elif self.environment == "DMZ":
            adjustment_factor = 1.5
        elif self.environment == "DRP":
            adjustment_factor = 1.0
        else:
            adjustment_factor = 1  # Por defecto, si el ambiente es desconocido

        adjusted_risk = total_risk * adjustment_factor
        return adjusted_risk
