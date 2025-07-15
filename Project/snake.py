#!/usr/bin/env python3
"""
Snake Game for Terminal
----------------------
A classic snake game implementation using Python's curses library
for terminal-based gameplay.

Controls:
- Arrow keys: Move the snake
- Q: Quit the game

Compatible with macOS and other Unix-based systems.
"""

import curses
import random
import time

def main(stdscr):
    """
    Main game function that initializes and runs the snake game
    
    Args:
        stdscr: The curses standard screen object
    """
    # Setup initial game state
    curses.curs_set(0)  # Hide the cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Snake color
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Food color
    
    # Get screen dimensions
    height, width = stdscr.getmaxyx()
    
    # Game boundaries (leave 1 cell border)
    game_area = {
        'top': 1,
        'bottom': height - 2,
        'left': 1,
        'right': width - 2
    }
    
    # Initialize game parameters
    snake = [{'y': height // 2, 'x': width // 4}]  # Start snake in the middle-left
    food = None
    direction = {'y': 0, 'x': 1}  # Start moving right
    score = 0
    game_speed = 0.1  # Seconds between movements
    
    # Generate initial food
    generate_food(stdscr, snake, game_area, food)
    
    # Main game loop
    game_over = False
    while not game_over:
        # Setup screen with borders and info
        stdscr.clear()
        draw_borders(stdscr, game_area)
        display_score(stdscr, score)
        
        # Draw snake
        for segment in snake:
            stdscr.addch(segment['y'], segment['x'], '#', curses.color_pair(1))
        
        # Draw food if it exists
        if food:
            stdscr.addch(food['y'], food['x'], '*', curses.color_pair(2))
        
        stdscr.refresh()
        
        # Get user input (non-blocking)
        stdscr.timeout(100)  # Wait 100ms for input
        key = stdscr.getch()
        
        # Process input for direction changes or quit
        if key == ord('q') or key == ord('Q'):
            return  # Exit the game
        elif key == curses.KEY_UP and direction['y'] != 1:
            direction = {'y': -1, 'x': 0}
        elif key == curses.KEY_DOWN and direction['y'] != -1:
            direction = {'y': 1, 'x': 0}
        elif key == curses.KEY_LEFT and direction['x'] != 1:
            direction = {'y': 0, 'x': -1}
        elif key == curses.KEY_RIGHT and direction['x'] != -1:
            direction = {'y': 0, 'x': 1}
        
        # Wait for game speed delay
        time.sleep(game_speed)
        
        # Calculate new head position
        new_head = {
            'y': snake[0]['y'] + direction['y'],
            'x': snake[0]['x'] + direction['x']
        }
        
        # Check for collisions with walls
        if (new_head['y'] <= game_area['top'] or 
            new_head['y'] >= game_area['bottom'] or
            new_head['x'] <= game_area['left'] or
            new_head['x'] >= game_area['right']):
            game_over = True
            break
        
        # Check for collisions with self
        if new_head in snake:
            game_over = True
            break
        
        # Add new head to snake
        snake.insert(0, new_head)
        
        # Check if snake ate the food
        if food and new_head['y'] == food['y'] and new_head['x'] == food['x']:
            food = None  # Remove the eaten food
            score += 10  # Increase score
            # Speed up slightly as score increases (max speed = 0.05s)
            game_speed = max(0.05, 0.1 - (score // 100) * 0.01)
            generate_food(stdscr, snake, game_area, food)
        else:
            # If no food was eaten, remove the tail to maintain length
            snake.pop()
    
    # Game over screen
    stdscr.clear()
    game_over_message = "GAME OVER! Your score: {}".format(score)
    exit_message = "Press any key to exit..."
    
    stdscr.addstr(height // 2 - 1, (width - len(game_over_message)) // 2, game_over_message)
    stdscr.addstr(height // 2 + 1, (width - len(exit_message)) // 2, exit_message)
    stdscr.refresh()
    stdscr.timeout(-1)  # Wait indefinitely for key press
    stdscr.getch()  # Wait for key press to exit

def generate_food(stdscr, snake, game_area, food):
    """
    Generate new food at a random position that's not on the snake
    
    Args:
        stdscr: The curses screen object
        snake: List of dictionaries representing snake segments
        game_area: Dictionary with game boundaries
        food: Current food position (or None)
    
    Returns:
        Dictionary with y, x coordinates of the new food
    """
    height, width = stdscr.getmaxyx()
    
    while True:
        # Generate random coordinates within game area
        new_food = {
            'y': random.randint(game_area['top'] + 1, game_area['bottom'] - 1),
            'x': random.randint(game_area['left'] + 1, game_area['right'] - 1)
        }
        
        # Make sure food is not on the snake
        if new_food not in snake:
            return new_food

def draw_borders(stdscr, game_area):
    """
    Draw the game borders on the screen
    
    Args:
        stdscr: The curses screen object
        game_area: Dictionary with game boundaries
    """
    height, width = stdscr.getmaxyx()
    
    # Draw top and bottom borders
    for x in range(game_area['left'], game_area['right'] + 1):
        stdscr.addch(game_area['top'], x, '=')
        stdscr.addch(game_area['bottom'], x, '=')
    
    # Draw left and right borders
    for y in range(game_area['top'], game_area['bottom'] + 1):
        stdscr.addch(y, game_area['left'], '|')
        stdscr.addch(y, game_area['right'], '|')
    
    # Draw corners
    stdscr.addch(game_area['top'], game_area['left'], '+')
    stdscr.addch(game_area['top'], game_area['right'], '+')
    stdscr.addch(game_area['bottom'], game_area['left'], '+')
    stdscr.addch(game_area['bottom'], game_area['right'], '+')

def display_score(stdscr, score):
    """
    Display the current score on the screen
    
    Args:
        stdscr: The curses screen object
        score: Current game score
    """
    height, width = stdscr.getmaxyx()
    score_text = "Score: {}".format(score)
    stdscr.addstr(0, (width - len(score_text)) // 2, score_text)

if __name__ == "__main__":
    try:
        # Initialize and run the game using the curses wrapper
        # (this handles terminal setup/reset automatically)
        curses.wrapper(main)
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        pass
    finally:
        print("Thanks for playing Snake!")