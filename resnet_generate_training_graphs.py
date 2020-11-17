import re
import matplotlib.pyplot as plot


file = open("resnet_data.txt", "r")

models = []
curr_model = []
curr_epoch = []

for line in file:
  if "Best Model " in line:
    l = re.split('Best Model |, Training Accuracy: |, Validation Accuracy: |, Test Accuracy: |\n', line)
    r = re.split('Best Model batch_size:|, learning_rate:|, momentum:|, Training Accuracy: ', line)
    name = l[1]
    training = l[2]
    validation = l[3]
    test = l[4]
    bs = r[1]
    lr = r[2]
    m = r[3]
    models.append((name, training, validation, test, bs, lr, m, curr_model))
    curr_model = []
  elif "Epoch:" in line:
    epoch = re.split('Epoch:|\n', line)[1]
    curr_epoch.append(int(epoch))
  elif "Training Test: " in line:
    accuracy = re.split('\(|\%', line)[1]
    curr_epoch.append(float(accuracy))
  elif "Validation Test: " in line:
    accuracy = re.split('\(|\%', line)[1]
    curr_epoch.append(float(accuracy))

    curr_model.append(curr)
    curr = []

model_sorted_validation = sorted(models, key=lambda x: float(x[2]))

worst_model = model_sorted_validation[0]
best_model = model_sorted_validation[-1]

print("Best Model: " + best_model[0])
print("Worst Model: " + worst_model[0])

# print graphs for best model
model = worst_model
data = model[-1]
epochs = [x[0] for x in data]
training_accs = [x[1] for x in data]
validation_accs = [x[2] for x in data]
fig, ax = plot.subplots()
ax.plot(epochs, training_accs, label="Training Dataset")
ax.plot(epochs, validation_accs, label="Validation Dataset")
ax.set_xlabel("Epochs Trained")
ax.set_ylabel("Prediction Accuracy")
ax.set_title("Epochs Trained vs Prediction Accuracy")
ax.legend()
fig.savefig("worst_resnet_accuracy_per_epoch.png")

# print graphs for best model
model = best_model
data = model[-1]
epochs = [x[0] for x in data]
training_accs = [x[1] for x in data]
validation_accs = [x[2] for x in data]
fig, ax = plot.subplots()
ax.plot(epochs, training_accs, label="Training Dataset")
ax.plot(epochs, validation_accs, label="Validation Dataset")
ax.set_xlabel("Epochs Trained")
ax.set_ylabel("Prediction Accuracy")
ax.set_title("Epochs Trained vs Prediction Accuracy")
ax.legend()
fig.savefig("best_resnet_accuracy_per_epoch.png")