document.getElementById("riskForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevenir el envío del formulario
    
    // Obtener los valores de los campos
    const skill = parseInt(document.getElementById("skill").value);
    const motivation = parseInt(document.getElementById("motivation").value);
    const opportunity = parseInt(document.getElementById("opportunity").value);
    const size = parseInt(document.getElementById("size").value);
    
    const discoverability = parseInt(document.getElementById("discoverability").value);
    const exploitability = parseInt(document.getElementById("exploitability").value);
    const knowledge = parseInt(document.getElementById("knowledge").value);
    const intrusion_detection = parseInt(document.getElementById("intrusion_detection").value);
    
    const confidentiality = parseInt(document.getElementById("confidentiality").value);
    const integrity = parseInt(document.getElementById("integrity").value);
    const availability = parseInt(document.getElementById("availability").value);
    const responsibility = parseInt(document.getElementById("responsibility").value);
    
    const financial_damage = parseInt(document.getElementById("financial_damage").value);
    const reputation_damage = parseInt(document.getElementById("reputation_damage").value);
    const non_compliance = parseInt(document.getElementById("non_compliance").value);
    const privacy_violation = parseInt(document.getElementById("privacy_violation").value);

    // Cálculo de la posibilidad
    const total_possibility = (skill + motivation + opportunity + size + discoverability + exploitability + knowledge + intrusion_detection) / 8;

    // Cálculo del impacto técnico
    const total_technical_impact = (confidentiality + integrity + availability + responsibility) / 4;

    // Cálculo del impacto en el negocio
    const total_business_impact = (financial_damage + reputation_damage + non_compliance + privacy_violation) / 4;

    // Cálculo de la severidad promedio
    const average_impact = (total_technical_impact + total_business_impact) / 2;

    // Determinar la severidad
    let severity = '';
    let severityClass = '';
    if (total_possibility < 3 && average_impact < 3) {
        severity = 'Bajo';
        severityClass = 'severity-bajo';
    } else if (total_possibility < 6 && average_impact < 6) {
        severity = 'Medio';
        severityClass = 'severity-medio';
    } else if (average_impact >= 6) {
        severity = 'Alto';
        severityClass = 'severity-alto';
    } else {
        severity = 'Crítico';
        severityClass = 'severity-crítico';
    }

    // Mostrar el resultado
    document.getElementById("finalRisk").innerHTML = `
        Total de Posibilidad: ${total_possibility.toFixed(2)}<br>
        Total de Impacto Técnico: ${total_technical_impact.toFixed(2)}<br>
        Total de Impacto de Negocio: ${total_business_impact.toFixed(2)}
    `;
    document.getElementById("severity").innerHTML = `Severidad del Riesgo: <span class="${severityClass}">${severity}</span>`;
    document.getElementById("result").style.display = "block";
});
