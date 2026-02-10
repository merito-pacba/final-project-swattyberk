import os
import django
import pandas as pd

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scout_project.settings')
django.setup()

from players.models import Player

def run_import():
    # Path to your Kaggle CSV file
    csv_file = 'filtered_players_data.csv' 
    
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found!")
        return

    # Loading the dataset
    df = pd.read_csv(csv_file)
    
    # Selecting the top 20 players for the initial setup
    top_players = df.head(20)

    for index, row in top_players.iterrows():
        # Check if player exists, otherwise create a new record
        player, created = Player.objects.get_or_create(
            name=row['Player'],
            defaults={
                'team': row['Squad'],
                'position': row['Pos'],
                'age': row['Age'],
                'goals': row['Gls'],
                'assists': row['Ast'],
                'height': row.get('Height', 180), # Default 180cm if missing
                'weight': row.get('Weight', 75),  # Default 75kg if missing
                'preferred_foot': 'Right'         # Default to Right foot
            }
        )
        if created:
            print(f"Successfully added: {row['Player']}")
        else:
            print(f"Already exists: {row['Player']}")

if __name__ == "__main__":
    run_import()