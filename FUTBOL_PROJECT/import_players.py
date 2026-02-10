import os
import django
import pandas as pd

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scout_project.settings')
django.setup()

from players.models import Player

def run_import():
    csv_file = 'filtered_players_data.csv' 
    
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found!")
        return

    try:
        # Loading the dataset
        df = pd.read_csv(csv_file)
        
        if df.empty:
            print("Error: The CSV file is empty!")
            return

        # Selecting top players
        top_players = df.head(20)

        for index, row in top_players.iterrows():
            # Check if player exists, otherwise create
            player, created = Player.objects.get_or_create(
                name=row['Player'],
                defaults={
                    'team': row['Squad'],
                    'position': row['Pos'],
                    'age': row['Age'],
                    'goals': row['Gls'],
                    'assists': row['Ast']
                }
            )
            if created:
                print(f"Successfully added: {row['Player']}")
            else:
                print(f"Already exists: {row['Player']}")
                
    except pd.errors.EmptyDataError:
        print("Error: Could not read CSV because it is empty!")

if __name__ == "__main__":
    run_import()