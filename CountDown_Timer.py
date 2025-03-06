import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# Example usage
countdown_timer(10))  # Countdown from 10 seconds