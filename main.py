
from pyscript import document

elements = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.90),
    "Xe": ("Xenon", 54, 131.29),
    "Rn": ("Radon", 86, 222),
}

def element_info(event=None):

    element = document.getElementById("elementInput").value.strip().capitalize()

    element_data = elements.get(
        element, ("Element not found", "-", "-")
    )

    document.getElementById("result").innerHTML = f"""
        <b>Element:</b> {element_data[0]}<br>
        <b>Symbol:</b> {element if element_data[0] != "Element not found" else "-"}<br>
        <b>Atomic Number:</b> {element_data[1]}<br>
        <b>Atomic Mass:</b> {element_data[2]}
    """
