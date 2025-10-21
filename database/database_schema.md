# Database Schema Design

## Entities and Relationships

### Teams
- id (unique identifier)
- name (display name)
- code (abbreviation like "T1", "GEN")
- region (LCK, LPL, etc.)
- current_elo (your ranking score)
- peak_elo (highest rating ever)
- global_rank (1, 2, 3...)
- regional_rank (1, 2, 3... within their region)
- created_at (when added to database)
- updated_at (when last modified)

Relationships:
- Has many Players
- Plays in many Matches
- Participates in many Tournaments

### Players
- id (unique identifier)
- summoner_name (in-game name)
- real_name (actual name if known)
- team_id (which team they belong to)
- role (TOP, JGL, MID, ADC, SUP)
- current_rating (performance score)
- peak_rating (best performance)
- debut_date (when they went pro)
- country (nationality)
- created_at
- updated_at

Relationships:
- Belongs to one Team
- Has many Performance records

### Matches
- id (unique identifier)
- tournament_id (which tournament)
- team1_id (first team)
- team2_id (second team)
- winner_id (which team won)
- scheduled_time (when match was supposed to start)
- start_time (actual start)
- end_time (when it finished)
- best_of (1, 3, or 5)
- status (scheduled, live, completed)
- patch_version (game version like "14.1")
- created_at
- updated_at

Relationships:
- Belongs to one Tournament
- Involves two Teams
- Contains multiple Games

### Tournaments
- id (unique identifier)
- name (LCK Spring 2024)
- slug (URL-friendly name)
- region (LCK, International, etc.)
- tier (regional, international)
- start_date
- end_date
- prize_pool
- status (scheduled, ongoing, completed)
- created_at
- updated_at

Relationships:
- Contains many Matches
- Has many Teams participating

### Games
- id (unique identifier)
- match_id (which match this game belongs to)
- game_number (1, 2, 3, etc.)
- winner_side (blue or red)
- duration_minutes (how long the game lasted)
- start_time
- end_time
- created_at

Relationships:
- Belongs to one Match
- Has multiple Player Performances

### Player Performance
- id (unique identifier)
- player_id (which player)
- game_id (which game)
- champion (which champion they played)
- side (blue or red)
- kills
- deaths
- assists
- damage_to_champions
- damage_per_minute
- gold_earned
- gold_per_minute
- cs_total (creep score)
- cs_per_minute
- vision_score
- performance_rating (calculated score)
- created_at

Relationships:
- Belongs to one Player
- Belongs to one Game

## Key Design Decisions

1. **Separate Matches and Games**: Matches can be Bo3 or Bo5, so we track individual games
2. **ELO stored with Teams**: Your ranking algorithm updates team ELO after matches
3. **Historical tracking**: created_at and updated_at let us see changes over time
4. **Regional context**: Store region info to support your regional strength algorithm
5. **Performance metrics**: Detailed stats for player analytics feature