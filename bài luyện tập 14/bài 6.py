layers = {
    "layer-11": {
        "layer-21": 90,
        "layer-22": {
            "layer-31": 43
        }
    },
    "layer-12": 35
}
gia_tri_12 = layers["layer-12"]
print(f"Giá trị của layer-12 là: {gia_tri_12}")
gia_tri_31 = layers["layer-11"]["layer-22"]["layer-31"]
print(f"Giá trị của layer-31 là: {gia_tri_31}")