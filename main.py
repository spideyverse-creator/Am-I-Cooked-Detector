import random

print("=" * 55)
print("              💀 AM I COOKED? DETECTOR 💀")
print("=" * 55)

situation = input("\n😬 What's your situation? → ").lower()

# Keywords used to detect the situation
categories = {

    "exam": [
        "exam", "test", "paper", "study", "studying",
        "syllabus", "marks", "result", "homework"
    ],

    "coding": [
        "code", "coding", "python", "program", "bug",
        "error", "debug", "programming", "github"
    ],

    "money": [
        "money", "broke", "salary", "paisa", "cash",
        "wallet", "bank", "poor"
    ],

    "sleep": [
        "sleep", "slept", "tired", "night",
        "awake", "sleeping", "insomnia"
    ],

    "relationship": [
        "crush", "girlfriend", "boyfriend", "reply",
        "seen", "love", "relationship", "message"
    ],

    "gaming": [
        "game", "gaming", "minecraft", "rank",
        "noob", "lost", "match", "enemy"
    ],

    "school": [
        "school", "teacher", "principal", "class",
        "attendance", "teacher", "lecture"
    ],

    "parents": [
        "mom", "mummy", "mother", "dad", "father",
        "parents", "ghar", "permission"
    ],

    "phone": [
        "phone", "mobile", "battery", "charger",
        "screen", "iphone", "android"
    ],

    "food": [
        "food", "hungry", "pizza", "burger",
        "khana", "eat", "eating", "restaurant"
    ],

    "late": [
        "late", "traffic", "bus", "train",
        "rickshaw", "alarm", "missed"
    ],

    "friend": [
        "friend", "bro", "bestie", "group",
        "friendship", "party"
    ]
}


# Funny statements for every category
roasts = {

    "exam": [
        "Bro opened the book only to check the page number 💀",
        "Your preparation has officially left the chat 📚💀",
        "Exam is tomorrow and your brain is still on vacation 🗿",
        "You studied everything except the actual syllabus 😭",
        "At this point, guessing answers is your study strategy."
    ],

    "coding": [
        "The bug is not in the code. It's in the developer 💀",
        "Bro is fighting the compiler instead of fixing the code 😭",
        "Stack Overflow is about to become your best friend.",
        "Your code has more errors than your confidence 💀",
        "Python didn't fail you. You failed Python 🐍💀"
    ],

    "money": [
        "Bro's wallet is running on air 💀",
        "Your bank account needs emotional support 😭",
        "Financially cooked. Absolutely toasted. 🔥",
        "Your balance is basically a motivational quote.",
        "Bro checked his bank account and saw a horror movie 💀"
    ],

    "sleep": [
        "Bro has forgotten what sunlight looks like ☀️💀",
        "Your sleep schedule needs a software update.",
        "At this point you're not sleeping, you're buffering 😭",
        "Your bed knows you better than your family.",
        "Bro sleeps at 4 AM and wakes up at 'whenever'. 🗿"
    ],

    "relationship": [
        "Bro got emotionally damage.exe 💀",
        "That 'seen' button hit harder than expected 😭",
        "Bro is refreshing the chat like it's a stock market.",
        "The reply is taking longer than a Windows update 💀",
        "Bro is writing a paragraph and deleting it 17 times."
    ],

    "gaming": [
        "Bro got skill-issued 💀",
        "The enemy didn't win. You just donated the victory 😭",
        "Minecraft said: not today bro.",
        "Your gaming career needs a restart.",
        "Bro blamed lag. The Wi-Fi was innocent 💀"
    ],

    "school": [
        "Teacher said 'take out your homework' and bro entered survival mode 💀",
        "Attendance is doing more damage than the final boss.",
        "Bro is physically present but mentally AFK.",
        "The teacher knows your name for all the wrong reasons 😭",
        "School isn't ready for your next excuse."
    ],

    "parents": [
        "Bro heard 'we need to talk' and instantly started sweating 💀",
        "Your parents have activated final boss mode.",
        "Bro is calculating every possible escape route 😭",
        "One question from Mom and the whole story collapses.",
        "Bro suddenly remembers every good thing he has ever done."
    ],

    "phone": [
        "Battery at 2% and bro still watching YouTube 💀",
        "Your charger is doing more work than you.",
        "Phone storage: 99% full. Brain storage: unknown.",
        "Bro has 47 notifications and chooses to ignore all of them.",
        "Your phone is fighting for its life 😭"
    ],

    "food": [
        "Bro is hungry enough to eat the menu itself 💀",
        "Your stomach has started sending warning notifications.",
        "Food is currently your only personality trait.",
        "Bro opened the fridge for the 12th time hoping something new spawned.",
        "The fridge said: 'Bro, I already told you. There's nothing here.' 💀"
    ],

    "late": [
        "Bro's definition of '5 minutes' is scientifically questionable 💀",
        "The alarm rang. Bro negotiated with it and lost.",
        "Traffic is innocent this time. You're just late 😭",
        "Bro arrived after the important part ended.",
        "Time management has officially blocked you."
    ],

    "friend": [
        "Bro's friendship group is 90% roasting and 10% survival 💀",
        "Your friends know too much. You're in danger.",
        "Bro trusted the group chat. Rookie mistake 😭",
        "Friendship level: chaotic.",
        "Your friends would sell you for one samosa 💀"
    ]
}


# Detect category
found_category = None

for category, keywords in categories.items():

    for keyword in keywords:

        if keyword in situation:
            found_category = category
            break

    if found_category:
        break


print("\n🔍 ANALYZING YOUR SITUATION...")
print("⏳ Please wait...")

# Detect known situation
if found_category:

    roast = random.choice(roasts[found_category])

    cooked_level = random.randint(60, 100)

    print("\n" + "-" * 55)

    print("📂 Category:", found_category.upper())
    print("🔥 Cooked Level:", cooked_level, "%")

    if cooked_level <= 70:

        print("🟡 Status: SLIGHTLY COOKED")

    elif cooked_level <= 85:

        print("🟠 Status: GETTING COOKED")

    elif cooked_level <= 95:

        print("🔴 Status: YOU ARE COOKED 💀")

    else:

        print("☠️ Status: BRO IS ABSOLUTELY CHARCOAL")

    print("\n🤖 AI Verdict:")
    print(roast)

    print("-" * 55)


# Unknown situation
else:

    cooked_level = random.randint(40, 100)

    unknown_roasts = [

        "I don't understand what happened... BUT YOU ARE STILL COOKED 💀",

        "Situation unclear. Your future is also unclear. 🗿",

        "Bro entered a situation even Python can't understand 😭",

        "No category found. Maximum confusion detected.",

        "Whatever happened... it probably wasn't a good idea 💀",

        "Python has no idea what you're talking about. Neither do we.",

        "This situation is beyond scientific explanation 😭"

    ]

    print("\n" + "-" * 55)

    print("🤔 Category: UNKNOWN")
    print("🔥 Cooked Level:", cooked_level, "%")

    if cooked_level <= 70:

        print("🟡 Status: MAYBE SAFE")

    elif cooked_level <= 85:

        print("🟠 Status: PROBABLY COOKED")

    elif cooked_level <= 95:

        print("🔴 Status: DEFINITELY COOKED 💀")

    else:

        print("☠️ Status: CHARCOAL DETECTED")

    print("\n🤖 AI Verdict:")
    print(random.choice(unknown_roasts))

    print("-" * 55)


print("\n💀 Thank you for using AM I COOKED?")
print("Remember: If you're asking this question...")
print("...you're probably already cooked. 🗿")

print("=" * 55)