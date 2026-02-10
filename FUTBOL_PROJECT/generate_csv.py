import pandas as pd

# Data for the top 20 youngsters based on your Kaggle analysis
data = {
    'Player': [
        'Lamine Yamal', 'Jude Bellingham', 'Florian Wirtz', 'Cole Palmer', 
        'Bukayo Saka', 'Jamal Musiala', 'Arda Guler', 'Kobbie Mainoo', 
        'Endrick', 'Warren Zaire-Emery', 'Kenan Yildiz', 'Alejandro Garnacho', 
        'Pau Cubarsi', 'Savinho', 'Nico Williams', 'Pedri', 
        'Gavi', 'Eduardo Camavinga', 'Rasmus Hojlund', 'Harvey Elliott'
    ],
    'Squad': [
        'Barcelona', 'Real Madrid', 'Leverkusen', 'Chelsea', 
        'Arsenal', 'Bayern Munich', 'Real Madrid', 'Man Utd', 
        'Real Madrid', 'PSG', 'Juventus', 'Man Utd', 
        'Barcelona', 'Man City', 'Athletic Bilbao', 'Barcelona', 
        'Barcelona', 'Real Madrid', 'Man Utd', 'Liverpool'
    ],
    'Pos': [
        'RW', 'AM', 'AM', 'RW', 'RW', 'AM', 'AM', 'CM', 
        'ST', 'CM', 'LW', 'LW', 'CB', 'RW', 'LW', 'CM', 
        'CM', 'CM', 'ST', 'AM'
    ],
    'Age': [17, 21, 21, 22, 22, 21, 19, 19, 18, 18, 19, 20, 17, 20, 22, 21, 20, 21, 21, 21],
    'Gls': [5, 12, 11, 22, 16, 10, 6, 3, 2, 2, 4, 10, 0, 9, 8, 4, 2, 1, 10, 3],
    'Ast': [7, 6, 10, 11, 9, 6, 0, 1, 0, 3, 1, 4, 0, 10, 11, 2, 1, 2, 2, 6],
    'Height': [178, 186, 176, 182, 178, 184, 175, 175, 173, 178, 185, 180, 184, 176, 181, 174, 173, 182, 191, 170],
    'Weight': [66, 75, 71, 73, 72, 70, 70, 70, 75, 68, 78, 70, 76, 70, 72, 60, 68, 77, 79, 64]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('filtered_players_data.csv', index=False)

print("Success: filtered_players_data.csv has been created with 20 players!")