import random
from tkinter import *
from tkinter import messagebox

REACH_SUMS = {
    2: 17, 3: 18, 4: 21, 5: 25, 6: 28,
}

BASE_REACH = {
    "Marquise de Cat": 10,
    "Eyrie Dynasties": 7,
    "Vagabond": 5,
    "Woodland Alliance": 3,
}

RIVERFOLK_REACH = {
    "Riverfolk Company": 5,
    "Lizard Cult": 2,
    "2nd Vagabond": 2,
}

UNDERWORLD_REACH = {
    "Underground Duchy": 8,
    "Corvid Conspiracy": 3,
}

MARAUDER_REACH = {
    "Lord of the Hundreds": 9,
    "Keepers in Iron": 8,
}

player_entries = []


def input_player_names(value):
    for num in range(value):
        label = Label(text=f"Player {num + 1}: ")
        label.grid(column=6, row=num + 1)
        player_entry = Entry(width=15)
        player_entry.grid(column=7, row=num + 1)
        player_entries.append(player_entry)
    assign_faction_button = Button(text='Assign Factions',
                                   command=lambda: add_expansions_to_dict(riverfolk=riverfolk.get(),
                                                                          underworld=underworld.get(),
                                                                          marauder=marauder.get()))
    assign_faction_button.grid(column=7, row=value + 1)


def add_expansions_to_dict(riverfolk, underworld, marauder):
    if num_of_players.get() > 4 and not riverfolk and not underworld and not marauder:
        messagebox.showerror(title="Error", message="Not enough factions for all players.")
    else:
        req_reach = REACH_SUMS[num_of_players.get()]
        print(req_reach)
        reach = BASE_REACH.copy()
        if riverfolk:
            reach.update(RIVERFOLK_REACH)
        if underworld:
            reach.update(UNDERWORLD_REACH)
        if marauder:
            reach.update(MARAUDER_REACH)

        assign_faction(req_reach=req_reach, reach=reach)


def assign_faction(req_reach, reach):
    reach_left = req_reach
    available_factions = reach.copy()
    assigned_factions = {}
    for entry in player_entries:
        faction = random.choice(list(available_factions.keys()))
        if faction == "2nd Vagabond" and "Vagabond" in available_factions.keys():
            faction = 'Vagabond'
        reach_left -= available_factions[faction]
        del available_factions[faction]
        player = entry.get()
        assigned_factions[player] = faction
    if reach_left > 0:
        assign_faction(req_reach, reach)
    else:
        for key in assigned_factions:
            Label(text=f"{key}: {assigned_factions[key]}").grid(columnspan=7)



window = Tk()
window.title('Faction Assigning Assistance')

players_label = Label(text="Number of players: ")
players_label.grid(row=0, column=0, columnspan=5)

num_of_players = IntVar(value=0)

two_players = Radiobutton(window, text='2', variable=num_of_players, value=2)
two_players.grid(column=0, row=1)

three_players = Radiobutton(window, text='3', variable=num_of_players, value=3)
three_players.grid(column=1, row=1)

four_players = Radiobutton(window, text='4', variable=num_of_players, value=4)

four_players.grid(column=2, row=1)

five_players = Radiobutton(window, text='5', variable=num_of_players, value=5)
five_players.grid(column=3, row=1)

six_players = Radiobutton(window, text='6', variable=num_of_players, value=6)
six_players.grid(column=4, row=1)

expansions_label = Label(text="Expansions in play: ")
expansions_label.grid(column=0, row=2, columnspan=5)

riverfolk = BooleanVar()
riverfolk_check = Checkbutton(text="The Riverfolk", variable=riverfolk, onvalue=True, offvalue=False)
riverfolk_check.grid(columnspan=5, row=3)

underworld = BooleanVar()
underworld_check = Checkbutton(text="The Underworld", variable=underworld, onvalue=True, offvalue=False)
underworld_check.grid(columnspan=5, row=4)

marauder = BooleanVar()
marauder_check = Checkbutton(text="The Marauder", variable=marauder, onvalue=True, offvalue=False)
marauder_check.grid(columnspan=5, row=5)

assign_button = Button(text="Input player names", command=lambda: input_player_names(num_of_players.get()))
assign_button.grid(columnspan=5)

window.mainloop()
