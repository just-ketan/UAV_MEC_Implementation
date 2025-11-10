### Simulation Components
- Datacenter: Represents cloud resources
- Host: Physical machines in datacenter
- Vm: Virtual machines running on hosts
- Cloudlet: Tasks/jobs submitted for execution
- Broker: Manages VM creation and cloudlet submission

### Key Classes to Use
- Datacenter, DatacenterBroker, Host, Vm, Cloudlet
- CloudSim (main simulation engine)
- Log (for output)

### Network Simulation
- NetworkTopology: Models network latency
- HostToHostBandwidth: Bandwidth between hosts

### Usage Pattern
1. Initialize CloudSim
2. Create Datacenter(s)
3. Create Broker
4. Create VMs and submit to broker
5. Create Cloudlets and submit to broker
6. Start simulation
7. Retrieve results