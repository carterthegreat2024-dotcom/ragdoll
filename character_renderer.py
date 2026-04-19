class CharacterRenderer:
    def __init__(self):
        self.characters = []

    def add_character(self, character):
        self.characters.append(character)

    def draw(self):
        for character in self.characters:
            # Code to visualize the character with bones, joints, etc.
            self.visualize_character(character)

    def visualize_character(self, character):
        # Placeholder for visualization code
        print(f"Drawing character with state: {character.state}")

    def demo(self):
        # Create two characters with dummy states
        character1 = {'state': 'standing'}
        character2 = {'state': 'falling'}

        self.add_character(character1)
        self.add_character(character2)

        # Draw both characters side by side
        print("Character 1:")
        self.visualize_character(character1)
        print("Character 2:")
        self.visualize_character(character2)

# Example usage:
if __name__ == '__main__':
    renderer = CharacterRenderer()
    renderer.demo()