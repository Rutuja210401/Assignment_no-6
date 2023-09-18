import json

state_capitals = {}

for i in range(7):
    state = input(f"Enter the name of Indian State {i + 1}: ")
    capital = input(f"Enter the capital of {state}: ")
    state_capitals[state] = capital

with open("indian_states.json", "w") as file:
    json.dump(state_capitals, file, indent=4)

print("State-capital information saved to 'indian_states.json'")