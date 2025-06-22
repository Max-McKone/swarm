#!/bin/bash

echo "Starting Drone Simulation..."

# Check if GUI mode is requested
if [ "$1" = "gui" ]; then
    echo "Running in GUI mode..."
    gz sim -g drone_gazebo/stable_world.world
elif [ "$1" = "server" ]; then
    echo "Running in server mode..."
    gz sim -s drone_gazebo/stable_world.world -v 4
else
    echo "On macOS, you must specify either 'gui' or 'server' mode."
    echo "Usage:"
    echo "  ./run_simulation.sh gui    # Run with GUI"
    echo "  ./run_simulation.sh server # Run in server mode"
    echo ""
    echo "Defaulting to GUI mode..."
    gz sim -g drone_gazebo/stable_world.world
fi 