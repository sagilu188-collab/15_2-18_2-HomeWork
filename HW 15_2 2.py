# קלוט מהמשתמש מספר ת.ז. של מצביע (נניח שמדובר במספרים בין 1 ל־100)
#
# כללים:
#
# כל מצביע שנקלט – הכנס לרשימה בשם votes
# קולטים רק את ת.ז. של המצביע, ולא את ההצבעה עצמה
# ייתכן שאותו מצביע ינסה להצביע יותר מפעם אחת
# הקלט מסתיים כאשר מתקבל הערך 999-
# לאחר סיום הקלט:
#
# צור set של מצביעים ייחודיים מתוך הרשימה
#
# צור set נוסף בשם invalid_voters
#
# עבור על כל המצביעים:
#
# כל מצביע שהופיע יותר מפעם אחת – הסר אותו מקבוצת המצביעים החוקיים
# הוסף אותו ל־invalid_voters
# לבסוף הדפס:
#
# את כל המצביעים החוקיים
# את כל המצביעים הפסולים
# כמה ניסיונות הצבעה היו היום (כלומר אורך הרשימה כולל כפילויות)


votes = []
codeInput = 0



print("Your voting code is the last 4 digits in your ID number")
print("Type -999 to stop voting")

while codeInput != -999:
    codeInput = int(input("Enter your voting code: "))
    if codeInput != -999:
        votes.append(codeInput)
        #print(votes)

vipVoters = set(votes)
invalidVoters = set()


for voter in votes:

    if votes.count(voter) > 1:
        invalidVoters.add(voter)

print("Valid Voters:" , list(vipVoters))
print("Invalid Voters:" , list(invalidVoters))
print("All Voters" , votes)
print("Total Votes Today:", len(votes))

