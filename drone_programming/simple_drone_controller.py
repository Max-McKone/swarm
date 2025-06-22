#!/usr/bin/env python3
"""
Simple Drone Controller for Gazebo Simulation
This is a basic controller that you can extend with Gazebo integration
"""

import time
import math
import json
import os

class SimpleDroneController:
    def __init__(self):
        """Initialize the drone controller"""
        self.position = {'x': 0.0, 'y': 0.0, 'z': 2.0}
        self.orientation = {'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0}
        self.is_flying = False
        
        print("Simple Drone Controller initialized!")
        print("Commands:")
        print("  'takeoff' - Start flying")
        print("  'land' - Land the drone")
        print("  'forward' - Move forward")
        print("  'backward' - Move backward")
        print("  'left' - Move left")
        print("  'right' - Move right")
        print("  'up' - Move up")
        print("  'down' - Move down")
        print("  'status' - Show current position")
        print("  'quit' - Exit the controller")
    
    def set_position(self, x, y, z):
        """Set the drone's position"""
        self.position['x'] = x
        self.position['y'] = y
        self.position['z'] = z
        print(f"Position set to: ({x:.2f}, {y:.2f}, {z:.2f})")
    
    def takeoff(self):
        """Start flying"""
        if not self.is_flying:
            self.is_flying = True
            print("Drone taking off...")
            # Here you would send commands to Gazebo
        else:
            print("Drone is already flying!")
    
    def land(self):
        """Land the drone"""
        if self.is_flying:
            self.is_flying = False
            print("Drone landing...")
            # Here you would send commands to Gazebo
        else:
            print("Drone is already on the ground!")
    
    def move_forward(self, distance=1.0):
        """Move drone forward"""
        if self.is_flying:
            self.position['y'] += distance
            print(f"Moving forward {distance}m")
            # Here you would send commands to Gazebo
        else:
            print("Drone must be flying to move!")
    
    def move_backward(self, distance=1.0):
        """Move drone backward"""
        if self.is_flying:
            self.position['y'] -= distance
            print(f"Moving backward {distance}m")
            # Here you would send commands to Gazebo
        else:
            print("Drone must be flying to move!")
    
    def move_left(self, distance=1.0):
        """Move drone left"""
        if self.is_flying:
            self.position['x'] -= distance
            print(f"Moving left {distance}m")
            # Here you would send commands to Gazebo
        else:
            print("Drone must be flying to move!")
    
    def move_right(self, distance=1.0):
        """Move drone right"""
        if self.is_flying:
            self.position['x'] += distance
            print(f"Moving right {distance}m")
            # Here you would send commands to Gazebo
        else:
            print("Drone must be flying to move!")
    
    def move_up(self, distance=1.0):
        """Move drone up"""
        if self.is_flying:
            self.position['z'] += distance
            print(f"Moving up {distance}m")
            # Here you would send commands to Gazebo
        else:
            print("Drone must be flying to move!")
    
    def move_down(self, distance=1.0):
        """Move drone down"""
        if self.is_flying:
            new_z = max(0.5, self.position['z'] - distance)
            self.position['z'] = new_z
            print(f"Moving down {distance}m")
            # Here you would send commands to Gazebo
        else:
            print("Drone must be flying to move!")
    
    def get_status(self):
        """Show current drone status"""
        status = f"""
Drone Status:
  Position: ({self.position['x']:.2f}, {self.position['y']:.2f}, {self.position['z']:.2f})
  Orientation: ({self.orientation['roll']:.2f}, {self.orientation['pitch']:.2f}, {self.orientation['yaw']:.2f})
  Flying: {self.is_flying}
        """
        print(status)
    
    def run(self):
        """Main control loop"""
        print("\nSimple Drone Controller is running...")
        print("Type commands (or 'help' for commands list):")
        
        while True:
            try:
                command = input("> ").lower().strip()
                
                if command == 'quit' or command == 'exit':
                    print("Exiting drone controller...")
                    break
                elif command == 'help':
                    print("Commands: takeoff, land, forward, backward, left, right, up, down, status, quit")
                elif command == 'takeoff':
                    self.takeoff()
                elif command == 'land':
                    self.land()
                elif command == 'forward':
                    self.move_forward()
                elif command == 'backward':
                    self.move_backward()
                elif command == 'left':
                    self.move_left()
                elif command == 'right':
                    self.move_right()
                elif command == 'up':
                    self.move_up()
                elif command == 'down':
                    self.move_down()
                elif command == 'status':
                    self.get_status()
                else:
                    print(f"Unknown command: {command}")
                    print("Type 'help' for available commands")
                
                time.sleep(0.1)  # Small delay
                
            except KeyboardInterrupt:
                print("\nExiting drone controller...")
                break
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    controller = SimpleDroneController()
    controller.run() 