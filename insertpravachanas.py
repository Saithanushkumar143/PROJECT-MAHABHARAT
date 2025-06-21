from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to MongoDB
client = MongoClient("mongodb+srv://kurukshetramind:myfirstproject123@cluster0.lqecbti.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["kurukshetramind"]
collection = db["pravachanas"]

# Updated entries (without deleting older ones)
wisdom_entries = [
  {
    "_id": ObjectId("68337219c4e2b4ce54fa9e01"),
    "video_id": "A8PabF2P7bw",
    "youtube_link": "https://youtu.be/A8PabF2P7bw",
    "category": "Arjuna",
    "author": "Chaganti Koteswara Rao",
    "feeling": "Courage"
  },
  {
    "_id": ObjectId("68337219c4e2b4ce54fa9e02"),
    "video_id": "Ywv93sMdwJM",
    "youtube_link": "https://youtu.be/Ywv93sMdwJM",
    "category": "Krishna",
    "author": "Chaganti Koteswara Rao",
    "feeling": "Wisdom"
  },
  {
    "_id": ObjectId("68337219c4e2b4ce54fa9e03"),
    "video_id": "W-GFPephPic",
    "youtube_link": "https://youtu.be/W-GFPephPic",
    "category": "Arjuna",
    "author": "Chaganti Koteswara Rao",
    "feeling": "Empathy"
  },
  {
    "_id": ObjectId("68337219c4e2b4ce54fa9e04"),
    "video_id": "EOgP1j3te5A",
    "youtube_link": "https://youtu.be/EOgP1j3te5A",
    "category": "General",
    "author": "Chaganti Koteswara Rao",
    "feeling": "Inspiration"
  },
  {
    "_id": ObjectId("68337219c4e2b4ce54fa9e05"),
    "video_id": "yJSQ3JZD1Oc",
    "youtube_link": "https://youtu.be/yJSQ3JZD1Oc",
    "category": "General",
    "author": "Chaganti Koteswara Rao",
    "feeling": "Peace"
  },
  {
    "_id": ObjectId("68337219c4e2b4ce54fa9e06"),
    "video_id": "BvmfF9xXwi8",
    "youtube_link": "https://youtu.be/BvmfF9xXwi8",
    "category": "Arjuna",
    "author": "Chaganti Koteswara Rao",
    "feeling": "Confidence"
  },
  {
    "_id": ObjectId("68337219c4e2b4ce54fa9e07"),
    "video_id": "ftTg1vU-QF8",
    "youtube_link": "https://youtu.be/ftTg1vU-QF8",
    "category": "General",
    "author": "Garikipati Narasimha Rao",
    "feeling": "Wisdom"
  },
  {
    "_id": ObjectId("68337219c4e2b4ce54fa9e08"),
    "video_id": "UET_Y0K7PoY",
    "youtube_link": "https://youtu.be/UET_Y0K7PoY",
    "category": "General",
    "author": "Garikipati Narasimha Rao",
    "feeling": "Inspiration"
  },
  {
    "_id": ObjectId("68337219c4e2b4ce54fa9e09"),
    "video_id": "QbAyMLVp4Hk",
    "youtube_link": "https://youtu.be/QbAyMLVp4Hk",
    "category": "Yudhishthira",
    "author": "Garikipati Narasimha Rao",
    "feeling": "Integrity"
  },
  {
    "_id": ObjectId("68337219c4e2b4ce54fa9e0a"),
    "video_id": "3ezFJJR8QQk",
    "youtube_link": "https://youtu.be/3ezFJJR8QQk",
    "category": "General",
    "author": "Garikipati Narasimha Rao",
    "feeling": "Courage"
  },
  {
    "_id": ObjectId("68337219c4e2b4ce54fa9e0b"),
    "video_id": "25QAiZ3DHSM",
    "youtube_link": "https://youtu.be/25QAiZ3DHSM",
    "category": "General",
    "author": "Garikipati Narasimha Rao",
    "feeling": "Revelation"
  },
  {
    "_id": ObjectId("68337219c4e2b4ce54fa9e0c"),
    "video_id": "tysb3D-vGco",
    "youtube_link": "https://youtu.be/tysb3D-vGco",
    "category": "General",
    "author": "Chaganti Koteswara Rao",
    "feeling": "Reflection"
  },
  {
    "_id": ObjectId("68337219c4e2b4ce54fa9e0d"),
    "video_id": "kT8FSrBcLA8",
    "youtube_link": "https://youtu.be/kT8FSrBcLA8",
    "category": "Vyasa",
    "author": "Garikipati Narasimha Rao",
    "feeling": "Gratitude"
  },
  {
    "_id": ObjectId("68337219c4e2b4ce54fa9e0e"),
    "video_id": "IwcIMbg_PlM",
    "youtube_link": "https://youtu.be/IwcIMbg_PlM",
    "category": "Dhritarashtra",
    "author": "Garikipati Narasimha Rao",
    "feeling": "Conflict"
  },
  {
    "_id": ObjectId("68337219c4e2b4ce54fa9e0f"),
    "video_id": "5jX20h6HWzg",
    "youtube_link": "https://youtu.be/5jX20h6HWzg",
    "category": "General",
    "author": "Garikipati Narasimha Rao",
    "feeling": "Mystery"
  },
  # ... continue up to ~30 total entries ...
]


# Insert into MongoDB (this will raise DuplicateKeyError if _id already exists)
try:
    collection.insert_many(wisdom_entries, ordered=False)
    print("✅ Empowering Mahabharata wisdom has been successfully inserted!")
except Exception as e:
    print(f"⚠️ Some entries might already exist or another issue occurred:\n{e}")
