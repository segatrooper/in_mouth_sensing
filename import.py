import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn import svm, datasets
import matplotlib.pyplot as plt
from collections import defaultdict

file_name = input("what file name?: ")
sensors = ["sensor" + str(i) for i in range(int(input("how many sensors?: ")))]
# print(sensors)
data = pd.read_csv(file_name + ".csv")
# print(data.head())
window_times = list(set((data["window"])))
# window_times.remove(0)
sensor_list = list()
super_sensor = dict()
for i in range(len(sensors)):
    sensor_list.append(dict())
    sensor_list[i]['mean'] = list()
    sensor_list[i]['std'] = list()
    sensor_list[i]['min'] = list()
    sensor_list[i]['max'] = list()
    sensor_list[i]['25'] = list()
    sensor_list[i]['50'] = list()
    sensor_list[i]['75'] = list()
    super_sensor['mean'] = list()
    super_sensor['std'] = list()
    super_sensor['min'] = list()
    super_sensor['max'] = list()
    super_sensor['25'] = list()
    super_sensor['50'] = list()
    super_sensor['75'] = list()
for w in window_times[0:100]:
    # print(w)
    window_data = data.loc[lambda df: df['window'] == w, :]
    # print(window_data)
    if window_data.shape != ():
        for i, v in enumerate(sensors):
            sensor_data = window_data[v]
            description = dict(sensor_data.describe().fillna(0))
            # print(description)
            sensor_list[i]['mean'].append(description['mean'])
            sensor_list[i]['std'].append(description['std'])
            sensor_list[i]['min'].append(description['min'])
            sensor_list[i]['max'].append(description['max'])
            sensor_list[i]['25'].append(description['25%'])
            sensor_list[i]['50'].append(description['50%'])
            sensor_list[i]['75'].append(description['75%'])
            
            super_sensor['mean'].append(description['mean'])
            super_sensor['std'].append(description['std'])
            super_sensor['min'].append(description['min'])
            super_sensor['max'].append(description['max'])
            super_sensor['25'].append(description['25%'])
            super_sensor['50'].append(description['50%'])
            super_sensor['75'].append(description['75%'])
random_output = np.random.randint(0,2,len(sensor_list[i]['mean']))
# random_input = np.column_stack(tuple([np.array([x]) for i in sensor_list for x in i.values()]))
# random_input = random_input.reshape(100, 28)







# RANDOM INPUT
'''
    think of random input as container of window - > each sensor - > each feature
'''
random_input = np.array([[]])
for i in range(len(sensor_list[0]['mean'])):
    temp_list = list()
    for j in range(len(sensor_list)):
        for k in sensor_list[j].keys():
            temp_list.append(sensor_list[j][k][i])
    # print(f"this is the temp list: {temp_list}")
    if (np.shape(random_input) == (1, 0)):
        random_input = np.array([temp_list])
    else:
        random_input = np.append(random_input, np.array([temp_list]), axis=0) # axis makes this 2D array instead of 1D
        
# print([sensor_list[0][x][0] for x in ['mean', 'std', 'min', 'max', '25', '50', '75']])
# print(np.shape(random_input))
# print(random_input) # this checks out





# LINEAR MODEL
linear = svm.SVC(kernel='linear', C=1, decision_function_shape='ovo').fit(random_input, random_output)# , sensor_list['min'], sensor_list['max'], sensor_list['25'], sensor_list['50'], sensor_list['75'])), np.random.randint(0,2,len(sensor_list['mean'])))
h = 0.01 # this is the number of steps one must choose

# SENSOR BOUNDARIES
sensor_output = defaultdict(dict) # this is where the boundaries and steps are stored
for a in range(len(sensor_list)):
    for i , v in super_sensor.items():
        sensor_output[a][i + '_min'], sensor_output[a][i + '_max'] = np.array(v).min() - 1, np.array(v).max() + 1
# print(sensor_output.keys())
# testing = f'''np.meshgrid({", ".join(['np.arange(sensor_output["' + i + '_min"], sensor_output["' + i + '_max"], h)' for i in list(sensor_list.keys())[0:2]])})'''
# i = list(sensor_list.keys())[0]



# GRID MAKING = using the h (steps) and boundaries before
primal_grid = list(); mean_grid = list()
for a in range(len(sensor_list)):
    for i in super_sensor.keys():
        primal_grid.append(list(np.arange(sensor_output[a][i + '_min'], sensor_output[a][i + '_max'], h)))

# print(random_input.shape)
for a in range(random_input.shape[1]):
    mean_grid.append(np.mean((random_input.T)[a]))

# testing = list()
# for i in list(sensor_list.keys()):
    # primal = np.arange(sensor_output[i + '_min'], sensor_output[i + '_max'], h)
    # testing.append(np.meshgrid(primal, np.arange(min(random_output) - 1, max(random_output) + 1, h))[0])
# print(primal_grid)

# print(len(testing))


# print(testing)
# sensor_revaling = eval(testing)# np.arange(mean_min, mean_max, h), np.arange(std_min, std_max, h))# ,np.arange(min_min, min_max, h),np.arange(max_min, max_max, h),np.arange(a25_min, a25_max, h),np.arange(a50_min, a50_max, h),np.arange(a75_min, a75_max, h),np.arange(std_min, std_max, h))
# testing = f'''linear.predict(np.c_[{', '.join(['sensor_revaling['+str(i)+']'+'.ravel()' for i in range(len(sensor_revaling))])}])'''
# print(testing)
# Z = eval(testing)
# predictions = np.array([[sensor_list[k][i] for k in sensor_list.keys()] for i in range(len(sensor_list['mean']))])
# print(predictions)

# ALL
# mgrid = eval(f"""np.meshgrid({", ".join(["primal_grid["+str(i)+"]" for i in range(len(primal_grid))])})""")
# SOME
plot_grid = eval(f"""np.meshgrid({", ".join(["primal_grid["+str(i)+"]" for i in range(2)])})""")



# plot all the colors
# Z_finder = f"""linear.predict(np.c_[{", ".join(["plot_grid["+str(i)+"].ravel()" for i in range(len(plot_grid))])}])"""
def chooser(n, l=list(), t=list(), i=0):
    if i == len(n):
        temp_array = np.append(t, np.array([mean_grid[i] for i in range(len(t), len(mean_grid))]))
        print(f"trying t: {temp_array}, leftovers: {np.array([mean_grid[i] for i in range(len(t), len(mean_grid))])}")
        l.append(linear.predict([temp_array]))
    else:
        for a in n[i]:
            if i == len(t):
                t.append(a)
            else: t[i] = a
            chooser(n, l=l, t=t, i=i+1)
    return l
# linear.predict()
Z = np.array([chooser(primal_grid[0:2])])# eval(Z_finder)
# Z = linear.predict(np.c_[sensor_revaling[0].ravel(), sensor_revaling[1].ravel()])
print(f"reshaping to {plot_grid[0].shape}")
Z = Z.reshape(plot_grid[0].shape)


plt.contourf(plot_grid[0], plot_grid[1], Z, cmap=plt.cm.PuBuGn, alpha=0.7)
plt.scatter(sensor_list[0]['mean'], sensor_list[0]['std'], c=random_output, cmap=plt.cm.PuBuGn, edgecolors='grey')
plt.xlabel('mean of window')
plt.ylabel('std of window')
plt.xlim(plot_grid[0].min(), plot_grid[0].max())
plt.ylim(plot_grid[1].min(), plot_grid[1].max())
plt.xticks(())
plt.yticks(())
plt.title('output')
plt.show()


