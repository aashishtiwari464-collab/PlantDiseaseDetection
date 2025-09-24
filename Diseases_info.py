# WARNING: This information is for educational purposes only. Always consult a local
# agricultural expert or extension service for accurate diagnosis and treatment plans.
# Misapplication of treatments can harm plants, the environment, and human health.
# Always follow local regulations and product labels for any chemical application.

DISEASE_INFO = {
    # == Pepper Classes ==
    "Pepper__bell___Bacterial_spot": {
        "description": "A common and destructive bacterial disease caused by several species of Xanthomonas. It thrives in warm, wet conditions and can spread rapidly.",
        "symptoms": [
            "Small, water-soaked, dark, raised spots on leaves, which may have a yellow halo.",
            "Spots may merge, causing leaves to yellow and drop.",
            "Raised, scab-like spots can appear on the fruit, making it unmarketable."
        ],
        "treatment": {
            "organic": "Apply copper-based bactericides. However, bacterial resistance to copper is common. Serenade (Bacillus subtilis) can also be used.",
            "chemical": "Use bactericides containing copper hydroxide or streptomycin (note: streptomycin use may be restricted in some areas)."
        },
        "prevention": "Use certified disease-free seeds and transplants. Rotate crops, avoiding planting peppers or tomatoes in the same spot for at least 3 years. Avoid overhead watering to keep foliage dry. Remove and destroy infected plants immediately."
    },
    "Pepper__bell___healthy": {
        "description": "The plant shows no signs of disease or pest infestation, exhibiting vigorous growth, normal color, and healthy fruit development.",
        "maintenance_tips": [
            "Ensure consistent watering and well-drained soil.",
            "Provide balanced fertilizer according to growth stage.",
            "Monitor regularly for early signs of pests or diseases.",
            "Ensure good air circulation through proper spacing and pruning."
        ],
        "symptoms": None,
        "treatment": None,
        "prevention": "Continue best practices for watering, fertilization, and pest monitoring."
    },

    # == Potato Classes ==
    "Potato___Early_blight": {
        "description": "A common fungal disease caused by Alternaria solani. It primarily affects leaves and tubers and is often seen in humid weather.",
        "symptoms": [
            "Dark, circular spots with concentric rings, creating a 'target' or 'bull's-eye' pattern on lower, older leaves.",
            "Yellowing of the area surrounding the spots.",
            "Lesions can also appear on stems and tubers."
        ],
        "treatment": {
            "organic": "Apply copper-based fungicides or bio-fungicides containing Bacillus subtilis.",
            "chemical": "Fungicides containing Chlorothalonil, Mancozeb, or Azoxystrobin are effective. Rotate fungicide types to prevent resistance."
        },
        "prevention": "Practice crop rotation (3-year rotation recommended). Use certified disease-free seed potatoes. Maintain plant health with proper nutrition and watering. Destroy crop debris after harvest."
    },
    "Potato___Late_blight": {
        "description": "An infamous and highly destructive disease caused by the oomycete (water mold) Phytophthora infestans. It thrives in cool, moist conditions and can destroy a crop in a matter of days. This is the pathogen responsible for the Irish Potato Famine.",
        "symptoms": [
            "Large, dark green to black, water-soaked lesions on leaves and stems, often appearing greasy.",
            "A white, fuzzy mold may appear on the underside of leaves in high humidity.",
            "Infected tubers develop a reddish-brown, dry rot that penetrates deep into the potato."
        ],
        "treatment": {
            "organic": "Copper-based fungicides can offer some protection but must be applied preventatively. Not effective once the infection is established.",
            "chemical": "Systemic fungicides are required. Products containing cymoxanil, dimethomorph, or propamocarb are common. Requires aggressive and timely application."
        },
        "prevention": "Use certified disease-free seed potatoes. Plant resistant varieties if available. Ensure good air circulation and drainage. Destroy volunteer potato plants and cull piles. Monitor weather forecasts for high-risk conditions."
    },
    "Potato___healthy": {
        "description": "The plant exhibits strong, upright stems, lush green foliage without spots or yellowing, and is developing tubers correctly.",
        "maintenance_tips": [
            "Maintain consistent soil moisture, especially during tuber formation.",
            "'Hill' soil around the base of the plant to protect developing tubers from sunlight and pests.",
            "Monitor for key pests like the Colorado potato beetle."
        ],
        "symptoms": None,
        "treatment": None,
        "prevention": "Follow proper hilling, watering, and nutrient management practices."
    },

    # == Tomato Classes ==
    "Tomato_Bacterial_spot": {
        "description": "Similar to Pepper Bacterial Spot, this disease is caused by Xanthomonas species and affects all above-ground parts of the tomato plant.",
        "symptoms": [
            "Small, water-soaked, irregular dark spots on leaves and stems.",
            "Unlike fungal spots, these do not typically have a 'target' look.",
            "Fruit spots are slightly raised and scabby."
        ],
        "treatment": {
            "organic": "Copper-based bactericides are the primary organic option, but effectiveness is limited and resistance is a major issue.",
            "chemical": "A combination of copper and mancozeb can be more effective than copper alone. Actigard (acibenzolar-S-methyl) can help induce the plant's natural defenses."
        },
        "prevention": "Use disease-free seeds (hot water treatment can help). Practice a 3-year crop rotation away from peppers and tomatoes. Stake plants to improve air circulation. Avoid working with plants when they are wet."
    },
    "Tomato_Early_blight": {
        "description": "Caused by the fungus Alternaria solani, the same pathogen that affects potatoes. It usually appears on lower leaves after fruit set.",
        "symptoms": [
            "Dark, concentric 'target' spots on lower leaves.",
            "Stem lesions are dark and slightly sunken (collar rot).",
            "Fruit can be infected near the stem, showing large, sunken black spots with concentric rings."
        ],
        "treatment": {
            "organic": "Copper fungicides or products with Bacillus subtilis (e.g., Serenade).",
            "chemical": "Fungicides containing Chlorothalonil or Mancozeb. Apply preventatively."
        },
        "prevention": "Mulch at the base of plants to prevent spore splash from the soil. Prune lower leaves. Ensure good air circulation. Rotate crops."
    },
    "Tomato_Late_blight": {
        "description": "Caused by Phytophthora infestans, the same water mold affecting potatoes. It is extremely destructive in cool, wet weather.",
        "symptoms": [
            "Large, greasy-looking, grey-green or brown patches on leaves.",
            "White fungal growth may appear on the underside of leaves.",
            "Fruit develops large, firm, brown, greasy spots that can rot the entire fruit."
        ],
        "treatment": {
            "organic": "Preventative application of copper fungicides is the only option, with very limited effectiveness once established.",
            "chemical": "Aggressive application of targeted fungicides is necessary. Rotate chemicals to prevent resistance."
        },
        "prevention": "Plant resistant varieties. Ensure ample spacing for air flow. Avoid overhead watering. Monitor weather and apply preventative fungicides when late blight is forecast."
    },
    "Tomato_Leaf_Mold": {
        "description": "A fungal disease caused by Passalora fulva, primarily affecting tomatoes grown in greenhouses or high-humidity environments.",
        "symptoms": [
            "Pale green or yellowish spots on the upper surface of leaves.",
            "The key diagnostic sign is a velvety, olive-green to brownish mold on the underside of the leaves, corresponding to the yellow spots above."
        ],
        "treatment": {
            "organic": "Improve ventilation and reduce humidity. Copper sprays or biofungicides can be used.",
            "chemical": "Fungicides containing Chlorothalonil or Mancozeb."
        },
        "prevention": "Choose resistant varieties. Ensure excellent air circulation and low humidity. Prune lower leaves. Water in the morning so foliage dries quickly."
    },
    "Tomato_Septoria_leaf_spot": {
        "description": "A very common fungal disease caused by Septoria lycopersici, which thrives in wet, humid conditions and primarily affects the leaves.",
        "symptoms": [
            "Numerous small, circular spots (about 1/8 inch) with dark brown borders and lighter tan or gray centers.",
            "Tiny black specks (pycnidia, the fungal fruiting bodies) can be seen in the center of the spots.",
            "Starts on lower leaves and progresses up the plant."
        ],
        "treatment": {
            "organic": "Copper-based fungicides or neem oil.",
            "chemical": "Chlorothalonil or Mancozeb-based fungicides."
        },
        "prevention": "Mulch heavily to prevent spore splash. Water at the base of the plant. Improve air circulation. Remove and destroy infected leaves promptly. Practice crop rotation."
    },
    "Tomato_Spider_mites_Two_spotted_spider_mite": {
        "description": "Caused by a tiny arachnid pest (Tetranychus urticae), not a disease. They feed by piercing plant cells to suck out the contents, thriving in hot, dry conditions.",
        "symptoms": [
            "Fine white or yellow stippling (tiny dots) on the leaves.",
            "As infestation grows, leaves may turn yellow or bronze and become dry.",
            "Fine, silky webbing may be visible on the underside of leaves and between stems."
        ],
        "treatment": {
            "organic": "Strong jet of water to knock them off. Apply insecticidal soap or neem oil, ensuring thorough coverage of the underside of leaves. Release predatory mites (Phytoseiulus persimilis).",
            "chemical": "Use a miticide (not a general insecticide, which can kill predators and worsen the problem). Products containing abamectin or bifenthrin are effective."
        },
        "prevention": "Keep plants well-watered to avoid drought stress. Regularly inspect the underside of leaves. Increase humidity where possible."
    },
    "Tomato__Target_Spot": {
        "description": "A fungal disease caused by Corynespora cassiicola. It can affect leaves, stems, and fruit, and is common in warm, humid climates.",
        "symptoms": [
            "Spots on leaves that resemble Early Blight but often have a darker center with less-defined concentric rings, creating a 'shot-hole' appearance as the center may fall out.",
            "Fruit lesions are deeply pitted and circular.",
            "Can be difficult to distinguish from Early Blight without lab analysis."
        ],
        "treatment": {
            "organic": "Copper fungicides can provide some control.",
            "chemical": "Fungicides containing mancozeb, chlorothalonil, or strobilurins."
        },
        "prevention": "Practice crop rotation. Maintain good air circulation. Remove and destroy infected plant debris. Avoid overhead irrigation."
    },
    "Tomato__Tomato_YellowLeaf__Curl_Virus": {
        "description": "A devastating viral disease transmitted primarily by the silverleaf whitefly. There is no cure for an infected plant.",
        "symptoms": [
            "Severe stunting of the plant.",
            "Upward curling, yellowing, and distortion of the leaves.",
            "Leaves are often smaller than normal.",
            "Significant reduction or complete loss of fruit production."
        ],
        "treatment": {
            "organic": "No cure. Focus on controlling the whitefly vector using insecticidal soaps, neem oil, or introducing natural predators like lacewings.",
            "chemical": "Use systemic insecticides to control whiteflies, but resistance is a major issue. Reflective mulches can help repel whiteflies."
        },
        "prevention": "The only effective strategy. Use virus-resistant tomato varieties. Control whitefly populations. Remove and immediately destroy infected plants to prevent spread. Use protective row covers on young plants."
    },
    "Tomato__Tomato_mosaic_virus": {
        "description": "A viral disease (ToMV) that can persist in seeds and soil. It is easily transmitted by mechanical means (hands, tools, etc.).",
        "symptoms": [
            "A light green and dark green mosaic or mottled pattern on the leaves.",
            "Leaf curling, distortion, and yellowing.",
            "Stunted plant growth and reduced fruit yield.",
            "Internal browning of fruit can occur."
        ],
        "treatment": {
            "organic": "None. There is no cure for viral diseases.",
            "chemical": "None."
        },
        "prevention": "Use certified disease-free seeds and resistant varieties. Do not use tobacco products near plants (Tobacco Mosaic Virus is related and can cross-infect). Disinfect tools regularly. Wash hands after handling plants. Remove and destroy infected plants."
    },
    "Tomato_healthy": {
        "description": "A healthy tomato plant displays vibrant green leaves, steady growth, strong stems, and is actively flowering and setting fruit appropriate for its age and variety.",
        "maintenance_tips": [
            "Provide consistent moisture, avoiding both drought and waterlogging.",
            "Support the plant with stakes or cages to keep fruit off the ground.",
            "Fertilize appropriately, reducing nitrogen once fruit begins to set to encourage fruit production over foliage growth.",
            "Prune suckers to improve air circulation and direct energy to fruit."
        ],
        "symptoms": None,
        "treatment": None,
        "prevention": "Continue good cultural practices: proper watering, fertilizing, pruning, and support."
    }
}
