# 🤖 ROS2 Hello World - Talker / Listener / Launch

> Mon tout premier projet ROS2 fonctionnel basé sur Python 🐍 et ROS2 Humble 🐢 !

## 🎯 Objectif

- 📦 Créer un package ROS2 (ament_python)
- 📤 Écrire un Publisher (`talker.py`)
- 📥 Écrire un Subscriber (`listener.py`)
- 🛠️ Lancer le tout avec un fichier `launch.py`

## 🧠 Apprentissage

- `rclpy` pour gérer les noeuds
- Publisher/Subscriber avec des messages `std_msgs/String`
- Fichier `launch` pour démarrer plusieurs noeuds facilement

## 📁 Arborescence
ros2_ws/
├── src/
│   └── my_first_pkg/
│       ├── my_first_pkg/
│       │   ├── talker.py ✅
│       │   ├── listener.py ✅
│       │   └── launch/
│       │       └── my_launch.py ✅
│       ├── package.xml 
│       ├── setup.py 
│       ├── setup.cfg 
│       └── test/ ...

