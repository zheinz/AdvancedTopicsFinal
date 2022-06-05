#Import desired modules
import statistics
import plotly.graph_objects as go
import os

#Read in the data for baselines results
baselinesReward = {}
baselinesTime = {}

for filename in os.listdir("baselines"):
    file = open("baselines/" + filename, 'r') 
    lines = file.readlines()

    reward = []
    time = []

    for i in range(0,200,2):
        reward.append(float(lines[i]))
    
    for i in range(1,200,2):
        time.append(float(lines[i]))

    baselinesReward.update({filename.strip(".txt"): reward})
    baselinesTime.update({filename.strip(".txt"): time})

#Read in data for the permuation attack results
permutationReward = {}
permutaionTime = {}

for filename in os.listdir("permutation"):
    file = open("permutation/"+filename, 'r')
    lines = file.readlines()

    reward = []
    time = []

    for i in range(0,200,2):
        reward.append(float(lines[i]))
    
    for i in range(1,200,2):
        time.append(float(lines[i]))

    permutationReward.update({filename.strip(".txt"): reward})
    permutaionTime.update({filename.strip(".txt"): time})

#Read in the data for the noise attack results
noiseReward = {}
noiseTime = {}

for filename in os.listdir("noise"):
    file = open("noise/"+filename, 'r')
    lines = file.readlines()

    reward = []
    time = []

    for i in range(0,200,2):
        reward.append(float(lines[i]))
    
    for i in range(1,200,2):
        time.append(float(lines[i]))

    noiseReward.update({filename.strip(".txt"): reward})
    noiseTime.update({filename.strip(".txt"): time})


#__________________Caluclating Averages to use in Graphs_________________________
temp = ['05', '10', '25', '50', '90']

permutaionRewardMeansModel1 = []
permutaionRewardMeansModel2 = []
permutaionRewardMeansModel3 = []
permutationTimeMeansModel1 = []
permutationTimeMeansModel2 = []
permutationTimeMeansModel3 = []
noiseRewardMeansModel1 = []
noiseRewardMeansModel2 = []
noiseRewardMeansModel3 = []
noiseTimeMeansModel1 = []
noiseTimeMeansModel2 = []
noiseTimeMeansModel3 = []
for i in temp:
    permutaionRewardMeansModel1.append(statistics.mean(permutationReward['M1P{}'.format(i)]))
    permutaionRewardMeansModel2.append(statistics.mean(permutationReward['M2P{}'.format(i)]))
    permutaionRewardMeansModel3.append(statistics.mean(permutationReward['M3P{}'.format(i)]))
    permutationTimeMeansModel1.append(statistics.mean(permutaionTime['M1P{}'.format(i)]))
    permutationTimeMeansModel2.append(statistics.mean(permutaionTime['M2P{}'.format(i)]))
    permutationTimeMeansModel3.append(statistics.mean(permutaionTime['M3P{}'.format(i)]))
    noiseRewardMeansModel1.append(statistics.mean(noiseReward['M1N{}'.format(i)]))
    noiseRewardMeansModel2.append(statistics.mean(noiseReward['M2N{}'.format(i)]))
    noiseRewardMeansModel3.append(statistics.mean(noiseReward['M3N{}'.format(i)]))
    noiseTimeMeansModel1.append(statistics.mean(noiseTime['M1N{}'.format(i)]))
    noiseTimeMeansModel2.append(statistics.mean(noiseTime['M2N{}'.format(i)]))
    noiseTimeMeansModel3.append(statistics.mean(noiseTime['M3N{}'.format(i)]))


#______________________Caluclating Mins and Maxes to use in Graphs _____________________________
permutaionRewardMinModel1 = []
permutaionRewardMinModel2 = []
permutaionRewardMinModel3 = []
permutationTimeMinModel1 = []
permutationTimeMinModel2 = []
permutationTimeMinModel3 = []
noiseRewardMinModel1 = []
noiseRewardMinModel2 = []
noiseRewardMinModel3 = []
noiseTimeMinModel1 = []
noiseTimeMinModel2 = []
noiseTimeMinModel3 = []

permutaionRewardMaxModel1 = []
permutaionRewardMaxModel2 = []
permutaionRewardMaxModel3 = []
permutationTimeMaxModel1 = []
permutationTimeMaxModel2 = []
permutationTimeMaxModel3 = []
noiseRewardMaxModel1 = []
noiseRewardMaxModel2 = []
noiseRewardMaxModel3 = []
noiseTimeMaxModel1 = []
noiseTimeMaxModel2 = []
noiseTimeMaxModel3 = []

for i in temp:
    permutaionRewardMinModel1.append(min(permutationReward['M1P{}'.format(i)]))
    permutaionRewardMinModel2.append(min(permutationReward['M2P{}'.format(i)]))
    permutaionRewardMinModel3.append(min(permutationReward['M3P{}'.format(i)]))
    permutationTimeMinModel1.append(min(permutaionTime['M1P{}'.format(i)]))
    permutationTimeMinModel2.append(min(permutaionTime['M2P{}'.format(i)]))
    permutationTimeMinModel3.append(min(permutaionTime['M3P{}'.format(i)]))
    noiseRewardMinModel1.append(min(noiseReward['M1N{}'.format(i)]))
    noiseRewardMinModel2.append(min(noiseReward['M2N{}'.format(i)]))
    noiseRewardMinModel3.append(min(noiseReward['M3N{}'.format(i)]))
    noiseTimeMinModel1.append(min(noiseTime['M1N{}'.format(i)]))
    noiseTimeMinModel2.append(min(noiseTime['M2N{}'.format(i)]))
    noiseTimeMinModel3.append(min(noiseTime['M3N{}'.format(i)]))

    permutaionRewardMaxModel1.append(max(permutationReward['M1P{}'.format(i)]))
    permutaionRewardMaxModel2.append(max(permutationReward['M2P{}'.format(i)]))
    permutaionRewardMaxModel3.append(max(permutationReward['M3P{}'.format(i)]))
    permutationTimeMaxModel1.append(max(permutaionTime['M1P{}'.format(i)]))
    permutationTimeMaxModel2.append(max(permutaionTime['M2P{}'.format(i)]))
    permutationTimeMaxModel3.append(max(permutaionTime['M3P{}'.format(i)]))
    noiseRewardMaxModel1.append(max(noiseReward['M1N{}'.format(i)]))
    noiseRewardMaxModel2.append(max(noiseReward['M2N{}'.format(i)]))
    noiseRewardMaxModel3.append(max(noiseReward['M3N{}'.format(i)]))
    noiseTimeMaxModel1.append(max(noiseTime['M1N{}'.format(i)]))
    noiseTimeMaxModel2.append(max(noiseTime['M2N{}'.format(i)]))
    noiseTimeMaxModel3.append(max(noiseTime['M3N{}'.format(i)]))


#_______________________GRAPHS______________________________________________
x_values = [0.05, 0.1, 0.25, 0.5, 0.9]

#Permutaion Reward Graph
permutationRewardGraph = go.Figure()
#permutationRewardGraph.add_hline(y=statistics.mean(baselinesReward['model1']), name='Model 1 Baseline', line_color='rgb(0,0,0)')
#permutationRewardGraph.add_hline(y=statistics.mean(baselinesReward['model2']), name='Model 2 Baseline', line_color='rgb(0,0,0)')
#permutationRewardGraph.add_hline(y=statistics.mean(baselinesReward['model3']), name='Model 3 Baseline', line_color='rgb(0,0,0)')
permutationRewardGraph.add_trace(go.Scatter(x=x_values, y=permutaionRewardMeansModel1, mode='lines+markers', name='Model 1 Average', showlegend=True, line_color='rgb(255,0,0)'))
permutationRewardGraph.add_trace(go.Scatter(x=x_values+x_values[::-1], y=permutaionRewardMaxModel1+permutaionRewardMinModel1[::-1], name='Model 1 Spread', fill='toself', showlegend=True, hoverinfo='skip', fillcolor='rgba(255,0,0,0.25)',line_color='rgba(0,0,0,0)'))
permutationRewardGraph.add_trace(go.Scatter(x=x_values, y=permutaionRewardMeansModel2, mode='lines+markers', name='Model 2 Average', showlegend=True, line_color='rgb(0,100,0)'))
permutationRewardGraph.add_trace(go.Scatter(x=x_values+x_values[::-1], y=permutaionRewardMaxModel2+permutaionRewardMinModel2[::-1], name='Model 2 Spread', fill='toself', showlegend=True, hoverinfo='skip', fillcolor='rgba(0,100,0,0.25)',line_color='rgba(0,0,0,0)'))
permutationRewardGraph.add_trace(go.Scatter(x=x_values, y=permutaionRewardMeansModel3, mode='lines+markers', name='Model 3 Average', showlegend=True, line_color='rgb(0,0,255)'))
permutationRewardGraph.add_trace(go.Scatter(x=x_values+x_values[::-1], y=permutaionRewardMaxModel3+permutaionRewardMinModel3[::-1], name='Model 3 Spread', fill='toself', showlegend=True, hoverinfo='skip', fillcolor='rgba(0,0,255,0.25)',line_color='rgba(0,0,0,0)'))
permutationRewardGraph.update_layout(title="Permutation Attack Probablility vs Average Cumulative Reward", title_font_size=50, xaxis_title="Probability of Attack (%)", yaxis_title='Average Cumulative Reward', legend_title='Model', legend_font_size=25)
permutationRewardGraph.update_xaxes(tickfont_size=50, title_font_size=50)
permutationRewardGraph.update_yaxes(tickfont_size=50, title_font_size=50)
permutationRewardGraph.show()

#Permutaion Time Graph
permutationTimeGraph = go.Figure()
#permutationTimeGraph.add_hline(y=statistics.mean(baselinesTime['model1']), name='Model 1 Baseline', line_color='rgb(0,0,0)')
#permutationTimeGraph.add_hline(y=statistics.mean(baselinesTime['model2']), name='Model 2 Baseline', line_color='rgb(0,0,0)')
#permutationTimeGraph.add_hline(y=statistics.mean(baselinesTime['model3']), name='Model 3 Baseline', line_color='rgb(0,0,0)')
permutationTimeGraph.add_trace(go.Scatter(x=x_values, y=permutationTimeMeansModel1, mode='lines+markers', name='Model 1 Average', showlegend=True, line_color='rgb(255,0,0)'))
permutationTimeGraph.add_trace(go.Scatter(x=x_values+x_values[::-1], y=permutationTimeMaxModel1+permutationTimeMinModel1[::-1], name='Model 1 Spread', fill='toself', showlegend=True, hoverinfo='skip', fillcolor='rgba(255,0,0,0.25)',line_color='rgba(0,0,0,0)'))
permutationTimeGraph.add_trace(go.Scatter(x=x_values, y=permutationTimeMeansModel2, mode='lines+markers', name='Model 2 Average', showlegend=True, line_color='rgb(0,100,0)'))
permutationTimeGraph.add_trace(go.Scatter(x=x_values+x_values[::-1], y=permutationTimeMaxModel2+permutationTimeMinModel2[::-1], name='Model 2 Spread', fill='toself', showlegend=True, hoverinfo='skip', fillcolor='rgba(0,100,0,0.25)',line_color='rgba(0,0,0,0)'))
permutationTimeGraph.add_trace(go.Scatter(x=x_values, y=permutationTimeMeansModel3, mode='lines+markers', name='Model 3 Average', showlegend=True, line_color='rgb(0,0,255)'))
permutationTimeGraph.add_trace(go.Scatter(x=x_values+x_values[::-1], y=permutationTimeMaxModel3+permutationTimeMinModel3[::-1], name='Model 3 Spread', fill='toself', showlegend=True, hoverinfo='skip', fillcolor='rgba(0,0,255,0.25)',line_color='rgba(0,0,0,0)'))
permutationTimeGraph.update_layout(title="Permutation Attack Probablility vs Average Number of Cycles per Game", title_font_size=50, xaxis_title="Probability of Attack (%)", yaxis_title='Average Number of Cycles', legend_title='Model', legend_font_size=25)
permutationTimeGraph.update_xaxes(tickfont_size=50, title_font_size=50)
permutationTimeGraph.update_yaxes(tickfont_size=50, title_font_size=50)
permutationTimeGraph.show()

#Noise Reward Graph
noiseRewardGraph = go.Figure()
#noiseRewardGraph.add_hline(y=statistics.mean(baselinesReward['model1']), name='Model 1 Baseline', line_color='rgb(0,0,0)')
#noiseRewardGraph.add_hline(y=statistics.mean(baselinesReward['model2']), name='Model 2 Baseline', line_color='rgb(0,0,0)')
#noiseRewardGraph.add_hline(y=statistics.mean(baselinesReward['model3']), name='Model 3 Baseline', line_color='rgb(0,0,0)')
noiseRewardGraph.add_trace(go.Scatter(x=x_values, y=noiseRewardMeansModel1, mode='lines+markers', name='Model 1 Average', showlegend=True, line_color='rgb(255,0,0)'))
noiseRewardGraph.add_trace(go.Scatter(x=x_values+x_values[::-1], y=noiseRewardMaxModel1+noiseRewardMinModel1[::-1], name='Model 1 Spread', fill='toself', showlegend=True, hoverinfo='skip', fillcolor='rgba(255,0,0,0.25)',line_color='rgba(0,0,0,0)'))
noiseRewardGraph.add_trace(go.Scatter(x=x_values, y=noiseRewardMeansModel2, mode='lines+markers', name='Model 2 Average', showlegend=True, line_color='rgb(0,100,0)'))
noiseRewardGraph.add_trace(go.Scatter(x=x_values+x_values[::-1], y=noiseRewardMaxModel2+noiseRewardMinModel2[::-1], name='Model 2 Spread', fill='toself', showlegend=True, hoverinfo='skip', fillcolor='rgba(0,100,0,0.25)',line_color='rgba(0,0,0,0)'))
noiseRewardGraph.add_trace(go.Scatter(x=x_values, y=noiseRewardMeansModel3, mode='lines+markers', name='Model 3 Average', showlegend=True, line_color='rgb(0,0,255)'))
noiseRewardGraph.add_trace(go.Scatter(x=x_values+x_values[::-1], y=noiseRewardMaxModel3+noiseRewardMinModel3[::-1], name='Model 3 Spread', fill='toself', showlegend=True, hoverinfo='skip', fillcolor='rgba(0,0,255,0.25)',line_color='rgba(0,0,0,0)'))
noiseRewardGraph.update_layout(title="Size of Noise vs Average Cumulative Reward", title_font_size=50, xaxis_title="Noise Amount (%)", yaxis_title='Average Cumulative Reward', legend_title='Model', legend_font_size=25)
noiseRewardGraph.update_xaxes(tickfont_size=50, title_font_size=50)
noiseRewardGraph.update_yaxes(tickfont_size=50, title_font_size=50)
noiseRewardGraph.show()

#Noise Time Graph
noiseTimeGraph = go.Figure()
#noiseTimeGraph.add_hline(y=statistics.mean(baselinesTime['model1']), name='Model 1 Baseline', line_color='rgb(0,0,0)')
#noiseTimeGraph.add_hline(y=statistics.mean(baselinesTime['model2']), name='Model 2 Baseline', line_color='rgb(0,0,0)')
#noiseTimeGraph.add_hline(y=statistics.mean(baselinesTime['model3']), name='Model 3 Baseline', line_color='rgb(0,0,0)')
noiseTimeGraph.add_trace(go.Scatter(x=x_values, y=noiseTimeMeansModel1, mode='lines+markers', name='Model 1 Average', showlegend=True, line_color='rgb(255,0,0)'))
noiseTimeGraph.add_trace(go.Scatter(x=x_values+x_values[::-1], y=noiseTimeMaxModel1+noiseTimeMinModel1[::-1], name='Model 1 Spread', fill='toself', showlegend=True, hoverinfo='skip', fillcolor='rgba(255,0,0,0.25)',line_color='rgba(0,0,0,0)'))
noiseTimeGraph.add_trace(go.Scatter(x=x_values, y=noiseTimeMeansModel2, mode='lines+markers', name='Model 2 Average', showlegend=True, line_color='rgb(0,100,0)'))
noiseTimeGraph.add_trace(go.Scatter(x=x_values+x_values[::-1], y=noiseTimeMaxModel2+noiseTimeMinModel2[::-1], name='Model 2 Spread', fill='toself', showlegend=True, hoverinfo='skip', fillcolor='rgba(0,100,0,0.25)',line_color='rgba(0,0,0,0)'))
noiseTimeGraph.add_trace(go.Scatter(x=x_values, y=noiseTimeMeansModel3, mode='lines+markers', name='Model 3 Average', showlegend=True, line_color='rgb(0,0,255)'))
noiseTimeGraph.add_trace(go.Scatter(x=x_values+x_values[::-1], y=noiseTimeMaxModel3+noiseTimeMinModel3[::-1], name='Model 3 Spread', fill='toself', showlegend=True, hoverinfo='skip', fillcolor='rgba(0,0,255,0.25)',line_color='rgba(0,0,0,0)'))
noiseTimeGraph.update_layout(title="Size of Noise vs Average Number of Cycles per Game", title_font_size=50, xaxis_title="Noise Amount (%)", yaxis_title='Average Number of Cycles', legend_title='Model', legend_font_size=25)
noiseTimeGraph.update_xaxes(tickfont_size=50, title_font_size=50)
noiseTimeGraph.update_yaxes(tickfont_size=50, title_font_size=50)
noiseTimeGraph.show()
