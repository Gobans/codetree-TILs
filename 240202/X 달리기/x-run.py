X = int(input())
def find_shortest_time(X):
    # Time, speed, and distance initialized
    time = 0
    speed = 1
    distance = 0
    
    # Loop until the distance is less than the target distance X
    while distance < X:
        time += 1  # Increment time
        distance += speed  # Update distance
        
        # Decide whether to increase, decrease, or maintain speed
        # If distance + speed + 1 is less than or equal to X, we can consider increasing speed
        # But we need to make sure we can decrease back to 1 m/s for the final moment
        # Calculate remaining distance after current step
        remaining_distance = X - distance
        
        # If the next step overshoots, maintain or decrease speed
        if speed > 1 and (remaining_distance <= speed or remaining_distance > ((speed * (speed + 1)) / 2)):
            speed -= 1  # Decelerate if speed is greater than 1 and conditions met
        elif remaining_distance > ((speed * (speed + 1)) / 2):
            speed += 1  # Accelerate if we won't overshoot in the next steps
    
    return time

print(find_shortest_time(X) - 1)