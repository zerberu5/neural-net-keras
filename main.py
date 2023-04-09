from keras.layers.core import Dense
from keras.models import Sequential


def read_training_data(training_data_txt):
    training_string = open(training_data_txt, 'r').read().split("\n")
    training_data = []
    targets = []
    for line in training_string:
        line_arr = line.split(",")

        coordinates = [float(line_arr[0]), float(line_arr[1])]
        training_data.append(coordinates)

        targets.append(float(line_arr[2]))
    return training_data, targets


def read_test_data(test_data_txt):
    test_string = open(test_data_txt, 'r').read().split("\n")
    test_data = []

    for line in test_string:
        line_arr = line.split(",")

        coordinates = [float(line_arr[0]), float(line_arr[1])]
        test_data.append(coordinates)
    return test_data


def run_net(training_data_txt, test_data_txt):
    training_data, targets = read_training_data(training_data_txt)
    model = build_model()
    model.fit(training_data, targets, epochs=50, batch_size=10)
    test_data = read_test_data(test_data_txt)
    test_results = model.predict(test_data)
    formatted_results = []
    for result in test_results:
        if result >= 0:
            formatted_results.append(1)
        else:
            formatted_results.append(-1)
    return formatted_results


def build_model():
    model = Sequential()
    model.add(Dense(5, input_dim=2, activation='tanh'))
    model.add(Dense(1, activation='tanh'))
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    return model


if __name__ == "__main__":
    print(run_net('data/training.txt', 'data/test.txt'))
