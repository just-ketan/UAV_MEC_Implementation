# UAV-Assisted Mobile Edge Computing System

A complete simulation framework for studying UAV-assisted task offloading in urban IoT environments.

## Project Structure

iFogSim/
├── src/org/uav_mec/
│ ├── communication/ # SINR, LoS, path loss calculations
│ ├── task/ # IoT device & task models
│ ├── uav/ # UAV entity & management
│ ├── edgeserver/ # Edge server resource models
│ ├── offloading/ # Matching algorithms & optimization
│ ├── simulation/ # Core simulation engine
│ └── utils/ # Configuration constants
├── bin/ # Compiled Java bytecode
├── results/ # Simulation results (CSV, reports)
└── src/

text

## Features Implemented

✅ **Day 1:** Core simulation engine with full IoT-UAV-ES stack
✅ **Day 2:** Analytics & CSV export modules
✅ **Day 3:** Scenario configuration & performance metrics
✅ **Day 4:** Batch simulation runner
✅ **Day 5:** Comparison analyzer & reporting

## Running Simulations

### Single Scenario
java -cp bin org.uav_mec.simulation.SimulationManager

text

### Batch Scenarios
java -cp bin org.uav_mec.simulation.EnhancedBatchRunner

text

## System Architecture

- **100 IoT Devices** distributed across 1km × 1km urban area
- **5 UAVs** deployed at 100m altitude
- **3 Edge Servers** with distributed computing capacity
- **SINR-based communication model** for realistic wireless
- **Three-sided matching** for optimal task offloading
- **Financial model** tracking revenue, cost, and profit

## Key Metrics

- Task completion rate
- User satisfaction score
- Service provider profit
- Resource utilization
- Coverage percentage

## Results

Baseline Results:
- Revenue: $123,000
- Operational Cost: $12,300,050
- Net Profit: -$12,177,050 (requires optimization)
- User Satisfaction: 30.1%
- Service Completion: 100%

