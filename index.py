import random

items = ["Rare", "Super rare", "Epic", "Mythic", "Legendary"]
weights = [55, 20, 13, 7, 5]

drop = random.choices(items, weights=weights, k=1)[0]

rare_rewards = ['25 power points', '50 coins', '10 credits']
rare_weights = [45, 45, 10]
rare_drop = random.choices(rare_rewards, weights=rare_weights, k=1)[0]

super_rewards = ['100 coins', '125 power points', '20 credits', 'common pin']
super_weights = [40, 40, 15, 5]
super_drop = random.choices(super_rewards, weights=super_weights, k=1)[0]

epic_rewards = ['200 coins', '200 power points', '100 credits', 'rare pin', 'rare brawler', 'rare skin']
epic_weights = [35, 35, 10, 2, 8, 10]
epic_drop = random.choices(epic_rewards, weights=epic_weights, k=1)[0]

mythic_rewards = ['500 coins', '500 power points', 'super rare brawler', 'epic brawler', 'mythic brawler', 'gadget', 'epic skin']
mythic_weights = [30, 30, 5, 9, 11, 10, 5]
mythic_drop = random.choices(mythic_rewards, weights=mythic_weights, k=1)[0]

legendary_rewards = ['hypercharge', 'mythic brawler', 'legendary brawler', '1000 credits']
legendary_weights = [8, 12, 10, 70]
legendary_drop = random.choices(legendary_rewards, weights=legendary_weights, k=1)[0]


def rare():
    return rare_drop


def super():
    return super_drop


def epic():
    return epic_drop


def mythic():
    return mythic_drop


def legendary():
    return legendary_drop


res_rare = rare()
res_super = super()
res_epic = epic()
res_mythic = mythic()
res_legendary = legendary()


if drop == "Rare":
    print(f"You got {drop} ,your reward is: {res_rare}")
elif drop == "Super rare":
    print(f"You got {drop} ,your reward is: {res_super}")
elif drop == "Epic":
    print(f"You got {drop} ,your reward is: {res_epic}")
elif drop == "Mythic":
    print(f"You got {drop} ,your reward is: {res_mythic}")
else:
    print(f"You got {drop} ,your reward is: {res_legendary}")
