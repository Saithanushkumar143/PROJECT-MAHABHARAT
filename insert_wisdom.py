from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  
db = client["kurukshetramind"]  
collection = db["wisdom"]  

# Sample Entries
wisdom_entries = [
    {
        "category": "Duty vs. Emotion",
        "scenario": "Arjuna hesitated to fight in the war due to emotional attachments.",
        "characters": ["Arjuna", "Krishna"],
        "lesson": "One must fulfill their dharma (duty) without attachment. Krishna advised Arjuna to act with detachment.",
        "shloka": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।"  # Bhagavad Gita 2.47
    },
    {
        "category": "Leadership",
        "scenario": "Yudhishthira’s commitment to truth and dharma, even in tough times.",
        "characters": ["Yudhishthira"],
        "lesson": "A leader must uphold dharma even when challenged. Integrity builds trust.",
        "shloka": "सत्यं वद, धर्मं चर।"  # Vedic wisdom on truth
    },
    {
        "category": "Friendship",
        "scenario": "Karna remained loyal to Duryodhana despite knowing he was on the wrong side.",
        "characters": ["Karna", "Duryodhana"],
        "lesson": "Loyalty is valuable, but blind loyalty can lead to downfall. Choose your allegiance wisely.",
        "shloka": "सखा त्वं मे प्रियः सखा च सदा।"
    },
    {
        "category": "Sacrifice",
        "scenario": "Abhimanyu enters the Chakravyuha formation, knowing he may not survive.",
        "characters": ["Abhimanyu"],
        "lesson": "True warriors are willing to sacrifice for a greater cause, even in the face of certain death.",
        "shloka": "वीर भोग्य वसुंधरा।"  # The brave inherit the earth
    },
    {
        "category": "Deception vs. Righteousness",
        "scenario": "Krishna uses deception (Ashwathama's name) to demoralize Drona.",
        "characters": ["Krishna", "Drona", "Yudhishthira"],
        "lesson": "Sometimes, bending the truth is necessary to uphold dharma.",
        "shloka": "धर्मो रक्षति रक्षितः।"  # Dharma protects those who protect it
    },
    {
        "category": "Loyalty and Betrayal",
        "scenario": "Vibhishana, Ravana's brother, joins Rama's side despite being blood-related to the enemy.",
        "characters": ["Vibhishana", "Ravana", "Rama"],
        "lesson": "Righteousness holds greater value than blood relations.",
        "shloka": "सत्यं वद, धर्मं चर।"  # Speak the truth, follow dharma
    },
    {
        "category": "Greed and Its Consequences",
        "scenario": "Shakuni manipulates Duryodhana, leading to the dice game.",
        "characters": ["Shakuni", "Duryodhana", "Yudhishthira"],
        "lesson": "Greed blinds wisdom and leads to self-destruction.",
        "shloka": "लोभः पापस्य कारणम्।"  # Greed is the cause of sin
    },
    {
        "category": "Feminine Strength",
        "scenario": "Draupadi demands justice in the Kuru court despite being humiliated.",
        "characters": ["Draupadi", "Kauravas", "Pandavas"],
        "lesson": "Courage and dignity in the face of injustice can spark revolution.",
        "shloka": "अधर्मो धर्मो भवति।"  # Injustice turns into justice over time
    },
    {
        "category": "Patience and Perseverance",
        "scenario": "Kunti raises her sons alone after Pandu's death.",
        "characters": ["Kunti", "Pandavas"],
        "lesson": "Patience and unwavering determination lead to success.",
        "shloka": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।"  # Do your duty without expecting rewards
    },
    {
        "category": "Wisdom of Detachment",
        "scenario": "Bhishma, lying on the bed of arrows, imparts wisdom to Yudhishthira.",
        "characters": ["Bhishma", "Yudhishthira"],
        "lesson": "True wisdom comes from detachment from material desires.",
        "shloka": "न कर्मणामनारम्भान्नैष्कर्म्यं पुरुषोऽश्नुते।"  # Detachment from action does not lead to inaction
    },
    {
        "category": "Karma and Consequences",
        "scenario": "Karna, despite being generous, faces a tragic end due to past sins.",
        "characters": ["Karna", "Krishna", "Arjuna"],
        "lesson": "One cannot escape the consequences of their karma.",
        "shloka": "कर्मणो ह्यपि बोद्धव्यं बोद्धव्यं च विकर्मणः।"  # One must understand karma and its consequences
    },
    {
        "category": "Destiny and Free Will",
        "scenario": "Krishna reveals the Vishwaroopa form, showing Arjuna the inevitable destiny.",
        "characters": ["Krishna", "Arjuna"],
        "lesson": "Destiny is inevitable, but free will determines our journey.",
        "shloka": "निमित्तमात्रं भव सव्यसाचिन्।"  # Be an instrument of divine will
    },
    {
        "category": "Humility and Greatness",
        "scenario": "Krishna, the supreme god, humbly serves as Arjuna’s charioteer.",
        "characters": ["Krishna", "Arjuna"],
        "lesson": "True greatness lies in humility and service.",
        "shloka": "न हि ज्ञानेन सदृशं पवित्रमिह विद्यते।"  # Nothing is more purifying than wisdom
    }
]

    

# Insert data into MongoDB
collection.insert_many(wisdom_entries)

print("✅ Mahabharata wisdom data inserted successfully!")
