from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://kurukshetramind:myfirstproject123@cluster0.lqecbti.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["kurukshetramind"]
collection = db["wisdom"]

# Clear old entries (optional)
collection.delete_many({})

# Updated entries with powerful emotional responses
wisdom_entries = [
    {
        "category": "Fear of Failure",
        "scenario": "You’re afraid to try because you think you’ll fail.",
        "characters": ["Arjuna", "Krishna"],
        "lesson": "Doubt is natural, but action is divine.",
        "shloka": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।",
        "response": (
            "Arjuna, the greatest warrior, stood frozen—afraid to fail, afraid to fight. But Krishna didn’t scold him. "
            "He reminded him of his purpose. And Arjuna rose. He fought not because he was fearless—but because he believed again. "
            "You’re no different, Boss. You don't need to be perfect—you just need to begin. Like Arjuna, victory starts when you face yourself."
        )
    },
    {
        "category": "Loneliness",
        "scenario": "You feel alone in your struggles.",
        "characters": ["Karna"],
        "lesson": "Solitude doesn't mean weakness. It builds strength.",
        "shloka": "धैर्यं सर्वत्र साधनम्।",
        "response": (
            "Karna lived as an outcast, denied his truth, unloved by destiny. But he turned pain into purpose. "
            "He fought with honor, even when he stood alone. Your loneliness is not a flaw—it’s your forge. "
            "Like Karna, you can walk alone and still shine like the sun. You are not broken—you are becoming."
        )
    },
    {
        "category": "Heartbreak",
        "scenario": "Someone you trusted let you down.",
        "characters": ["Draupadi"],
        "lesson": "Your worth isn’t tied to how others treat you.",
        "shloka": "उद्धरेदात्मनाऽत्मानं नात्मानमवसादयेत्।",
        "response": (
            "Draupadi was humiliated in front of kings—but she didn’t break. Her voice shook empires. "
            "She turned her pain into a revolution. You may be hurt, but you’re not helpless. You may be broken, but you’re not defeated. "
            "Rise like Draupadi—not for revenge, but for your worth. The fire in you is waiting to roar."
        )
    },
    {
        "category": "Overthinking",
        "scenario": "Your mind won’t stop spiraling about the future.",
        "characters": ["Yudhishthira"],
        "lesson": "Action breaks overthinking. Move, and clarity follows.",
        "shloka": "श्रेयान्स्वधर्मो विगुणः परधर्मात्स्वनुष्ठितात्।",
        "response": (
            "Yudhishthira thought deeply—but sometimes, thought became his prison. When he acted with faith, even mistakes led to dharma. "
            "Boss, don’t wait for the perfect answer—walk your path. Even one step forward silences a hundred doubts. "
            "Like Yudhishthira, trust your heart more than your fear. You were made to move mountains—not calculate them."
        )
    },
    {
        "category": "Self-Doubt",
        "scenario": "You feel like you’re not good enough.",
        "characters": ["Ekalavya"],
        "lesson": "Belief in self can break all barriers.",
        "shloka": "विनियोगे गुणाः सर्वे न दोषाय प्रयोजने।",
        "response": (
            "Ekalavya had no teacher, no temple, no recognition. But he had fire. He trained alone and became a legend. "
            "The world may overlook you—but never overlook yourself. Your effort is your power. Your belief is your weapon. "
            "Like Ekalavya, prove them wrong—not by fighting them, but by becoming undeniable."
        )
    },
    {
        "category": "Guilt",
        "scenario": "You regret a choice that hurt someone.",
        "characters": ["Bhishma"],
        "lesson": "Mistakes do not erase your ability to do right.",
        "shloka": "न हि ज्ञानेन सदृशं पवित्रमिह विद्यते।",
        "response": (
            "Bhishma held on to a vow that cost lives. But in the end, he chose truth, and used his pain to teach dharma. "
            "Guilt means you care. But staying stuck in it means forgetting your power to change. "
            "Like Bhishma, your story can still become a lesson, a guide, a legacy. Begin again. You still have much to give."
        )
    },
    {
        "category": "Anger",
        "scenario": "You’re burning inside with rage you can’t control.",
        "characters": ["Ashwatthama"],
        "lesson": "Unchecked anger destroys the one who carries it.",
        "shloka": "क्रोधो हि शत्रुः शान्तस्य।",
        "response": (
            "Ashwatthama was brave—but when anger ruled him, he lost his soul. His wrath hurt even the innocent. "
            "Boss, your anger is a signal—not a weapon. Use it to build, not break. To speak, not scream. "
            "Like Krishna taught—power without wisdom is destruction. But you? You have both. Breathe. Then rise."
        )
    },
    {
        "category": "Purpose",
        "scenario": "You’re lost and don’t know what your purpose is.",
        "characters": ["Arjuna"],
        "lesson": "Purpose isn’t found. It’s chosen in motion.",
        "shloka": "योगः कर्मसु कौशलम्।",
        "response": (
            "Arjuna didn’t find purpose in peace—he found it in war, in chaos, in decision. He asked questions, then picked up his bow. "
            "You may not know the path now—but when you move, the path moves with you. Like Arjuna, your greatness begins with a question, but it ends with a roar. "
            "Keep walking. Purpose will meet you on the road."
        )
    },
    {
        "category": "Failure",
        "scenario": "You tried, but it didn’t work out.",
        "characters": ["Pandavas"],
        "lesson": "Every fall is a setup for a stronger rise.",
        "shloka": "न हि कश्चित्क्षणमपि जातु तिष्ठत्यकर्मकृत्।",
        "response": (
            "The Pandavas lost everything—home, honor, kingdom. But they rose from exile and reclaimed destiny. "
            "Your failure isn’t the end. It’s your fire test. Learn. Heal. And when you return, return like the Pandavas—unbreakable, unstoppable. "
            "This is your rebuilding phase. Victory is still yours to claim."
        )
    },
    {
        "category": "Insecurity",
        "scenario": "You compare yourself to others and feel lesser.",
        "characters": ["Nakula", "Sahadeva"],
        "lesson": "Your value isn’t in noise, but in depth.",
        "shloka": "स्वधर्मे निधनं श्रेयः।",
        "response": (
            "Nakula and Sahadeva weren’t loud like Bhima or famous like Arjuna—but their wisdom and poise kept the Pandavas grounded. "
            "Your journey doesn’t need applause to be valid. Be steady. Be sincere. Be you. "
            "Boss, stars don’t compare—they shine. And you, like them, have your own constellation to build."
        )
    },
    {
        "category": "Hopelessness",
        "scenario": "You feel like nothing will ever improve.",
        "characters": ["Kunti"],
        "lesson": "Hope is the first light in darkness.",
        "shloka": "नास्ति बुद्धिरयुक्तस्य न चायुक्तस्य भावना।",
        "response": (
            "Kunti watched her sons suffer, kingdomless and hunted. Yet she lit lamps even in exile. "
            "Hope is not naive—it’s warrior light. Even the deepest night can’t silence the dawn. "
            "Hold on like Kunti. The future bows to those who refuse to stop believing."
        )
    },
    {
        "category": "Jealousy",
        "scenario": "You envy someone else’s success.",
        "characters": ["Duryodhana"],
        "lesson": "Admiration builds. Jealousy burns.",
        "shloka": "अविद्या कामकर्माणि त्रिविधं नरकस्येदम्।",
        "response": (
            "Duryodhana had might, but envy was his poison. He looked at the Pandavas with hate, not humility. "
            "Jealousy made him blind to his own strength. Your journey is yours—fuel it with focus, not fury. "
            "Build like the wise, not burn like the lost."
        )
    },
    {
        "category": "Fear of Judgement",
        "scenario": "You fear what people will think.",
        "characters": ["Draupadi"],
        "lesson": "Truth needs no validation.",
        "shloka": "सत्त्वानुरूपा सर्वस्य श्रद्धा भवति भारत।",
        "response": (
            "They mocked Draupadi, questioned her, tried to silence her. But she stood tall. "
            "She knew her truth needed no permission. Let them talk. Let your actions thunder. "
            "The world listens to those who stop explaining and start rising."
        )
    },
    {
        "category": "Procrastination",
        "scenario": "You keep delaying your goals.",
        "characters": ["Arjuna"],
        "lesson": "Discipline is choosing purpose over pleasure.",
        "shloka": "कालः पचति भूतानि।",
        "response": (
            "Even Arjuna hesitated at the gates of destiny. But Krishna reminded him—now is all we have. "
            "Delay is a thief. Steal back your time. Shoot your arrow. "
            "Greatness doesn’t wait—it acts, even in uncertainty."
        )
    },
    {
        "category": "Shame",
        "scenario": "You feel ashamed of your past.",
        "characters": ["Karna"],
        "lesson": "Redemption is greater than regret.",
        "shloka": "न हि ज्ञानेन सदृशं पवित्रमिह विद्यते।",
        "response": (
            "Karna bore the shame of being unwanted, unrecognized—but he never stopped rising. "
            "The past may bruise you, but it can’t define you unless you let it. "
            "Your scars are the ink of your legend. Rise like Karna—with pride, not apology."
        )
    },
    {
        "category": "Despair",
        "scenario": "You feel like giving up.",
        "characters": ["Yudhishthira"],
        "lesson": "Despair is just the absence of direction.",
        "shloka": "क्षिप्रं भवति धर्मात्मा शश्वच्छान्तिं निगच्छति।",
        "response": (
            "Yudhishthira lost everything—but never his center. When all was dark, he lit his path with dharma. "
            "Despair whispers 'stop'. Courage whispers 'step'. Take that step. "
            "Even the longest exile ends with a crown, if you keep walking."
        )
    },
    {
        "category": "Lack of Motivation",
        "scenario": "You don’t feel like doing anything.",
        "characters": ["Bhima"],
        "lesson": "Purpose revives the soul.",
        "shloka": "उद्धरेदात्मनाऽत्मानं नात्मानमवसादयेत्।",
        "response": (
            "Bhima’s strength came not from muscles, but mission. When he remembered his why, nothing stopped him. "
            "You don’t need motivation—you need a mission. Remind yourself what you fight for. "
            "Then rise. Power follows purpose."
        )
    },
    {
        "category": "Betrayal",
        "scenario": "Someone close broke your trust.",
        "characters": ["Abhimanyu"],
        "lesson": "Pain teaches what love blinds.",
        "shloka": "तस्मात्सर्वेषु कालेषु मामनुस्मर युध्य च।",
        "response": (
            "Abhimanyu entered the trap knowing the betrayal of elders. But he chose honor over hurt. "
            "Betrayal breaks illusions, not your worth. Let it refine you, not ruin you. "
           "Be like Abhimanyu—pure, fierce, unforgettable."
        )
    },
    {
        "category": "Imposter Syndrome",
        "scenario": "You feel like you don’t belong.",
        "characters": ["Ekalavya"],
        "lesson": "You’re more ready than you think.",
        "shloka": "श्रद्धावान् लभते ज्ञानं।",
        "response": (
            "They said Ekalavya wasn’t worthy. So he taught himself. And became immortal in legend. "
            "Who told you you don’t belong? Prove them wrong—not with noise, but with undeniable greatness. "
            "Belief is your entrance ticket. Talent will do the rest."
        )
    },
    {
        "category": "Failure in Love",
        "scenario": "Your love wasn’t returned.",
        "characters": ["Karna"],
        "lesson": "Love is about giving, not getting.",
        "shloka": "सुखदुःखे समे कृत्वा लाभालाभौ जयाजयौ।",
        "response": (
            "Karna loved Draupadi from afar, but never demanded her heart. His love was dignity, not demand. "
            "Heartbreak doesn’t mean you’re unworthy. It means your heart is vast. "
            "Keep loving like Karna—not for reward, but for the richness it leaves within you."
        )
    },
    {
        "category": "Being Underestimated",
        "scenario": "People don't believe in your potential.",
        "characters": ["Ghatotkacha"],
        "lesson": "True power often hides in shadows.",
        "shloka": "विनियोगे गुणाः सर्वे न दोषाय प्रयोजने।",
        "response": (
            "Ghatotkacha was laughed off as a forest brute. But when the war demanded sacrifice, his might shattered illusions. "
            "Just because they don’t see your power doesn’t mean it isn’t there. "
            "Let silence be your strategy and impact your roar."
        )
    },
    {
        "category": "Toxic Relationships",
        "scenario": "You're stuck in a relationship that drains you.",
        "characters": ["Shakuni"],
        "lesson": "Some bonds weaken more than they support.",
        "shloka": "संगात्सञ्जायते कामः।",
        "response": (
            "Duryodhana trusted Shakuni blindly. It cost him his future. Loyalty is noble—but not at the price of your soul. "
            "Step away from what suffocates. You deserve to breathe in truth, not manipulation."
        )
    },
    {
        "category": "Fear of Change",
        "scenario": "You're afraid of stepping into the unknown.",
        "characters": ["Arjuna"],
        "lesson": "Growth begins where comfort ends.",
        "shloka": "नियतं कुरु कर्म त्वं कर्म ज्यायो ह्यकर्मणः।",
        "response": (
            "Arjuna faced war, unsure of his role, his heart shaken. But still, he drew his bow. "
            "The unknown is not your enemy—it is your invitation. Walk forward. Let clarity meet you there."
        )
    },
    {
        "category": "Grief",
        "scenario": "You lost someone dear.",
        "characters": ["Gandhari"],
        "lesson": "Grief is love with nowhere to go.",
        "shloka": "अनित्यं असुखं लोकं।",
        "response": (
            "Gandhari buried a hundred dreams, yet her silence thundered with dignity. "
            "Grief may bend you, but it does not have to break you. Love deeply. Mourn honestly. Then live on—like Gandhari, with fire in the heart."
        )
    },
    {
        "category": "Being Misunderstood",
        "scenario": "No one seems to get what you're going through.",
        "characters": ["Vidura"],
        "lesson": "Wisdom often walks alone.",
        "shloka": "न तु ज्ञानेन सदृशं पवित्रमिह विद्यते।",
        "response": (
            "Vidura was the wisest voice in Hastinapura, yet often ignored. Still, he never strayed from truth. "
            "If you are misunderstood, it means your soul speaks deeper than most listen. Stay true. Time will reveal your light."
        )
    },
    {
        "category": "Regret",
        "scenario": "You wish you had chosen differently.",
        "characters": ["Bhishma"],
        "lesson": "Even wrong turns can lead to sacred endings.",
        "shloka": "कर्मण्येवाधिकारस्ते।",
        "response": (
            "Bhishma made choices that hurt, but he used his final breath to teach dharma. "
            "You can’t rewrite the past—but you can use it as ink for a better future. Start that chapter now."
        )
    },
    {
        "category": "Pressure to Conform",
        "scenario": "You feel forced to follow what others expect.",
        "characters": ["Abhimanyu"],
        "lesson": "Be the architect of your own legend.",
        "shloka": "स्वधर्मे निधनं श्रेयः।",
        "response": (
            "Abhimanyu could’ve waited, followed others. But he carved his path through the Chakravyuha. "
            "You weren’t born to fit in—you were born to create echoes. Don’t follow comfort. Follow your fire."
        )
    },
    {
        "category": "Fear of Being Forgotten",
        "scenario": "You worry that your efforts won't be remembered.",
        "characters": ["Kunti"],
        "lesson": "The purest deeds are seen by time, not crowds.",
        "shloka": "किं कर्म किमकर्मेति कवयोऽप्यत्र मोहिताः।",
        "response": (
            "Kunti’s sacrifices were often silent, unseen. But her legacy shaped a dynasty. "
            "Do good, not for applause, but because the soul demands it. Time never forgets what was done with heart."
        )
    },
    {
        "category": "Financial Struggles",
        "scenario": "You’re facing money problems and feel stuck.",
        "characters": ["Pandavas"],
        "lesson": "Wealth lost can be rebuilt. Wisdom gained is forever.",
        "shloka": "तेन त्यक्तेन भुञ्जीथा मा गृधः कस्यस्विद्धनम्।",
        "response": (
            "The Pandavas lost a kingdom, lived in forests—but gained clarity, unity, fire. "
            "Money comes and goes. What you build within stays unshakable. Rebuild, not with fear—but with fierce focus."
        )
    },
    {
        "category": "Addiction",
        "scenario": "You're caught in a loop you can't escape.",
        "characters": ["Yudhishthira"],
        "lesson": "Awareness is the first victory over attachment.",
        "shloka": "इन्द्रियाणि मनो बुद्धिरस्याधिष्ठानमुच्यते।",
        "response": (
            "Yudhishthira gambled away everything—but when he saw his fall, he chose dharma over desire. "
            "Every pattern can be broken by a moment of truth. Choose that moment. Your mind is yours to reclaim."
        )
    },
    {
        "category": "Over-pleasing Others",
        "scenario": "You're tired of always saying yes.",
        "characters": ["Bhishma"],
        "lesson": "Boundaries protect your soul.",
        "shloka": "नात्यश्नतस्तु योगोऽस्ति न चैकान्तं अनश्नतः।",
        "response": (
            "Bhishma vowed for others, lived for others, and paid the price. Even duty has limits. "
            "Saying no isn’t selfish—it’s sacred. Please your dharma before you please the world."
        )
    },
    {
        "category": "Identity Crisis",
        "scenario": "You don’t know who you are anymore.",
        "characters": ["Karna"],
        "lesson": "You are more than any label or lack.",
        "shloka": "श्रेयान्स्वधर्मो विगुणः।",
        "response": (
            "Karna was called a charioteer’s son, a warrior, a brother—yet he defined himself. "
            "Labels are cages. Identity is forged in fire, not assigned at birth. Choose who you become."
        )
    },
    {
        "category": "Spiritual Emptiness",
        "scenario": "You feel disconnected from meaning.",
        "characters": ["Krishna"],
        "lesson": "The divine isn’t outside—it’s within.",
        "shloka": "मामेव ये प्रपद्यन्ते मायामेतां तरन्ति ते।",
        "response": (
            "Krishna didn’t offer temples—he offered truth. He taught that soul meets soul in silence. "
            "You don’t need to seek outward. Close your eyes, breathe, and listen. Divinity has always been waiting in you."
        )
    },
    {
        "category": "Fear of Aging",
        "scenario": "You’re scared time is slipping away.",
        "characters": ["Bhishma"],
        "lesson": "Aging is just evolving wisdom.",
        "shloka": "कालः सर्वभक्षयः।",
        "response": (
            "Bhishma lay on a bed of arrows, but his voice shaped the next era. "
            "Age doesn’t steal power—it distills it. Don’t count years—count truths. Each one adds weight to your sword."
        )
    },
    {
        "category": "Judging Yourself Too Harshly",
        "scenario": "You're your own worst critic.",
        "characters": ["Yudhishthira"],
        "lesson": "Self-compassion is the highest discipline.",
        "shloka": "न आत्मा हन्यते हन्यमाने शरीरे।",
        "response": (
            "Yudhishthira blamed himself for every loss. But Krishna reminded him—perfection isn’t the path, presence is. "
            "You’re allowed to be flawed and still be worthy. Forgive yourself. That’s when true growth begins."
        )
    },
    {
        "category": "Loss of Inspiration",
        "scenario": "Nothing excites or ignites you anymore.",
        "characters": ["Krishna", "Arjuna"],
        "lesson": "Inspiration is a choice, not a miracle.",
        "shloka": "योगः कर्मसु कौशलम्।",
        "response": (
            "Arjuna waited for a sign. Krishna gave him truth. Inspiration doesn’t fall from the sky—it rises when you start moving. "
            "Pick up your bow. Fire follows focus."
        )
    },
    {
        "category": "Trust Issues",
        "scenario": "You find it hard to trust anyone anymore.",
        "characters": ["Draupadi"],
        "lesson": "Trust is sacred. Don't offer it to the undeserving.",
        "shloka": "सत्यं वद धर्मं चर।",
        "response": (
            "Draupadi was betrayed by husbands, kings, kin. Yet she didn’t stop trusting—she just chose wiser. "
            "You don’t have to close your heart—just guard it with wisdom. Let experience be your sword."
        )
    },
    {
        "category": "Fear of Being Average",
        "scenario": "You want to stand out but feel ordinary.",
        "characters": ["Nakula"],
        "lesson": "Depth matters more than dazzle.",
        "shloka": "विद्यया अमृतमश्नुते।",
        "response": (
            "Nakula wasn’t loud—but he was radiant, kind, balanced. The world needs depth more than drama. "
            "Be steady in who you are. That’s how stars are born—silently, but forever."
        )
    },
    {
        "category": "Emotional Burnout",
        "scenario": "You're emotionally drained from everything.",
        "characters": ["Sahadeva"],
        "lesson": "Stillness is strength too.",
        "shloka": "योगस्थः कुरु कर्माणि।",
        "response": (
            "Sahadeva observed more than he spoke, and healed more than he fought. Rest is not retreat—it is repair. "
            "Sit. Breathe. Listen to your soul. Then rise like the quiet storm you are."
        )
    },
{
  "category": "Being Misunderstood",
  "scenario": "You feel like no one truly understands your intentions.",
  "characters": ["Vidura"],
  "lesson": "Truth doesn’t shout—it endures.",
  "shloka": "सत्यं ब्रूयात् प्रियं ब्रूयात् न ब्रूयात् सत्यमप्रियम्।",
  "response": "Vidura walked the halls of power, whispering dharma while others roared with ego. Though he was ignored, insulted, and sidelined, he never strayed from truth. He knew that understanding may not arrive today—but it always comes to those who wait with integrity. If you're not being seen right now, it doesn’t mean you're invisible. It means you're rare. Keep standing firm. One day, your silence will echo louder than their doubts."
},
{
  "category": "Fear of Starting Over",
  "scenario": "You’re afraid to begin again after a setback.",
  "characters": ["Pandavas"],
  "lesson": "New beginnings are born from ashes.",
  "shloka": "अनायासेन मरणं विना दैन्येन जीवनम्।",
  "response": "The Pandavas lost their palace to deceit, their kingdom to chance, and their pride to exile. But they didn't curl into defeat. In forests and caves, they learned, trained, healed. When they returned, they weren’t broken—they were reborn. Starting over isn’t failure. It’s your preparation for a stronger version of yourself. Don’t fear the empty slate; it is where your next victory will be written."
},
{
  "category": "Craving Approval",
  "scenario": "You depend too much on others' validation.",
  "characters": ["Karna"],
  "lesson": "Approval fades. Character remains.",
  "shloka": "स्वधर्मे निधनं श्रेयः परधर्मो भयावहः।",
  "response": "Karna lived under shadows—rejected by birth, mocked by class, and constantly seeking validation. He became great, not because others believed in him, but because he refused to betray his own values. Yet the hunger for approval cost him dearly. You don't need their applause to walk your path. Trust your heartbeat over their noise. Let your journey echo from self-worth, not borrowed praise. Become undeniable, not because they clap—but because you never stopped walking."
},
{
  "category": "Impatience",
  "scenario": "You want results faster than life allows.",
  "characters": ["Yudhishthira"],
  "lesson": "Time reveals all that is earned.",
  "shloka": "कालः पचति भूतानि कालः संहरते प्रजाः।",
  "response": "Yudhishthira waited years in exile—tolerating insult, watching injustice, and yet holding faith. He knew that dharma isn’t rushed—it’s revealed. If you’re growing restless, remember: the fruit doesn't ripen faster just because you're hungry. Some victories bloom only after the soil has fully tested your roots. Be patient—not because it’s easy, but because your destiny deserves the time to become unshakable."
},
{
  "category": "Feeling Powerless",
  "scenario": "You feel like nothing you do matters.",
  "characters": ["Draupadi"],
  "lesson": "Even one voice can awaken justice.",
  "shloka": "न्यायो हि बलवान् राजा।",
  "response": "Draupadi stood alone in a court of silence, her dignity under siege. No one came to her aid—not at first. But her voice cracked the pillars of that hall. Her pain forced the gods to listen. When you feel powerless, remember—you don’t need an army to be powerful. You need fire in your truth. One whisper of justice can ignite an empire of change. Your voice matters. Speak it—even when it trembles."
},{
  "category": "Loss of Identity",
  "scenario": "You don’t know who you are anymore.",
  "characters": ["Arjuna"],
  "lesson": "Identity isn’t found. It is remembered.",
  "shloka": "क्लैब्यं मा स्म गमः पार्थ नैतत्त्वय्युपपद्यते।",
  "response": "On the eve of battle, Arjuna looked at the faces of his kin and felt lost—no warrior, no hero, no clarity. His bow slipped. His purpose blurred. But Krishna reminded him: you were never just a name or a role. You are the fire born of dharma. You are the soul born to act. When you forget who you are, it’s not the end—it’s the pause before rediscovery. Sit still. Listen deep. Your strength has only stepped into the shadow. Call it back."
},
{
  "category": "Envy",
  "scenario": "You’re consumed by jealousy of others’ success.",
  "characters": ["Duryodhana"],
  "lesson": "Jealousy blinds you to your own abundance.",
  "shloka": "लोभः प्राणानपि त्यजेत्।",
  "response": "Duryodhana had wealth, power, and a kingdom—but his eyes only saw what others had. His envy turned blessings into chains. His hunger for more cost him everything. Envy is not just a poison—it’s theft of your own joy. Look again at your journey. What you’re building is yours. Let others inspire, not threaten. The only competition worth keeping is with your own past."
},
{
  "category": "Fear of Letting Go",
  "scenario": "You’re holding on to something you know is hurting you.",
  "characters": ["Bhishma"],
  "lesson": "Letting go is not weakness. It’s wisdom.",
  "shloka": "सर्वं आत्मवशं सुखं।",
  "response": "Bhishma held onto a vow for decades—even when it cost him peace, even when it chained him to silence. It was noble, but also tragic. Sometimes, loyalty to the past becomes betrayal of the self. If something no longer serves your dharma, release it. Letting go isn’t the end—it’s the space where new truths begin. What you release with grace, returns as freedom."
},
{
  "category": "Injustice",
  "scenario": "You’re tired of facing unfairness over and over.",
  "characters": ["Abhimanyu"],
  "lesson": "Even short lives can become eternal flames.",
  "shloka": "धर्म एव हतो हन्ति धर्मो रक्षति रक्षितः।",
  "response": "Abhimanyu was young, outnumbered, and betrayed by the rules of war. But he did not retreat. He broke through what others feared to face. Life isn’t always fair—but your courage doesn’t wait for fairness to show up. You are not defined by what was done to you—but by how you rise through it. Let your name be remembered not for what stopped you, but for what couldn’t."
},
{
  "category": "Overwhelm",
  "scenario": "You feel like everything is happening at once and you can’t handle it.",
  "characters": ["Krishna"],
  "lesson": "Stillness is the root of mastery.",
  "shloka": "योगस्थः कुरु कर्माणि संगं त्यक्त्वा धनञ्जय।",
  "response": "In the middle of war, chaos, and heartbreak—Krishna never raised a weapon. Yet he changed everything. Power doesn’t always roar. Sometimes, it whispers. You don’t have to do everything. You have to do what matters. Find stillness in the storm. Breathe like Krishna—steady, centered, present. One focused act with calm destroys a thousand confused reactions."
}



]


# Insert into MongoDB
collection.insert_many(wisdom_entries)

print("✅ Empowering Mahabharata wisdom has been successfully inserted!")

