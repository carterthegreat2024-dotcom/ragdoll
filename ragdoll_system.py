class Ragdoll:
    def __init__(self):
        self.bones = []  # List to hold bone objects
        self.is_physics_mode = False  # State of the Ragdoll

    def create_bone(self, name, length, position):
        # Create a new bone and add to bones list
        bone = {'name': name, 'length': length, 'position': position}
        self.bones.append(bone)
        return bone

    def manage_bone(self, name, new_position):
        # Update position of an existing bone
        for bone in self.bones:
            if bone['name'] == name:
                bone['position'] = new_position
                return bone
        return None

    def switch_mode(self):
        # Switch between animation and physics modes
        self.is_physics_mode = not self.is_physics_mode

    def apply_ball_socket_constraint(self, bone_a, bone_b):
        # Implementation for BallSocketConstraint between two bones
        # Placeholder for constraint logic
        return f'BallSocketConstraint applied between {bone_a} and {bone_b}'

# Example Usage
if __name__ == '__main__':
    ragdoll = Ragdoll()
    ragdoll.create_bone('upper_arm', 10, (0, 0, 0))
    ragdoll.manage_bone('upper_arm', (1, 1, 1))
    print(ragdoll.apply_ball_socket_constraint('upper_arm', 'lower_arm'))
    ragdoll.switch_mode()