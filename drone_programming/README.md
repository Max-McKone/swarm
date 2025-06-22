# Drone Swarm Programming Project

A Gazebo-based drone simulation environment for developing and testing drone swarm algorithms and control systems.

## 🚁 Overview

This project provides a complete simulation environment for drone programming using Gazebo. It includes:
- **Quadrotor drone models** with realistic physics
- **World files** for different simulation scenarios
- **Python controllers** for drone automation
- **Swarm simulation** capabilities for multiple drones

## 📁 Project Structure

```
drone_programming/
├── drone_gazebo/
│   ├── models/
│   │   └── quadrotor/          # Drone model with physics
│   ├── simple_drone_world.world
│   ├── stable_world.world
│   ├── enhanced_world.world
│   └── simple_stable_world.world
├── drone_controller.py         # Advanced drone controller
├── simple_drone_controller.py  # Basic drone controller
├── run_simulation.sh          # Simulation launcher script
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- **macOS** (tested on macOS 14+)
- **Gazebo** (installed via Homebrew)
- **Python 3.x**

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Max-McKone/swarm.git
   cd swarm
   ```

2. **Install Gazebo (if not already installed):**
   ```bash
   brew install gz
   ```

3. **Make scripts executable:**
   ```bash
   chmod +x run_simulation.sh
   chmod +x drone_controller.py
   chmod +x simple_drone_controller.py
   ```

### Running the Simulation

#### **GUI Mode (Recommended for development):**
```bash
./run_simulation.sh gui
```

#### **Server Mode (for automation):**
```bash
./run_simulation.sh server
```

#### **Direct commands:**
```bash
# GUI mode
gz sim -g drone_gazebo/simple_stable_world.world

# Server mode
gz sim -s drone_gazebo/simple_stable_world.world
```

## 🎮 Controlling the Drone

### **Method 1: Python Controller**

Run the simple drone controller:
```bash
python3 simple_drone_controller.py
```

Available commands:
- `takeoff` - Start flying
- `land` - Land the drone
- `forward` - Move forward
- `backward` - Move backward
- `left` - Move left
- `right` - Move right
- `up` - Move up
- `down` - Move down
- `status` - Show current position
- `quit` - Exit controller

### **Method 2: Manual Control in Gazebo**

1. Start the simulation in GUI mode
2. Click on the drone to select it
3. Use the simulation controls to play/pause
4. Move the camera to view from different angles

## 🌍 World Files

### **Available Worlds:**

1. **`simple_stable_world.world`** (Default)
   - Basic ground plane
   - Single quadrotor drone
   - Stable physics

2. **`enhanced_world.world`**
   - Sun lighting
   - Ground plane
   - Obstacles
   - Multiple objects

3. **`stable_world.world`**
   - Full physics simulation
   - Ground plane
   - Realistic gravity

## 🤖 Drone Models

### **Quadrotor Model**
- **Mass:** 1.316 kg
- **Collision:** Box geometry (0.5m × 0.5m × 0.1m)
- **Visual:** Mesh-based appearance
- **Physics:** Kinematic (doesn't fall through ground)

### **Model Properties:**
- **Inertia:** Realistic moment of inertia
- **Position:** Configurable spawn position
- **Kinematic:** True (prevents falling)

## 🔧 Customization

### **Adding New Drones**

1. **Copy the quadrotor model:**
   ```bash
   cp -r drone_gazebo/models/quadrotor drone_gazebo/models/my_drone
   ```

2. **Modify the model.sdf file:**
   - Change the model name
   - Adjust mass and inertia
   - Modify visual appearance

3. **Add to world file:**
   ```xml
   <include>
     <uri>file://path/to/my_drone</uri>
     <name>my_drone</name>
     <pose>0 0 2 0 0 0</pose>
   </include>
   ```

### **Creating Custom Worlds**

1. **Start with a template:**
   ```bash
   cp drone_gazebo/simple_stable_world.world drone_gazebo/my_world.world
   ```

2. **Add objects:**
   - Ground planes
   - Obstacles
   - Multiple drones
   - Lighting

3. **Configure physics:**
   - Gravity settings
   - Collision detection
   - Simulation parameters

## 🐛 Troubleshooting

### **Common Issues:**

1. **Drone falling through ground:**
   - Use `simple_stable_world.world`
   - Ensure drone is kinematic
   - Check collision geometry

2. **Models not loading:**
   - Verify file paths
   - Check model structure
   - Ensure proper SDF format

3. **Gazebo not starting:**
   - Check Gazebo installation
   - Verify world file syntax
   - Check for missing dependencies

### **macOS Specific Notes:**

- Gazebo requires `-g` (GUI) or `-s` (server) flag
- Cannot run both GUI and server in same terminal
- Use the provided `run_simulation.sh` script

## 🔮 Future Enhancements

### **Planned Features:**
- [ ] **Swarm coordination algorithms**
- [ ] **Path planning and navigation**
- [ ] **Obstacle avoidance**
- [ ] **Multi-drone simulation**
- [ ] **ROS integration**
- [ ] **Real-time control interfaces**
- [ ] **Sensor simulation (cameras, lidar)**
- [ ] **Mission planning tools**

### **Advanced Features:**
- [ ] **Formation flying**
- [ ] **Distributed control**
- [ ] **Fault tolerance**
- [ ] **Energy management**
- [ ] **Communication simulation**

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Test thoroughly**
5. **Submit a pull request**

## 📝 License

This project is open source. Feel free to use, modify, and distribute.

## 📞 Support

For issues and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review Gazebo documentation

---

**Happy Drone Programming! 🚁✨** 