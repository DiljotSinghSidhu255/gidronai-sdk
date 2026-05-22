# GidronAI Python SDK

Official Python client for the GidronAI Synthetic Reality Engine API.

## Installation

```bash
pip install gidronai
```

## Quick Start

```python
from gidronai import GidronClient

client = GidronClient(api_key="your-api-key")

scene = client.scenes.create(
    environment="urban_intersection",
    weather="rain",
    time_of_day="dusk",
    num_agents=12,
    physics=True
)

dataset = scene.export(
    formats=["rgb", "depth", "segmentation", "lidar"],
    resolution=(1920, 1080),
    frames=500
)
dataset.download("./training_data/")
```

## Features

- **Scene Generation** - Procedural urban, rural, indoor, and custom environments
- **Physics Simulation** - Rigid body, fluid dynamics, and soft body physics
- **Multi-Agent** - Autonomous agents with configurable behavior
- **Auto-Labeling** - Depth maps, segmentation masks, 3D bounding boxes, LiDAR
- **Batch Processing** - Millions of frames with horizontal scaling

## License

Apache 2.0
