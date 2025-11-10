## System Components
- IoT Devices: Characteristics, task generation patterns, constraints
- UAVs: Mobility models, communication range, computation capacity, cost
- Edge Servers (ES): Fixed locations, computation resources, bandwidth limits
- Cloud: Unlimited resources but highest latency and cost

## Data Models
- Task Model: [Data size, CPU cycles, delay deadline]
- UAV State: [Position (x, y), altitude, velocity, remaining battery]
- ES Configuration: [Location, computation capacity, communication bandwidth]

## Key Algorithms
- UAV Placement: K-means clustering for optimal positioning
- Task Matching: R-TMSC algorithm for IoT-UAV-ES association
- Offloading Decision: Heuristic for task routing
- Profit Maximization: SP revenue vs. operational cost

## Performance Metrics
- Served IoT Count: % of successfully served devices
- User Satisfaction: Ratio of satisfied to total requests
- SP Profit: Revenue minus operational costs
- UAV Count: Total number of UAVs deployed
- Average Latency: Task completion time