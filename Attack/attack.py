import random

playerhp = 320
enemy_attacklow = 60
enemy_attackhigh = 80

while playerhp > 0:
    dmg = random.randrange(enemy_attacklow, enemy_attackhigh)
    playerhp = playerhp - dmg

    if playerhp <= 0:
        playerhp = 0

    print("Enemy strikes for", dmg, "points of damage.""current hp of the player =", playerhp)