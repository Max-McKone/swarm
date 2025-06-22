#!/usr/bin/env python3
"""
Drone Controller for Gazebo Simulation
Controls a quadrotor drone using Gazebo's Python API
"""

import time
import math
from gz.msgs10.vector3d_pb2 import Vector3d
from gz.msgs10.pose_pb2 import Pose
from gz.transport13 import Node

class DroneController:
    def __init__(self):
        """Initialize the drone controller"""
        self.node = Node()
        
        # Create publishers for controlling the drone
        self.pose_pub = self.node.advertise(
            "/model/drone/set_pose", "gz.msgs.Pose")
        
        # Create subscribers for getting drone state
        self.pose_sub = self.node.subscribe(
            "/model/drone/pose", self.on_pose_received)
        
        self.current_pose = Pose()
        self.current_pose.position.x = 0.0
        self.current_pose.position.y = 0.0
        self.current_pose.position.z = 2.0
        
        print("Drone Controller initialized!")
        print("Commands:")
        print("  'takeoff' - Move drone up")
        print("  'land' - Move drone down")
        print("  'forward' - Move drone forward")
        print("  'backward' - Move drone backward")
        print("  'left' - Move drone left")
        print("  'right' - Move drone right")
        print("  'hover' - Keep drone in current position")
        print("  'quit' - Exit the controller")
    
    def on_pose_received(self, msg):
        """Callback for receiving drone pose updates"""
        self.current_pose = msg
    
    def set_pose(self, x, y, z, roll=0, pitch=0, yaw=0):
        """Set the drone's position and orientation"""
        pose = Pose()
        pose.position.x = x
        pose.position.y = y
        pose.position.z = z
        pose.orientation.x = roll
        pose.orientation.y = pitch
        pose.orientation.z = yaw
        
        self.pose_pub.publish(pose)
        print(f"Moving drone to position: ({x:.2f}, {y:.2f}, {z:.2f})")
    
    def takeoff(self):
        """Move drone up"""
        current_z = self.current_pose.position.z
        self.set_pose(
            self.current_pose.position.x,
            self.current_pose.position.y,
            current_z + 1.0
        )
    
    def land(self):
        """Move drone down"""
        current_z = self.current_pose.position.z
        new_z = max(0.5, current_z - 1.0)  # Don't go below 0.5m
        self.set_pose(
            self.current_pose.position.x,
            self.current_pose.position.y,
            new_z
        )
    
    def move_forward(self):
        """Move drone forward (positive Y direction)"""
        self.set_pose(
            self.current_pose.position.x,
            self.current_pose.position.y + 1.0,
            self.current_pose.position.z
        )
    
    def move_backward(self):
        """Move drone backward (negative Y direction)"""
        self.set_pose(
            self.current_pose.position.x,
            self.current_pose.position.y - 1.0,
            self.current_pose.position.z
        )
    
    def move_left(self):
        """Move drone left (negative X direction)"""
        self.set_pose(
            self.current_pose.position.x - 1.0,
            self.current_pose.position.y,
            self.current_pose.position.z
        )
    
    def move_right(self):
        """Move drone right (positive X direction)"""
        self.set_pose(
            self.current_pose.position.x + 1.0,
            self.current_pose.position.y,
            self.current_pose.position.z
        )
    
    def hover(self):
        """Keep drone in current position"""
        print("Hovering at current position")
    
    def run(self):
        """Main control loop"""
        print("\nDrone Controller is running...")
        print("Type commands (or 'help' for commands list):")
        
        while True:
            try:
                command = input("> ").lower().strip()
                
                if command == 'quit' or command == 'exit':
                    print("Exiting drone controller...")
                    break
                elif command == 'help':
                    print("Commands: takeoff, land, forward, backward, left, right, hover, quit")
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
                elif command == 'hover':
                    self.hover()
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
    controller = DroneController()
    controller.run() 