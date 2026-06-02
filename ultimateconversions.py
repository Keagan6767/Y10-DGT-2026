import difflib
import re

# Registry simplified for brevity
UNIT_REGISTRY = {
    "m": {"aliases":["m","meter","metre","meters","metres"], "category":"distance", "to_base":1.0},
    "mm": {"aliases":["mm","millimeter","millimetre","millimetres"], "category":"distance", "to_base":0.001},
    "s": {"aliases":["s","sec","second","seconds"], "category":"time", "to_base":1.0},
    "min": {"aliases":["min","minute","minutes"], "category":"time", "to_base":60.0},
    "g": {"aliases":["g","gram","grams"], "category":"mass", "to_base":1.0},
    "kg": {"aliases":["kg","kilogram","kilograms"], "category":"mass", "to_base":1000.0},
    "L": {"aliases":["l","L","litre","liter","liters","litres"], "category":"volume", "to_base":1.0},
    "mL": {"aliases":["ml","millilitre","milliliter","milliliters","millilitres"], "category":"volume", "to_base":0.001},
    "C": {"aliases":["c","°c","celsius","degc"], "category":"temperature", "handler":"temperature"},
    "F": {"aliases":["f","°f","fahrenheit","degf"], "category":"temperature", "handler":"temperature"},
    "K": {"aliases":["k","kelvin"], "category":"temperature", "handler":"temperature"}
}

# Build alias map
ALIAS_MAP = {}
for canon, meta in UNIT_REGISTRY.items():
    for a in meta["aliases"]:
        ALIAS_MAP[a.lower()] = canon

def normalize_unit(raw):
    u = raw.lower().strip()
    u = re.sub(r"°", "", u)
    if u in ALIAS_MAP:
        return ALIAS_MAP[u]
    # fuzzy suggestions
    candidates = difflib.get_close_matches(u, list(ALIAS_MAP.keys()), n=3, cutoff=0.7)
    if candidates:
        suggestions = ", ".join(sorted({ALIAS_MAP[c] for c in candidates}))
        raise ValueError(f"Unknown unit '{raw}'. Did you mean {suggestions}?")
    raise ValueError(f"Unknown unit '{raw}'. Try common units like 'm', 'kg', 's', 'L'.")

def get_category(canon):
    return UNIT_REGISTRY[canon]["category"]

def convert_linear(value, from_canon, to_canon):
    base = value * UNIT_REGISTRY[from_canon]["to_base"]
    return base / UNIT_REGISTRY[to_canon]["to_base"]

def convert_temperature(value, from_canon, to_canon):
    # convert from source to Celsius
    if from_canon == "C":
        c = value
    elif from_canon == "K":
        c = value - 273.15
    elif from_canon == "F":
        c = (value - 32) * 5.0/9.0
    else:
        raise ValueError("Unsupported temperature unit")
    # convert Celsius to target
    if to_canon == "C":
        return c
    if to_canon == "K":
        return c + 273.15
    if to_canon == "F":
        return c * 9.0/5.0 + 32
    raise ValueError("Unsupported temperature unit")

def convert(value, from_unit_raw, to_unit_raw):
    from_canon = normalize_unit(from_unit_raw)
    to_canon = normalize_unit(to_unit_raw)
    from_cat = get_category(from_canon)
    to_cat = get_category(to_canon)
    if from_cat != to_cat:
        raise ValueError(f"Cannot convert {from_unit_raw} ({from_cat}) to {to_unit_raw} ({to_cat}). Choose units from the same category.")
    if from_cat == "temperature":
        return convert_temperature(value, from_canon, to_canon)
    return convert_linear(value, from_canon, to_canon)

# CLI demo
if __name__ == "__main__":
    examples = [
        (300, "seconds", "hours"),
        (500, "mm", "m"),
        (50, "g", "kg"),
        (100, "C", "F"),
    ]
    for val, f, t in examples:
        try:
            res = convert(val, f, t)
            print(f"{val} {f} -> {res} {t}")
        except ValueError as e:
            print("Error:", e)
