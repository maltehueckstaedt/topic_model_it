import math
def calculate_sample_size(N=None, p=0.5, z=1.96, e=0.03):
    """
    Berechnet die benötigte Stichprobengröße basierend auf der Cochran-Formel.
    
    Parameter:
    N: Gesamtpopulation (Optional). Falls None, wird n_0 berechnet.
    p: Erwarteter Anteil (Default 0.5 für maximale Stichprobe).
    z: Z-Wert (Default 1.96 für 95% Konfidenz).
    e: Fehlermarge (Default 0.03 für 3%).
    """
    
    # 1. Basis-Stichprobengröße (n0) berechnen
    n_0 = (z**2 * p * (1 - p)) / (e**2)
    
    if N is None:
        return math.ceil(n_0)
    
    # 2. Korrekturterm für kleine Populationen berechnen
    # Korrekturterm = 1 + (z^2 * p * (1-p)) / (e^2 * N)
    correction_term = 1 + (n_0 / N)
    
    # Finale Stichprobengröße = n0 / Korrekturterm
    sample_size = n_0 / correction_term
    
    return math.ceil(sample_size)