import matplotlib.pyplot as plt


def GenerateGANTT_Chart(processList, process_Timing):
        
        G_fig, G_ax = plt.subplots()
        for i, (process, timings) in enumerate(process_Timing.items()):
            start, end = timings
            ax.barh(i, end - start, left=start, align='center', label=process)

        ax.set_xlabel('Time')
        ax.set_yticks(range(len(process_Timing)))
        ax.set_yticklabels(process_Timing.keys())
        plt.grid(axis='x')
        plt.savefig("./GANTT_OUTPUT/GTChart.png", bbox_inches='tight', dpi=150)
        