import os
import random
from datetime import datetime

# Calculate the number of commits (5% chance of 10-15, 95% chance of 5-10)
chance = random.random()

if chance < 0.05:
    num_commits = random.randint(10, 15)
else:
    num_commits = random.randint(5, 10)

# Generate the commits
for i in range(num_commits):
    # Modify a dummy file
    with open("activity.log", "a") as file:
        file.write(f"System check logged at {datetime.now()} - Cycle {i}\n")
    
    # Add and commit
    os.system("git add activity.log")
    os.system(f'git commit -m "Update system metrics {datetime.now().strftime("%Y%m%d%H%M%S")}-{i}"')

print(f"Successfully created {num_commits} commits.")