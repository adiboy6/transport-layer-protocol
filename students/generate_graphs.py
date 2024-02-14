import os
import matplotlib.pyplot as plt

# Parse the log file
filepath = os.getcwd()+'/metrics/'
for filename in os.listdir(filepath+'logs/'):
    times = []
    cwnd_sizes = []
    throughputs = []
    data = {}
    if filename.startswith('log-'):
        with open(filepath+'logs/'+filename, 'r') as f:
            for line in f:
                parts = line.split()
                port = parts[1]
                if port not in data:
                    data[port] = {'times': [], 'cwnd_sizes': [], 'throughputs': []}
                if parts[3] == 'data]':
                    data[port]['times'].append(float(parts[4]))
                    data[port]['cwnd_sizes'].append(float(parts[5]))
                elif parts[3] == 'ack]':
                    data[port]['throughputs'].append(float(parts[5]))
                
            # Generate the graphs
            try:
                plt.figure()
                for port, values in data.items():
                    plt.plot(values['times'], values['cwnd_sizes'], label=f'Port {port}')
                plt.title('Congestion Window Size Over Time')
                plt.xlabel('Time (s)')
                plt.ylabel('Congestion Window Size (packets)')
                plt.legend()
                plt.savefig(filepath+'graphs/'+'cwnd-'+filename[:-4]+'.png')
            except Exception as e:
                print(e)
                print("error in figure 1!")
            
            # for port, values in data.items():
            #     try:
            #         plt.figure()
            #         plt.plot(values['times'], values['cwnd_sizes'])
            #         plt.title(f'Congestion Window Size Over Time (Port {port})')
            #         plt.xlabel('Time (s)')
            #         plt.ylabel('Congestion Window Size (packets)')
            #         plt.savefig(filepath+'graphs/'+'cwnd-'+filename[:-4]+'-'+port+'.png')
            #     except Exception as e:
            #         print(e)
            #         print("error in figure 1!")

            # try:
            #     plt.figure()
            #     plt.plot(times, throughputs)
            #     plt.title('Throughput Over Time')
            #     plt.xlabel('Time (s)')
            #     plt.ylabel('Throughput (bytes/s)')
            #     plt.axhline(y=10, color='r', linestyle='--')
            #     plt.savefig('throughput'+filename[:-4]+'.png')
            # except Exception as e:
            #     print(e)
            #     print("error in figure 2!")