# src/superheat.py
from pyXSteam.XSteam import XSteam

# Create an instance using the MKS unit system
steam_table = XSteam(XSteam.UNIT_SYSTEM_MKS)


def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def superheat_temp(pressure_bar, enthalpy_kJkg, unit="C"):
    """
    Calculate superheated steam temperature.
    unit: "C" → Celsius (default), "F" → Fahrenheit
    """
    temp_c = steam_table.t_ph(pressure_bar, enthalpy_kJkg)
    if unit.upper() == "F":
        return celsius_to_fahrenheit(temp_c)
    return temp_c

if __name__ == "__main__":
    p = 100
    h = 3300
    t_c = superheat_temp(p, h, "C")
    t_f = superheat_temp(p, h, "F")
    print(f"Superheated steam temp at {p} bar, h={h} kJ/kg:")
    print(f"  → {t_c:.2f} °C")
    print(f"  → {t_f:.2f} °F")