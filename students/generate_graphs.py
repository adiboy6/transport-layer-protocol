import os
import matplotlib.pyplot as plt

# Parse the log file
times = []
cwnd_sizes = []
throughputs = []
for filename in os.listdir(os.getcwd()):
    if filename.startswith('log-'):
        print(filename)
        with open(filename, 'r') as f:
            for line in f:
                parts = line.split()
                if parts[1] == 'data]':
                    times.append(float(parts[2]))
                    cwnd_sizes.append(float(parts[3]))
                elif parts[1] == 'ack]':
                    throughputs.append(float(parts[3]))
                
            # Generate the graphs
            try:
                plt.figure()
                plt.plot(times, cwnd_sizes)
                plt.title('Congestion Window Size Over Time')
                plt.xlabel('Time (s)')
                plt.ylabel('Congestion Window Size (packets)')
                # plt.xlim(min(times), min(times) + 0.01)  # Adjust the 0.01 to change the range of x-values displayed
                plt.savefig('cwnd'+filename[:-4]+'.png')
            except Exception as e:
                print(e)
                print("error in figure 1!")

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