#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import sys

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

def load_data(results_dir):
    data = {}
    files = {
        'iot': 'iot_device_metrics.csv',
        'uav': 'uav_metrics.csv',
        'es': 'edge_server_metrics.csv',
        'summary': 'simulation_summary.csv'
    }
    
    for key, filename in files.items():
        filepath = Path(results_dir) / filename
        if filepath.exists():
            data[key] = pd.read_csv(filepath)
            print(f"✓ Loaded {filename}")
    return data

def plot_satisfaction(iot_data, output_dir):
    fig, ax = plt.subplots(figsize=(10, 6))
    if 'Avg_Satisfaction' in iot_data.columns:
        satisfaction = iot_data['Avg_Satisfaction'].dropna()
        ax.hist(satisfaction, bins=20, color='steelblue', edgecolor='black', alpha=0.7)
        ax.axvline(satisfaction.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {satisfaction.mean():.3f}')
        ax.set_xlabel('User Satisfaction', fontsize=12)
        ax.set_ylabel('Number of Devices', fontsize=12)
        ax.set_title('IoT Device Satisfaction Distribution', fontsize=14, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'{output_dir}/satisfaction_distribution.png', dpi=300)
        print(f"✓ Saved: satisfaction_distribution.png")
        plt.close()

def plot_success_rate(iot_data, output_dir):
    fig, ax = plt.subplots(figsize=(10, 6))
    if 'Success_Rate' in iot_data.columns:
        success = iot_data['Success_Rate'].dropna()
        ax.scatter(range(len(success)), success, alpha=0.6, s=100, color='green')
        ax.axhline(success.mean(), color='red', linestyle='--', linewidth=2, label=f'Average: {success.mean():.1f}%')
        ax.set_xlabel('IoT Device ID', fontsize=12)
        ax.set_ylabel('Task Success Rate (%)', fontsize=12)
        ax.set_title('Task Completion Success Rate by Device', fontsize=14, fontweight='bold')
        ax.set_ylim([0, 110])
        ax.legend()
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'{output_dir}/success_rate.png', dpi=300)
        print(f"✓ Saved: success_rate.png")
        plt.close()

def plot_uav_coverage(uav_data, output_dir):
    fig, ax = plt.subplots(figsize=(12, 6))
    if 'Associated_IoTs' in uav_data.columns:
        ax.bar(uav_data['UAV_ID'], uav_data['Associated_IoTs'], color='steelblue', edgecolor='black', alpha=0.7)
        ax.set_xlabel('UAV ID', fontsize=12)
        ax.set_ylabel('Associated IoT Devices', fontsize=12)
        ax.set_title('UAV Coverage (IoT Associations)', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/uav_coverage.png', dpi=300)
        print(f"✓ Saved: uav_coverage.png")
        plt.close()

def plot_es_performance(es_data, output_dir):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    if 'Tasks_Completed' in es_data.columns:
        ax1.bar(es_data['ES_ID'], es_data['Tasks_Completed'], color='steelblue', edgecolor='black', alpha=0.7)
        ax1.set_xlabel('Edge Server ID', fontsize=12)
        ax1.set_ylabel('Tasks Completed', fontsize=12)
        ax1.set_title('Edge Server Task Processing', fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.3, axis='y')
    
    if 'Tasks_Dropped' in es_data.columns:
        ax2.bar(es_data['ES_ID'], es_data['Tasks_Dropped'], color='coral', edgecolor='black', alpha=0.7)
        ax2.set_xlabel('Edge Server ID', fontsize=12)
        ax2.set_ylabel('Tasks Dropped', fontsize=12)
        ax2.set_title('Edge Server Task Loss', fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/es_performance.png', dpi=300)
    print(f"✓ Saved: es_performance.png")
    plt.close()

def main():
    results_dir = './iFogSim/results' if len(sys.argv) < 2 else sys.argv[1]
    print(f"Loading results from: {results_dir}")
    print("=" * 80)
    
    data = load_data(results_dir)
    
    if not data:
        print("✗ No data files found!")
        return
    
    output_dir = f"{results_dir}/plots"
    Path(output_dir).mkdir(exist_ok=True)
    
    print(f"\nGenerating visualizations...")
    print("=" * 80)
    
    if 'iot' in data:
        plot_satisfaction(data['iot'], output_dir)
        plot_success_rate(data['iot'], output_dir)
    
    if 'uav' in data:
        plot_uav_coverage(data['uav'], output_dir)
    
    if 'es' in data:
        plot_es_performance(data['es'], output_dir)
    
    print("=" * 80)
    print(f"✓ All plots saved to: {output_dir}")
    print("✓ Visualization complete!")

if __name__ == '__main__':
    main()
