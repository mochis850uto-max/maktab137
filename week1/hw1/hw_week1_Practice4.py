name: str = input("enter your name:")
score: str = input("enter your score:")
user_score: int = int(score)

if user_score > 90:
    print(f"user {name}: Great")

elif 70 <= user_score <= 90:
    print(f"user {name}: Good")

elif user_score < 70:
    print(f"user {name}: Need to improve")
