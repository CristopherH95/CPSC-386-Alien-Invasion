import pickle


class GameStats:
    """Track statistics for Alien Invasion"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.ships_left = 0
        self.high_score = None
        self.score = None
        self.level = None
        self.reset_stats()
        self.initialize_high_score()
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that change during game play"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def initialize_high_score(self):
        """Read the saved high score from the pickle file on disk (if it exists)"""
        try:
            with open('score_data.pkl', 'rb') as file:
                self.high_score = int(pickle.load(file))    # Cast to int to verify type
        except FileNotFoundError:
            self.high_score = 0     # No high score yet, probably first time running
        except ValueError:
            print('Invalid score data found in pickle file')
            print('Setting high score to default value')
            self.high_score = 0     # File may have been corrupted or tampered with
        except EOFError:
            print('Empty score data file')
            print('Setting high score to default value')
            self.high_score = 0     # File contents were deleted somehow

    def save_high_score(self):
        """Save the high score to a pickle file on disk"""
        with open('score_data.pkl', 'wb') as file:
            pickle.dump(self.high_score, file)
