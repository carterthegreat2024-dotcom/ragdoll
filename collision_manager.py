class CollisionManager:
    def __init__(self):
        self.collision_groups = {}
        self.collision_filters = {}

    def add_collision_group(self, group_name):
        if group_name not in self.collision_groups:
            self.collision_groups[group_name] = []

    def add_to_group(self, group_name, object):
        if group_name in self.collision_groups:
            self.collision_groups[group_name].append(object)

    def set_collision_filter(self, group_a, group_b, is_collidable):
        self.collision_filters[(group_a, group_b)] = is_collidable

    def check_collision(self, obj_a, obj_b):
        group_a = obj_a.get_collision_group()
        group_b = obj_b.get_collision_group()
        collidable = self.collision_filters.get((group_a, group_b), True)

        if collidable:
            self.handle_collision(obj_a, obj_b)

    def handle_collision(self, obj_a, obj_b):
        # Implement collision handling logic
        print(f'Collision detected between {obj_a} and {obj_b}')
        self.trigger_on_hit_event(obj_a, obj_b)

    def trigger_on_hit_event(self, obj_a, obj_b):
        # Handle OnHit event logic
        print(f'OnHit triggered for {obj_a} and {obj_b}')

    def detect_impact_velocity(self, obj_a, obj_b, delta_time):
        # Calculate impact velocity based on position change over time
        velocity = (obj_b.position - obj_a.position) / delta_time
        return velocity

# Example usage:
# collision_manager = CollisionManager()
# collision_manager.add_collision_group('ragdoll_parts')
# collision_manager.add_collision_group('environment')
# collision_manager.set_collision_filter('ragdoll_parts', 'environment', False)