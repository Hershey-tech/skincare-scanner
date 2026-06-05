import matplotlib.pyplot as plt

def classify(name):
    n = name.lower()

    # water base
    if "water" in n or "aqua" in n:
        return ("Base Solvent", "Dissolves ingredients", "Safe")

    # glycols & penetration enhancers
    if "glycol" in n or "propanediol" in n:
        return ("Penetration Enhancer", "Improves absorption", "Safe")

    # humectants
    if any(x in n for x in ["glycerin","urea","lactate","pca","hyaluronic"]):
        return ("Humectant", "Attracts moisture & hydrates skin", "Safe")

    # amino acids
    if n.endswith("ine") or n.endswith("ine ") or n.endswith("acid"):
        if any(x in n for x in ["glycine","alanine","serine","valine","arginine","proline"]):
            return ("Amino Acid", "Supports hydration & repair", "Safe")

    # peptides
    if "peptide" in n:
        return ("Peptide Active", "Stimulates growth & repair", "Safe")

    # botanical extracts
    if "extract" in n:
        return ("Botanical Active", "Plant-based skin benefits", "Safe")

    # exfoliating acids
    if any(x in n for x in ["glycolic","salicylic","lactic","mandelic"]):
        return ("Exfoliant", "Removes dead skin & unclogs pores", "Moderate")

    # vitamin actives
    if any(x in n for x in ["niacinamide","retinol","tocopherol","ascorbic"]):
        return ("Vitamin Active", "Skin repair & brightening", "Safe")

    # fragrance
    if any(x in n for x in ["fragrance","parfum"]):
        return ("Fragrance", "Adds scent, may irritate skin", "High")

    # alcohols
    if "alcohol" in n:
        return ("Alcohol", "Quick drying & penetration", "High")

    # stabilizers & thickeners
    if any(x in n for x in ["gum","carbomer","polysorbate","dextrin"]):
        return ("Stabilizer", "Improves texture & stability", "Safe")

    # pH regulators
    if "citric acid" in n:
        return ("pH Regulator", "Balances pH", "Safe")

    return ("Support Ingredient", "Supports formulation", "Safe")


def analyze(ingredient_list):
    hydration = 0
    irritation = 0
    repair = 0

    print("\n🧴 SMART ANALYSIS\n")

    for ing in ingredient_list:
        category, function, risk = classify(ing)

        print(f"🔹 {ing}")
        print("Category:", category)
        print("Function:", function)

        if risk == "High":
            print("⚠️ Risk: HIGH\n")
            irritation += 2
        else:
            print("✅ Safe\n")

        if category in ["Humectant","Amino Acid"]:
            hydration += 1
        if category in ["Peptide Active","Vitamin Active"]:
            repair += 1

    print("\n🔎 PRODUCT SUMMARY")
    print("Hydration Support:", hydration)
    print("Skin Repair Support:", repair)
    print("Irritation Risk:", irritation)

    show_chart(hydration, repair, irritation)


def show_chart(h, r, i):
    plt.figure()
    plt.bar(["Hydration","Repair","Irritation"], [h,r,i])
    plt.title("Skin Impact Overview")
    plt.show()


# -------- RUN --------
text = input("\nPaste ingredients separated by comma:\n")
ingredients = [i.strip() for i in text.split(",")]
analyze(ingredients)