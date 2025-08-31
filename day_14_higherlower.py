import random

def higherlower():
    celebrity_followers = {# in millions
    "Cristiano Ronaldo": 663,
    "Lionel Messi": 506,
    "Selena Gomez": 417,
    "Kylie Jenner": 393,
    "Dwayne Johnson": 392,
    "Ariana Grande": 374,
    "Kim Kardashian": 355,
    "Beyoncé": 310,
    "Khloé Kardashian": 301,
    "Justin Bieber": 294,
    "Kendall Jenner": 286,
    "Taylor Swift": 280,
    "Virat Kohli": 273,
    "Jennifer Lopez": 248,
    "Neymar": 231,
    "Nicki Minaj": 224,
    "Kourtney Kardashian": 217,
    "Miley Cyrus": 212,
    "Katy Perry": 203,
    "Zendaya": 178,
    "Gal Gadot": 107,
    "Lisa (BLACKPINK)": 106,
    "Rosé (BLACKPINK)": 84,
    "Addison Rae": 88  
}
    score = 0
    Celeb_A, Celeb_B = random.sample(list(celebrity_followers.keys()), 2)
    while True:
        print(f"Type A to pick {Celeb_A}")
        print(f"Type B to pick {Celeb_B}")
        choose = input("Type your choice: ")
        
        if choose == 'A':
            winner = Celeb_A if celebrity_followers[Celeb_A] > celebrity_followers[Celeb_B] else Celeb_B
        elif choose == 'B':
            winner = Celeb_B if celebrity_followers[Celeb_B] > celebrity_followers[Celeb_A] else Celeb_A
        else:
            print("Invalid choice")
        
        if winner == Celeb_A and choose == 'A' or winner == Celeb_B and choose == 'B':
            print("Correct.")
            score += 1
            Celeb_A = Celeb_B
            Celeb_B = random.choice([c for c in celebrity_followers.keys() if c != Celeb_A])
        else:
            print(f"Wrong. Final score: {score}")
            break

higherlower()