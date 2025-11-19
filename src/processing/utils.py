from math import log
from typing import Optional

def compute_dew_point(temperature_c: Optional[float], humidity: Optional[float]) -> Optional[float]:
    """
    Magnus formula for dew point approximation.
    Returns dew point in Celsius or None if inputs missing.
    """
    
    if temperature_c is None or humidity is None:
        return None
    # Magnus coefficients for water
    a = 17.27
    b = 237.7
    alpha = (a * temperature_c) / (b + temperature_c) + log(humidity / 100.0)
    dew = (b * alpha) / (a - alpha)
    return round(dew, 3)

