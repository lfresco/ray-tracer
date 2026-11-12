from tuples import Vector, Point

class Environment:
    
    def __init__(self, gravity: Vector, wind: Vector):
        self.gravity = gravity
        self.wind = wind

class Projectile:
    
    def __init__(self, position: Point, velocity: Vector):
        self.position = position
        self.velocity = velocity

def tick(env: Environment, proj: Projectile):
    new_position = proj.position + proj.velocity
    new_velocity = proj.velocity + env.gravity + env.wind
    return Projectile(new_position, new_velocity)
        
if __name__ == "__main__":
    p = Projectile(Point(0, 1, 0), Vector(1, 1, 0).normalize())
    e = Environment(Vector(0, -0.1, 0), Vector(-0.01, 0, 0))
    
    ticks = 0
    ys = [p.position.y]
    
    while p.position.y >= 0:
        p = tick(e, p)
        ys.append(p.position.y)
        ticks +=1   

    print(f"Number of ticks required: {ticks}")
    print(ys)     