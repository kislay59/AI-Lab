class VacuumCleanerAgent:
    def __init__(self, location, status_a, status_b):
        self.location = location.upper()
        self.environment = {
            'A': 'Dirty' if status_a == '1' else 'Clean',
            'B': 'Dirty' if status_b == '1' else 'Clean'
        }
        self.cost = 0

    def sense_and_act(self):
        print(f"\nCurrent Location: {self.location}")
        print(f"Environment Status: {self.environment}")

        if self.environment[self.location] == 'Dirty':
            self.environment[self.location] = 'Clean'
            print("Action: Suck (Cleaned dirt)")
            self.cost += 1
        elif self.location == 'A' and self.environment['B'] == 'Dirty':
            self.location = 'B'
            print("Action: Move Right")
            self.cost += 1
        elif self.location == 'B' and self.environment['A'] == 'Dirty':
            self.location = 'A'
            print("Action: Move Left")
            self.cost += 1
        else:
            print("Action: No-Op (Both rooms are clean)")
            return False
        return True

# --- Get User Input for Initial State ---
print("--- Vacuum Cleaner Setup ---")
start_loc = input("Enter starting location of Vacuum (A or B): ").strip().upper()
while start_loc not in ['A', 'B']:
    start_loc = input("Invalid room. Please enter A or B: ").strip().upper()

status_a = input("Is Room A Dirty or Clean? (Enter 1 for Dirty, 0 for Clean): ").strip()
status_b = input("Is Room B Dirty or Clean? (Enter 1 for Dirty, 0 for Clean): ").strip()

# Run Simulation
vacuum = VacuumCleanerAgent(location=start_loc, status_a=status_a, status_b=status_b)
running = True
while running:
    running = vacuum.sense_and_act()

print(f"\nGoal Achieved! Total cost/actions: {vacuum.cost}")
