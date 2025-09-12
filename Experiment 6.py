import random

def vacuum_cleaner(env, start_pos=0):
    position = start_pos
    steps = 0
    
    print("Initial Environment:", env)
    
    while 1 in env:  
        if env[position] == 1:
            print(f"Step {steps+1}: Dirt found at {position}, cleaning...")
            env[position] = 0
        else:
            print(f"Step {steps+1}: Position {position} is clean.")
        
        if 1 in env:
            if position == 0:
                position = 1
                print(f"Step {steps+1}: Moving Right → {position}")
            else:
                position = 0
                print(f"Step {steps+1}: Moving Left → {position}")
        steps += 1
    
    print("\nFinal Environment:", env)
    print("All squares are clean!")

if __name__ == "__main__":
   
    environment = [random.choice([0, 1]) for _ in range(2)]  
    vacuum_cleaner(environment, start_pos=0)
