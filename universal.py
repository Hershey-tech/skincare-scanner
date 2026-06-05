import matplotlib.pyplot as plt

def classify(name):
    n = name.lower()

    # ---------- BASE SOLVENTS ----------
    if "water" in n or "aqua" in n:
        return ("Base", "Solvent base", "Safe")

    # ---------- HUMECTANTS ----------
    if any(x in n for x in ["glycerin","urea","hyaluronic","pca","lactate"]):
        return ("Humectant", "Hydration & moisture retention", "Safe")

    # ---------- AMINO ACIDS ----------
    if any(x in n for x in ["glycine","alanine","valine","arginine","proline","serine"]):
        return ("Amino Acid", "Repair & hydration support", "Safe")

    # ---------- PEPTIDES ----------
    if "peptide" in n:
        return ("Peptide Active", "Stimulates growth & repair", "Safe")

    # ---------- HAIR GROWTH ----------
    if any(x in n for x in ["caffeine","biotin","keratin"]):
        return ("Hair Growth Active", "Strengthens hair & boosts growth", "Safe")

    # ---------- BOTANICAL EXTRACT ----------
    if "extract" in n:
        return ("Botanical Extract", "Plant-based active benefits", "Safe")

    # ---------- EXFOLIANTS ----------
    if any(x in n for x in ["glycolic","salicylic","lactic","mandelic"]):
        return ("Exfoliant", "Removes dead cells & unclogs pores", "Moderate")

    # ---------- VITAMINS ----------
    if any(x in n for x in ["niacinamide","retinol","tocopherol","ascorbic","vitamin"]):
        return ("Vitamin", "Skin & cellular repair", "Safe")

    # ---------- SUNSCREEN FILTERS ----------
    if any(x in n for x in ["zinc oxide","titanium dioxide"]):
        return ("UV Filter", "Sun protection", "Safe")

    # ---------- SILICONES (hair & skin smoothing) ----------
    if any(x in n for x in ["dimethicone","siloxane"]):
        return ("Silicone", "Smoothness & protective barrier", "Safe")

    # ---------- FOOD / SUPPLEMENT SUGARS ----------
    if any(x in n for x in ["glucose","fructose","sucrose"]):
        return ("Sugar", "Energy source & sweetener", "Moderate")

    # ---------- PROTEIN SUPPLEMENTS ----------
    if any(x in n for x in ["whey","casein","soy protein","pea protein"]):
        return ("Protein", "Muscle repair & growth", "Safe")

    # ---------- VITAMIN SUPPLEMENTS ----------
    if any(x in n for x in ["b12","vitamin c","vitamin d","zinc","iron","magnesium"]):
        return ("Nutrient", "Essential body function support", "Safe")

    # ---------- PRESERVATIVES ----------
    if any(x in n for x in ["benzoate","paraben","sorbate"]):
        return ("Preservative", "Prevents microbial growth", "Safe")

    # ---------- IRRITANTS ----------
    if any(x in n for x in ["fragrance","parfum","alcohol"]):
        return ("Irritant", "May irritate sensitive skin", "High")

    # ---------- STABILIZERS ----------
    if any(x in n for x in ["gum","carbomer","polysorbate","dextrin"]):
        return ("Stabilizer", "Improves texture & stability", "Safe")

    return ("Support Ingredient", "Supports formulation", "Safe")


def analyze(ingredients):
    hydration = 0
    repair = 0
    irritation = 0
    nutrition = 0
    hair = 0

    print("\n🔬 UNIVERSAL INGREDIENT ANALYSIS\n")

    for ing in ingredients:
        category, function, risk = classify(ing)

        print(f"🔹 {ing}")
        print("Category:", category)
        print("Function:", function)

        if risk == "High":
            print("⚠️ Risk: HIGH\n")
            irritation += 2
        else:
            print("✅ Safe\n")

        if category == "Humectant":
            hydration += 1
        if category in ["Peptide Active","Vitamin","Amino Acid"]:
            repair += 1
        if category == "Hair Growth Active":
            hair += 1
        if category in ["Protein","Nutrient","Sugar"]:
            nutrition += 1

    print("\n🧠 PRODUCT INSIGHT")

    if hair >= 2:
        print("💇 Likely Hair Growth / Hair Care Product")

    if hydration >= 2:
        print("💧 Hydrating formulation")

    if repair >= 2:
        print("🛡 Repair & strengthening support")

    if nutrition >= 2:
        print("💊 Nutritional / supplement product")

    if irritation == 0:
        print("🌿 Gentle & safe formulation")

    show_chart(hydration, repair, hair, nutrition, irritation)


def show_chart(h, r, hair, nut, irr):
    labels = ["Hydration","Repair","Hair","Nutrition","Irritation"]
    values = [h, r, hair, nut, irr]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Ingredient Function Overview")
    plt.show()


# -------- RUN --------
text = input("\nPaste ingredients separated by comma:\n")
ingredients = [i.strip() for i in text.split(",")]
analyze(ingredients)